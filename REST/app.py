from flask import Flask, render_template, redirect, url_for, abort, request
from flask_sqlalchemy import SQLAlchemy
from .forms import LoginForm, RegisterForm, AddPassForm
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
encryptor = Encryptor()


@app.route('/')
def init():
    return redirect(url_for('login'))


from .models import User, Data


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
                return redirect(url_for('user', username=db_user.name, id=db_user.id, user=db_user))
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/registration', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_exists = User.query.filter_by(name=form.user_name.data).first()
        if user_exists is None and form.master_password.data == form.second_password.data:
            user = User()
            user.name = form.user_name.data
            user.master_password = encryptor.encrypt(form.master_password.data)
            user.email = form.email.data
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user', username=user.name))
        form.user_name.errors.append('That user exists.')
    return render_template('register.html', form=form)


@app.route('/home/<username>/', methods=["GET", "POST"])
@login_required
def user(username):
    return render_template('home.html', username=username, data=Data.query.filter_by(user_id=current_user.id), id=current_user.id)


@app.route('/home/<username>/<id>/add', methods=["GET", "POST"])
@login_required
def addPassword(username, id):
    form = AddPassForm()
    if form.validate_on_submit():
        print(form.password.data, form.confirm_password.data)
        if form.password.data == form.confirm_password.data:
            data = Data()
            data.user_id = current_user.id
            data.site_name = form.site_name.data
            data.username = form.username.data
            data.password = encryptor.encrypt(form.password.data)
            db.session.add(data)
            db.session.commit()
            print(current_user.id)
            return redirect(url_for('user', username=username))
        else:
            form.confirm_password.errors.append('The passwords are not the same.')
    else:
        return render_template('addPass.html', form=form)


@login_manager.user_loader
def load_user(name):
    return User.query.get(name)
