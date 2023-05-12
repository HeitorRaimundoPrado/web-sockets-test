from flask import Blueprint, render_template, request, redirect
from __init__ import socket_


rooms = list()

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        rooms.append(len(rooms)+1)
        return redirect(request.url)

    else:
        return render_template('index.html', sync_mode=socket_.async_mode, rooms=rooms)
