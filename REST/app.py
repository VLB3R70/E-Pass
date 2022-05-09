from datetime import timedelta

from flask import Flask, render_template, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from .forms import LoginForm
from REST.config import Config
from API.Encryption import Encryptor, Decryptor
from flask_login import LoginManager, current_user, login_required, login_user, logout_user

app = Flask(__name__)
app.config.from_object(Config)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
db = SQLAlchemy(app)
decryptor = Decryptor()


@app.route('/')
def init():
    return redirect(url_for('login'))


from .models import User


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = form.user_name.data
        password = form.master_password.data
        if User.query.filter_by(name=user).first():
            db_user = User.query.filter_by(name=user).first()
            if password == decryptor.decrypt(password=db_user.master_password):
                login_user(db_user)
                return redirect(url_for('user', username=db_user.name))
    return render_template('login.html', form=form)


@app.route('/user/<username>', methods=["GET", "POST"])
@login_required
def user(username):
    return render_template('home.html', user=username)


@login_manager.user_loader
def load_user(name):
    return User.query.get(name)
