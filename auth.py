from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        return redirect(url_for('main.home'))

    else:
        return render_template('login.html')

@bp.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return redirect(url_for('auth.login'))
    
    else:
        return render_template('register.html')
