from flask import Blueprint, render_template, request, flash, redirect, url_for   
from flask_login import login_user, login_required, logout_user, current_user
import re
from .models import User
from . import db
from werkzeug.security import generate_password_hash,check_password_hash

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def check(email):
    if(re.fullmatch(regex, email)):
        return False
    else:
        return True        
auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        passw = request.form.get('pass')
        print(email, passw)
        user = User.query.filter_by(email = email).first()

        if user:
            if check_password_hash(user.password, passw):
                flash("logged in successfully", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:   
                flash("Incorrect password", category='error')
        else:
            flash("No such user found", category='error')

    return render_template("login.html" ,user=current_user)

@auth.route('/logout')
@login_required
def Logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        uname = request.form.get('uname')
        email = request.form.get('email')
        passw = request.form.get('pass')
        cpassw = request.form.get('cpass')
        print(passw)
        print(cpassw)
        
        exist = User.query.filter_by(username = uname).first()
        eexist = User.query.filter_by(email = email).first()
        
        if exist:
            flash("Username already taken!", category='error')
        elif check(email):
            flash("Enter a valid email!", category='error')
        elif eexist:
            flash("email already taken!", category='error')
        elif passw != cpassw:
            flash("Both passwords must match!", category='error')
        else:
            new_user = User(username=uname,email=email,password=generate_password_hash(passw), status='n')
            db.session.add(new_user)
            db.session.commit()
            flash("Account created", category='success')
            user = User.query.filter_by(username = uname).first()
            login_user(user, remember=True)
            return redirect(url_for('views.home'))

    return render_template("signup.html", user=current_user)
