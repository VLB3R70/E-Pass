import os
from pathlib import Path


class Config(object):
    SECRET_KEY = 'wUn8McRT13KDVjXVO3eT5fHvfopq6FpbDXkuznt5_rhpYSMWoeBana7xPWnxAtjC4-8Ql1ihvVHMTiqUBU2VaQ'

    DATA_DIRECTORY = os.path.join(Path.home(), '.EPass/')
    DATABASE_PATH = os.path.join(DATA_DIRECTORY, ".epass.sqlite")

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/.epass.sqlite'.format(DATA_DIRECTORY)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
