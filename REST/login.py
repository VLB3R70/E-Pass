from flask import session, redirect


def login_user(User):
    session["name"] = User.name
    session["master_password"] = User.master_password
    session["email"] = User.email


def logout_user():
    session.pop("name", None)
    session.pop("master_password", None)
    session.pop("email", None)
