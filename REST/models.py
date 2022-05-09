from .app import db, LOGIN_MANAGER
from sqlalchemy import VARCHAR, ForeignKey, Column


@LOGIN_MANAGER.user_loader
def load_user(name):
    return User.query.get(name)


class User(db.Model):
    __tablename__ = 'User'
    name = Column(VARCHAR(50), primary_key=True, nullable=False)
    master_password = Column(VARCHAR(100), nullable=False)
    email = Column(VARCHAR(100))


class Data(db.Model):
    __tablename__ = 'Data'
    id = Column(db.Integer, primary_key=True)
    user = Column(db.VARCHAR(50), ForeignKey('User.name', ondelete='cascade', onupdate='cascade'), nullable=False)
    site_name = Column(db.VARCHAR(100), nullable=False)
    username = Column(db.VARCHAR(100), nullable=False)
    password = Column(db.VARCHAR(100), nullable=False)
