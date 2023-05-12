from flask import Blueprint, render_template
from flask_login import current_user, login_required
from __init__ import socket_
import events

bp = Blueprint('room', __name__)

@bp.route('/room/<int:id>', methods=['GET', 'POST'])
@login_required
def room(id: int):
    return render_template('room.html', sync_mode=socket_.async_mode, id=id , user_id=current_user.id) # type: ignore
