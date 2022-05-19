"""
.. module:: forms
    :synopsis:

This module implements all the necessary forms for the app. These forms are called at the start of the functions from
the :py:meth:`REST.app` module.
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    """

    This class represents the form the user will see during login. It sets up two entries: the one for the `username`,
    for the `master password` and a button to submit the data.

    The `username` and the `master password` are required which means that the user must enter data on that entries.

    """
    user_name = StringField("Enter your username", validators=[DataRequired()])
    master_password = PasswordField(
        "Enter your master password", validators=[DataRequired()]
    )
    login = SubmitField("Log in")


class RegisterForm(FlaskForm):
    """

    This class represents the form the user will see during a registration. It sets up four entries: the `username`, the
    `master password`, an entry to enter the `master password` once again and the `email` entry. It also implements a
    button to submit the fields.

    The `username`, `master password` and `second password` entries are required.

    """
    user_name = StringField("Enter the username", validators=[DataRequired()])
    master_password = PasswordField(
        "Enter the master password", validators=[DataRequired()]
    )
    second_password = PasswordField(
        "Enter the master password again", validators=[DataRequired()]
    )
    email = StringField("Enter your email (Optional)")
    register = SubmitField("Register me")


class AddPassForm(FlaskForm):
    """

    This class represents the form the user will see during adding a password. It sets up three entries: the `site name`
    , the `username` and the `password`. It also implements a button to submit the fields.

    The `site name`, `master password` and `username` entries are required.

    """
    site_name = StringField("Enter the site name:", validators=[DataRequired()])
    username = StringField("Enter your username:")
    password = PasswordField(
        "Enter the password of the site:", validators=[DataRequired()]
    )
    confirm_password = PasswordField(
        "Confirm the password:", validators=[DataRequired()]
    )
    addPassword = SubmitField("Add new password")


class DeletePassForm(FlaskForm):
    """

    This class represents the form the user will see during deleting a password. It sets up one entry for the `id` of
    the password and a button to submit the data.

    The `id` entry is required.

    """
    id = IntegerField("Enter the ID of the password:", validators=[DataRequired()])
    delete = SubmitField("Delete")


class ModifyPassForm(FlaskForm):
    """

    This class represents the form the user will see during modifying a password. It sets up five entries: the `id`, the
    `new site name`, the `new username`, the `new password`, a second entry to enter the `new password` and the button
    to submit the data

    None entries are required.

    """
    id = IntegerField("Enter the ID of the password:")
    new_site_name = StringField("Enter the new site name:")
    new_username = StringField("Enter the new username:")
    new_password = StringField("Enter the new password:")
    confirm_password = StringField("Enter the password again:")
    modify = SubmitField("Modify")
