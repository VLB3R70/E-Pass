from sqlalchemy import ForeignKey, Column, Integer, Text
from sqlalchemy.orm import backref

from .app import db


class User(db.Model):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Text, nullable=False, unique=True)
    master_password = Column(Text, nullable=False)
    email = Column(Text, nullable=False)

    # def is_authenticated(self):
    #     return False
    #
    # def is_active(self):
    #     return True
    #
    # def is_anonymous(self):
    #     return False
    #
    # def get_id(self):
    #     return str(self.id)


class Data(db.Model):
    __tablename__ = "Data"
    id = Column(db.Integer, primary_key=True, nullable=False)
    user_id = Column(
        Integer,
        ForeignKey("User.id", ondelete="cascade", onupdate="cascade"),
        nullable=False,
    )
    user = db.relationship("User", backref=backref("Data", uselist=False))
    site_name = Column(Text, nullable=False)
    username = Column(Text, nullable=False)
    password = Column(Text, nullable=False)
