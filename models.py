import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    comment = db.Column(db.String(1000))

    def __repr_(self):
        return '<Name: %r>' % self.name


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    username = db.Column(db.String(16), unique=True)
    password = db.Column(db.String(16))
    email = db.Column(db.String(64), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.date.today())

    def __init__(self, firstname, lastname, username, password, email):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.username = username
        self.set_password(password)
        self.email = email.lower()


    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)

    def __repr_(self):
        return '<Member: %r>' % self.username
