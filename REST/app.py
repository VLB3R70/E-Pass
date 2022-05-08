from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from .forms import LoginForm
from .config import Config
from API.Encryption import Encryptor, Decryptor

app = Flask(__name__)
app.config.from_object(Config)
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
                print('Successful login')
                return redirect(url_for('user'))
    return render_template('login.html', form=form)


@app.route('/user/<username>')
def user():
    pass


if __name__ == '__main__':
    app.run()
