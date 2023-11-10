from flask import *
from flask_sqlalchemy import SQLAlchemy
from database.db import Database
from database.models import User, db
from database import crud
from werkzeug.utils import secure_filename

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///"C:\Users\user\Desktop\ictProject\usersdb.db"'


app.config['SECRET_KEY']="my secret key here"


db.init_app(app)

@app.route('/')
def mainpahe():
    return render_template('main.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        user = db.session.query(User).filter_by(email=request.form['email'], password=request.form['password']).first()
        print(user)
        if user:
            session['authenticated'] = True
            session['uid'] = user.user_id
            session['email'] = user.email
            return redirect(url_for('userpage', user_id=user.user_id))
        else:
            return render_template('login_page.html', context='SOMETHING WENT WRONG, TRY AGAIN!')
    else:
        return render_template('login_page.html')

@app.route("/logout")
def logout():
    session.pop('authenticated', None)
    session.pop('uid', None)
    session.pop('username', None)
    return redirect(url_for('mainpahe'))

@app.route('/signup', methods = ['GET', 'POST'])
def register(context=None):
    if request.method == 'POST':
        email = request.form['email']
        fname = request.form['fname']
        sname = request.form['sname']
        pssw = request.form['password']

        data = db.session.query(User).filter_by(email=request.form['email']).first()
        
        if data:
            return redirect(url_for('signup', context='ALREADY EXISTS!'))
        else:
            crud.add_user(User(email=email, 
                                user_fname=fname,
                                user_sname=sname,
                                password=pssw))
            return redirect(url_for('login', context='DONE'))
    return render_template('signup_page.html', context=context)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)
