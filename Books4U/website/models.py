from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    uId = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique = True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    status = db.Column(db.String(10)) 
    books = db.relationship('Books')
    transactions = db.relationship('Transactions')
    verify = db.relationship('Verify')

    def get_id(self):
           return (self.uId)

class Books(db.Model):
    bId = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    author = db.Column(db.String(50))
    price = db.Column(db.Integer)
    bDesc = db.Column(db.String(1000))
    status = db.Column(db.String(10))
    genre = db.Column(db.String(20))
    cover = db.Column(db.String(100))
    uId = db.Column(db.Integer, db.ForeignKey('user.uId'))

class Transactions(db.Model):
    tId = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    uId = db.Column(db.Integer, db.ForeignKey('user.uId'))

class Verify(db.Model):
    vId = db.Column(db.Integer, primary_key=True)
    tyOf = db.Column(db.Integer)
    res = db.Column(db.String(10))
    uId = db.Column(db.Integer, db.ForeignKey('user.uId'))