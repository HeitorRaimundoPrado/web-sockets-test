from flask import Flask
from flask_socketio import SocketIO
from threading import Lock
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager

db = SQLAlchemy()

async_mode = None
thread = None
thread_lock = Lock()

users = list()

socket_ = SocketIO()

def create_app(debug=False):
    app = Flask(__name__)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' # type: ignore
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.config['SECRET_KEY'] = 'SECRET'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    app.debug = debug

    socket_.init_app(app)

    import models

    db.init_app(app)
    with app.app_context():
        db.create_all()


    import main
    import room
    import auth

    app.register_blueprint(main.bp)
    app.register_blueprint(room.bp)
    app.register_blueprint(auth.bp)
    return app

