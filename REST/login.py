from flask import session, redirect


def login_user(user):
    session["name"] = user.name
    session["master_password"] = user.master_password
    session["email"] = user.email


def logout_user():
    session.pop("name", None)
    session.pop("master_password", None)
    session.pop("email", None)
