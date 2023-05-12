from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from flask_login import login_user, logout_user, login_required
from __init__ import db

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('bemail')
        password = request.form.get('bpassword')


        if email is None or password is None:
            flash('Fill all information!')
            return redirect(request.url)

        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            flash('Email or password wrong')
            return redirect(request.url)

        login_user(user)

        return redirect(url_for('main.index'))

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

        new_user = User(email=email, name=username, password=generate_password_hash(password, method='sha256')) # type: ignore

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    
    else:
        return render_template('register.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
