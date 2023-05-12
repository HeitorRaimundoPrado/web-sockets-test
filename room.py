from flask import Blueprint, render_template
from __init__ import socket_

bp = Blueprint('room', __name__)

@bp.route('/room/<int:id>', methods=['GET', 'POST'])
def room(id: int):
    return render_template('room.html', sync_mode=socket_.async_mode, id=id , user_id=1)
