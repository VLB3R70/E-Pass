"""
.. module:: login
    :synopsis:

This module is used to log in and log out a user from a ``session`` from flask. The ``LoginManager`` object needs this
data to work properly.

"""
from flask import session


def login_user(user):
    """

    This function adds the information of the user logged to the ``session`` object.

    :param user: Is the user that is trying to log in

    """
    session["name"] = user.name
    session["master_password"] = user.master_password
    session["email"] = user.email


def logout_user():
    """

    This function drops all the information about the user logged so the next time will ask again for a login.

    When the time set in the :py:meth:`REST.config` for the user to be active is exceeded this function is called.

    """
    session.pop("name", None)
    session.pop("master_password", None)
    session.pop("email", None)
