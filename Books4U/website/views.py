from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for, send_from_directory, app, current_app
from flask_sqlalchemy import SQLAlchemy
from fileinput import filename
from flask_login import login_required, current_user
from os.path import join, dirname, abspath
from . import db
from .models import Books
import os
from werkzeug.utils import secure_filename
views = Blueprint('views',__name__)
enctype="multipart/form-data" 

@views.route('/')
def home():
    return render_template("home.html", user=current_user)

@views.route('/sell', methods=['GET', 'POST'])
def sell():
    if request.method == "POST":
        image = request.files['file']

        filename = secure_filename(image.filename)
        basedir = os.path.abspath(os.path.dirname(__file__))
        sv = (basedir,current_app.config["IMAGE_UPLOADS"])
        image.save(sv,image.filename)

    return render_template("sell.html", user = current_user)

@views.route('/info')
def info():
    title="Integration"
    author="Educational Guides"
    price=600
    bDesc="Test"
    status="NotSold"
    genre="Educational"
    cover="/static/uploads/Integration.jpeg"
    
    i = Books(title=title,author=author,price=price,bDesc=bDesc,status=status,genre=genre,cover=cover)
    
    b = Books.query.all()
    return render_template("info.html",user=current_user,data = b)

@views.route('/verify')
def verify():
    return render_template("verify.html",user=current_user)

@views.route('/search')
def search():
    return render_template("search.html",user=current_user)