from flask import Flask
from flask_login import current_user, LoginManager, UserMixin
from flask_socketio import SocketIO
from threading import Lock
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

async_mode = None
thread = None
thread_lock = Lock()

users = list()

socket_ = SocketIO()

def create_app(debug=False):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'SECRET'
    app.debug = debug

    socket_.init_app(app)


    import main
    import room
    import auth

    app.register_blueprint(main.bp)
    app.register_blueprint(room.bp)
    app.register_blueprint(auth.bp)
    return app

