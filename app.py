from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO, send, join_room, leave_room, emit
from threading import Lock

async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET'
socket_ = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

rooms = list()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        rooms.append(len(rooms)+1)
        return redirect(request.url)

    else:
        return render_template('index.html', sync_mode=socket_.async_mode, rooms=rooms)

@app.route('/room/<int:id>', methods=['GET', 'POST'])
def room(id: int):
    return render_template('room.html', sync_mode=socket_.async_mode, id=id, user_id=1 )

@socket_.on('join', namespace='/message')
def on_join(data):
    user = data['user_id']
    room = data['room']
    join_room(room)
    send(str(user) + 'has entered the room', to=room)
    app.logger.debug(str(user) + 'has entered room ' + str(room))

@socket_.on('leave', namespace='/message')
def on_leave(data):
    user = data['user_id']
    room = data['room']
    leave_room(room)
    send(str(user) + 'has left the room', to=room)
    app.logger.debug(str(user) + 'has left room ' + str(room))

@socket_.on('message', namespace='/message')
def on_msg(data):
    msg = data['msg']
    room = data['room']
    emit("msg", {'data': msg}, to=room)
    app.logger.debug('received message')


if __name__ == '__main__':
    socket_.run(app, debug=True)
