from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

app = Flask(__name__)



# # Adding SQLite3 database URI to a config

app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Users\ggene\OneDrive\Рабочий стол\ass3 py\usersdb.db'


app.config['SECRET_KEY']="my secret key here"


db.init_app(app)