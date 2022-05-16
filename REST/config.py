from datetime import timedelta

from CORE.data import Data
import secrets

data = Data()


class Config(object):
    SECRET_KEY = secrets.token_urlsafe(64)
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)
    TEMPLATES_AUTO_RELOAD = True
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(data.DATABASE_PATH)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
