from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    user_name = StringField('Enter your username', validators=[DataRequired()])
    master_password = PasswordField('Enter your master password', validators=[DataRequired()])
    login = SubmitField('Log in')