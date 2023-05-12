from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from __init__ import db

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
        email = request.form.get('bemail')
        username = request.form.get('busername')
        password = request.form.get('bpassword')

        if email is None or username is None or password is None:
            flash('All fields must be filled to signup!')
            return redirect(url_for('auth.register'))

        user = User.query.filter_by(email=email).first()

        if user:
            flash('User with this email already exists!')
            return redirect(url_for('auth.register'))

        new_user = User(email=email, name=username, password=generate_password_hash(password, method='sha256'))

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    
    else:
        return render_template('register.html')

@bp.route('/logout')
def logout():
    return redirect(url_for('main.home'))
