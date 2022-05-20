"""
.. module:: models
    :synopsis:

This module is in charge of the models of the database. When using an `ORM` `Object Relational Mapper`, we need to declare
the same objects as the tables in the database. In this case, the ``EPass`` database has two tables :py:class:`User` and
:py:class:`Data` so we need to instance two classes with the same names and properties.

"""
from sqlalchemy import ForeignKey, Column, Integer, Text
from sqlalchemy.orm import backref

from .app import db


class User(db.Model):
    """
    .. class:: User

    This class represents the table ``User`` from the database and has the same properties. To be, an `id`, the `name`
    of the user, the `master password` and the `email`. When doing queries, the `ORM` uses the properties from the class
    as columns of the table with the same name in the database.

    """
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Text, nullable=False, unique=True)
    master_password = Column(Text, nullable=False)
    email = Column(Text, nullable=False)

    def is_authenticated(self):
        """

        This function checks if the user is authenticated and returns its value. By default the user isn't authenticated
        so the value will be ``False`` but when the user logs in the value change to ``True``

        :return: It returns if the user is authenticated or not

        :rtype: bool

        """
        return False

    def is_active(self):
        """
        This function is similar to previous. When a user ``is active

        :return: It returns if the user is authenticated or not

        :rtype: bool

        """
        return True

    def get_id(self):
        """
        This functions returns the ID of the user logged.

        :return: It returns the ID of the user

        :rtype: str
        """
        return str(self.id)


class Data(db.Model):
    """
    .. class:: Data

    This class represents the table ``Data`` from the database and has the same properties. To be, the `id`, the
    `user id`, the `site name`, the `username` and the `pasword`.

    The ``user_id`` property indicates the relationship between the :py:class:`User` class and table in the database.

    """
    __tablename__ = "Data"
    id = Column(db.Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("User.id", ondelete="cascade", onupdate="cascade"), nullable=False, )
    user = db.relationship("User", backref=backref("Data", uselist=False))
    site_name = Column(Text, nullable=False)
    username = Column(Text, nullable=False)
    password = Column(Text, nullable=False)
