from flask_sqlalchemy import SQLAlchemy
from flaskapp import db
from flask import Flask

app = Flask(__name__)



class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True) # integer primary key will be autoincremented by default
    email = db.Column(db.String(255), unique=True, nullable=False)
    user_fname = db.Column(db.String(255))
    user_sname = db.Column(db.String(255))
    password = db.Column(db.String(255), nullable=False)
    
    def __repr__(self) -> str:
        return f"User(user_id {self.user_id!r}, name={self.user_fname!r}, surname={self.user_sname!r})"