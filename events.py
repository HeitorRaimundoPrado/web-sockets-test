from __init__ import socket_
from flask_socketio import send, join_room, leave_room, emit
from flask import current_app
from flask_login import current_user

@socket_.on('join')
def on_join(data):
    user = data['user_id']
    room = data['room']
    join_room(room)
    send(str(user) + 'has entered the room', to=room)
    # current_app.logger.warn("user joined room" + str(room))
    # current_app.logger.debug(str(user) + 'has entered room ' + str(room))

@socket_.on('leave')
def on_leave(data):
    user = data['user_id']
    room = data['room']
    leave_room(room)
    send(str(user) + 'has left the room', to=room)
    # current_app.logger.debug(str(user) + 'has left room ' + str(room))

@socket_.on('message')
def on_msg(data):
    msg = data['msg']
    room = data['room']
    emit("msg", {'data': msg, 'user_id': current_user.id}, to=room) # type: ignore
    # current_app.logger.debug('received message')

@socket_.on('connect')
def on_connect():
    # current_app.logger.warn('CONECTED')
    pass

