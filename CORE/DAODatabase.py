"""
.. module:: DAODatabase
    :synopsis:

.. moduleauthor::
    `Alberto Jiménez <https://github.com/VLB3R70>`_

This module implements an object with all the necessary functions to get the data from the database.

"""
import os
import sqlite3

from CORE import Encryption
from .data import Data

data = Data()

databaseCreated = True

encryptor = Encryption


class DAO:
    """

    It is the class which implements de Data Access Object methods.

    """

    def __init__(self):
        try:
            self.connection = sqlite3.connect(
                data.DATABASE_PATH, check_same_thread=False
            )
            self.setup_database()
        except sqlite3.OperationalError:
            os.mkdir(data.DATA_DIRECTORY)
            open(data.DATABASE_PATH, "w")

    def database_empty(self):
        """
        It checks if the database is empty or not with a simple query.

        :return: It returns if the database is empty

        :rtype: bool

        """
        with self.connection:
            not_empty = self.connection.execute(data.USER_COUNT).fetchone()

            if not_empty:
                return False
            else:
                return True

    def setup_database(self):
        """
        This function executes the necessary queries to set up the database.

        """
        with self.connection:
            self.connection.executescript(data.SQL_START)

    def reset_database(self):
        """
        This function drops all the existing tables in the database and calls to
        :py:func:`setupDataBase()`

        """
        with self.connection:
            self.connection.executescript(data.SQL_RESET)
            self.setup_database()

    def new_user(self, username, master_password, email):
        """
        This function adds a new User in the database with the params that the user enters

        :param username: Is the username of the new user. It is used during the login

        :param master_password: Is the master password of the new user. This password is saved with an encryption. It is
            used during the login

        :param email: Is the email of the new user

        :type master_password: str

        :type username: str

        :type email: str

        """
        encrypted_pass = encryptor.encrypt(password=master_password)

        with self.connection:
            self.connection.execute(
                data.INSERT_NEW_USER, (username, encrypted_pass, email)
            )

    def get_users(self):
        """
        This function is used to get all the users in the database

        :return: It returns a list with all the usernames

        :rtype: list[str]

        """
        with self.connection:
            users = self.connection.execute(data.USER_COUNT).fetchall()
            return users

    def get_user_id(self, username):
        """
        This function is used to get the ID of the user

        :param username: Is the name of the user

        :type username: str

        :return: It returns the ID of the user with the same username

        """
        with self.connection:
            id = self.connection.execute(data.SELECT_USER_ID, (username,)).fetchone()

        return id[0]

    def get_master_password(self, user):
        """
        This function is used to get the decrypted password of the user with the same name as the given

        :param user: Is the name of the user

        :type user: str

        :return: It returns the decrypted password of the user

        :rtype: str

        """
        with self.connection:
            result = self.connection.execute(
                data.SELECT_USER_MASTER_PASSWORD, (user,)
            ).fetchone()
            decrypted_password = encryptor.decrypt(password=result[0])
        return decrypted_password

    def update_master_password(self, new_password, user):
        """
        This function is used to update the master password of the user given

        :param new_password: Is the new password of the user

        :type new_password: str

        :param user: Is the name of the user

        :type user: str

        """
        with self.connection:
            encrypted_password = encryptor.encrypt(new_password)
            self.connection.execute(
                data.UPDATE_MASTER_PASSWORD, (encrypted_password, user)
            )

    ########################################################################################

    def save_user_data(self, id, user_id, site_name, username, password):
        """
        This function is used to add a new password in the database. This password is linked with the user logged

        :param id: Is the ID of the new entry

        :type id: str

        :param user_id: Is the ID of the user logged

        :type user_id: str

        :param site_name: Is the URL or the name of the website

        :type site_name: str

        :param username: Is the username linked on the site name

        :type username: str

        :param password: Is the password used in the website or app. This password is saved with an encryption

        :type password: str

        """
        encrypted_password = encryptor.encrypt(password=password)
        with self.connection:
            self.connection.execute(
                data.INSERT_USER_DATA,
                (id, user_id, username, site_name, encrypted_password),
            )

    def get_user_data(self, user_id):
        """
        This function is used to get all the data of the user logged. It returns all the data with the same ID as the
        given

        :param user_id: Is the ID of the user logged

        :type user_id: int

        :return: It returns a list with all the entries of the database

        :rtype: list

        """
        with self.connection:
            user_data = self.connection.execute(
                data.SELECT_USER_DATA, (user_id,)
            ).fetchall()
        return user_data

    def get_user_password(self, id):
        """
        This function is used to get the password of the selected one by the ID

        :param id: The ID of the saved password

        :type id: int

        :return: It returns the decrypted password

        :rtype: str

        """
        with self.connection:
            user_password = self.connection.execute(
                data.SELECT_USER_PASSWORD, (id,)
            ).fetchone()
            decrypted_password = encryptor.decrypt(password=user_password[0])

        return decrypted_password

    def get_num_passwords(self, user_id):
        """
        This function is used to get the number of passwords saved by the logged user

        :param user_id: Is the ID of the logged user

        :type user_id: int

        :return: It returns the number of passwords saved

        :rtype: int

        """
        with self.connection:
            num_passwords = self.connection.execute(
                data.SELECT_COUNT_PASSWORDS, (user_id,)
            ).fetchone()

        return num_passwords[0]

    def get_username(self, id):
        """
        This function is used to get the username of the password saved by the logged user

        :param id: Is the ID of the password

        :type id: int

        :return: It returns the username of the password

        :rtype: str

        """
        with self.connection:
            user_name = self.connection.execute(data.SELECT_USER_NAME, (id,)).fetchone()

        return user_name[0]

    def update_site_name(self, id, new_site_name):
        """
        This function is used to update the site name of the password selected by it ID

        :param id: Is the ID of the password

        :type id: int

        :param new_site_name: Is the new site name of the password selected

        :type new_site_name: str

        """
        with self.connection:
            self.connection.execute(data.UPDATE_USER_SITENAME, (new_site_name, id))

    def update_username(self, id, new_username):
        """
        This function is used to update the username of the password selected by it ID

        :param id: Is the ID of the password

        :type id: int

        :param new_username: Is the new username of the password selected

        :type new_username: str

        """
        with self.connection:
            self.connection.execute(data.UPDATE_USER_NAME, (new_username, id))

    def update_user_password(self, id, new_password):
        """
        This function is used to update the password of the selected one by it ID

        :param id: Is the ID of the password

        :type id: int

        :param new_password: Is the new password of the selected one

        :type new_password: str

        """
        with self.connection:
            encrypted_password = encryptor.encrypt(new_password)
            self.connection.execute(data.UPDATE_USER_PASSWORD, (encrypted_password, id))

    def delete_one_password(self, id):
        """
        This function is used to delete the password selected by the user

        :param id: Is the ID of the selected password

        :type id: int

        """
        with self.connection:
            self.connection.execute(data.DELETE_ONE_PASSWORD, (id,))

    def delete_many_passwords(self, id_list):
        """
        This function is used to delete more than one password at once

        :param id_list: Is a list with the ID's of the passwords

        :type id_list: list

        """
        with self.connection:
            for i in id_list:
                self.connection.execute(data.DELETE_MANY_PASSWORDS, (i,))
