from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    user_name = StringField('Enter your username', validators=[DataRequired()])
    master_password = PasswordField('Enter your master password', validators=[DataRequired()])
    login = SubmitField('Log in')


class RegisterForm(FlaskForm):
    user_name = StringField('Enter the username', validators=[DataRequired()])
    master_password = PasswordField('Enter the master password', validators=[DataRequired()])
    second_password = PasswordField('Enter the master password again', validators=[DataRequired()])
    email = StringField('Enter your email (Optional)')
    register = SubmitField('Register me')


class AddPassForm(FlaskForm):
    site_name = StringField('Enter the site name:', validators=[DataRequired()])
    username = StringField('Enter your username:')
    password = PasswordField('Enter the password of the site:', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm the password:', validators=[DataRequired()])
    addPassword = SubmitField('Add new password')


class DeletePasswordForm(FlaskForm):
    id = IntegerField('Enter the ID of the password:', validators=[DataRequired()])
    delete = SubmitField('Delete')
