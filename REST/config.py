"""
.. module:: config

This module is used to set up some configurations to the flask app.

"""
from datetime import timedelta

from CORE.data import Data
import secrets

data = Data()


class Config(object):
    """
    This class implements extra configuration for the flask app to run like the URI to the database or the maximum time
    a session last.

    This object is called during the instance of the app object in :py:meth:`REST.app`

    """
    SECRET_KEY = secrets.token_urlsafe(64)
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)
    TEMPLATES_AUTO_RELOAD = True
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(data.DATABASE_PATH)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
