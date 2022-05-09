from API.data import Data
from flask_login import LoginManager

data = Data()


class Config(object):
    SECRET_KEY = 'wUn8McRT13KDVjXVO3eT5fHvfopq6FpbDXkuznt5_rhpYSMWoeBana7xPWnxAtjC4-8Ql1ihvVHMTiqUBU2VaQ'

    DEBUG = 'True'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(data.DATABASE_PATH)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
