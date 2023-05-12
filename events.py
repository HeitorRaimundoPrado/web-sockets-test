from . import socket_
from flask_socketio import send, join_room, leave_room, emit
from flask import current_app

@socket_.on('join', namespace='/message')
def on_join(data):
    user = data['user_id']
    room = data['room']
    join_room(room)
    send(str(user) + 'has entered the room', to=room)
    current_app.logger.debug(str(user) + 'has entered room ' + str(room))

@socket_.on('leave', namespace='/message')
def on_leave(data):
    user = data['user_id']
    room = data['room']
    leave_room(room)
    send(str(user) + 'has left the room', to=room)
    current_app.logger.debug(str(user) + 'has left room ' + str(room))

@socket_.on('message', namespace='/message')
def on_msg(data):
    msg = data['msg']
    room = data['room']
    emit("msg", {'data': msg}, to=room)
    current_app.logger.debug('received message')

@socket_.on('connect', namespace='/message')
def on_connect():
    pass

