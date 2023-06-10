from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=False)
    email = db.Column(db.String(50), nullable=False, unique=False)
    number = db.Column(db.String(50), nullable=False, unique=False)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    def __init__(self, name, email, number, username, password):
        self.name = name
        self.email = email
        self.number = number
        self.username = username
        self.password = generate_password_hash(password) 

    def saveUser(self):
        db.session.add(self)
        db.session.commit()


class customerContact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    number = db.Column(db.String(50), nullable=False, unique=True)
    comments = db.Column(db.String(100), nullable=False, unique=True)

    def __init__(self, name, email, number, comments):
        self.name = name
        self.email = email
        self.number = number
        self.comments = comments
        
    def saveNumber(self):
        db.session.add(self)
        db.session.commit()
