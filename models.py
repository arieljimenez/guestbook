from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    comment = db.Column(db.String(1000))
