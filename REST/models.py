from .app import db, login_manager
from sqlalchemy import VARCHAR, ForeignKey, Column, Integer


class User(db.Model):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(50), nullable=False)
    master_password = Column(VARCHAR(100), nullable=False)
    email = Column(VARCHAR(100))

    def is_authenticated(self):
        return False

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


class Data(db.Model):
    __tablename__ = 'Data'
    id = Column(db.Integer, primary_key=True)
    user = Column(db.VARCHAR(50), ForeignKey('User.name', ondelete='cascade', onupdate='cascade'), nullable=False)
    site_name = Column(db.VARCHAR(100), nullable=False)
    username = Column(db.VARCHAR(100), nullable=False)
    password = Column(db.VARCHAR(100), nullable=False)
