import os

import sqlalchemy.exc
from flask import Flask, render_template, redirect, url_for, flash
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy

from API.Encryption import Encryptor, Decryptor
from API.data import Data as data
from REST.config import Config
from .forms import LoginForm, RegisterForm, AddPassForm, DeletePassForm, ModifyPassForm

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


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


from .models import User, Data


@app.route('/registration', methods=["GET", "POST"])
def register():
    if not os.path.exists(data.DATA_DIRECTORY):
        os.mkdir(data.DATA_DIRECTORY)
    elif not os.path.exists(data.DATABASE_PATH):
        open(data.DATABASE_PATH, 'w')
        db.create_all()
    global user
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
    # if request.form["copy"] == "Copy to clipboard!":
    #     data = Data.query.filter_by(id=id, user_id=current_user.id).first()
    #     password = decryptor.decrypt(data.password)
    #     pc.copy(password)
    #     flash('Password successfully copied to clipboard!')
    # else:
    return render_template('home.html', username=username, data=Data.query.filter_by(user_id=current_user.id),
                           id=current_user.id)


@app.route('/home/<username>/add', methods=["GET", "POST"])
@login_required
def addPassword(username):
    form = AddPassForm()
    if form.validate_on_submit():
        if form.password.data == form.confirm_password.data:
            data = Data()
            data.user_id = current_user.id
            data.site_name = form.site_name.data
            data.username = form.username.data
            data.password = encryptor.encrypt(form.password.data)
            db.session.add(data)
            db.session.commit()
            return redirect(url_for('user', username=username))
        else:
            form.confirm_password.errors.append('The passwords are not the same.')
    else:
        return render_template('addPass.html', form=form)


@app.route('/home/<username>/modify', methods=["GET", "POST"])
@login_required
def modifyPassword(username):
    form = ModifyPassForm()
    num_passwords = Data.query.filter_by(user_id=current_user.id).count()
    if form.validate_on_submit():
        old_data = Data.query.filter_by(id=form.id.data, user_id=current_user.id).first()
        new_data = Data()
        new_data.user_id = current_user.id
        if form.id.data != "":
            if form.new_site_name.data != "":
                new_data.site_name = form.new_site_name.data
            else:
                new_data.site_name = old_data.site_name
            if form.new_username.data != "":
                new_data.username = form.new_username.data
            else:
                new_data.username = old_data.username
            if form.new_password.data != "" and form.new_password.data == form.confirm_password.data:
                new_data.password = form.new_password.data
            elif form.new_password.data != form.confirm_password.data:
                flash('The passwords must be the same')
            else:
                new_data.password = old_data.password
            db.session.delete(old_data)
            db.session.commit()
            new_data.id = num_passwords + 1
            db.session.add(new_data)
            db.session.commit()
            return redirect(url_for('user', username=username))
    else:
        return render_template('modify.html', form=form, data=Data.query.filter_by(user_id=current_user.id))


@app.route('/home/<username>/delete', methods=["GET", "POST"])
@login_required
def delete_password(username):
    form = DeletePassForm()
    if form.validate_on_submit():
        data = Data.query.filter_by(id=form.id.data, user_id=current_user.id).first()
        db.session.delete(data)
        db.session.commit()
        return redirect(url_for('user', username=username))
    else:
        return render_template('delete.html', form=form, data=Data.query.filter_by(user_id=current_user.id))


@login_manager.user_loader
def load_user(name):
    return User.query.get(name)
