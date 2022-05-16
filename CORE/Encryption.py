"""
.. module:: Encryption
    :synopsis:

.. moduleauthor:: Alberto Jiménez <https://github.com/VLB3R70>

This module uses the `cryptography <https://pypi.org/project/cryptography/>`_ package for the encryption. There are two
main methods :py:func:`encrypt` and :py:func:`decrypt`. These methods are the ones which encrypts and decrypts the
passwords from the database.
"""
from cryptography.fernet import Fernet

from .data import Data

data = Data()


def load_key():
    """
    This method reads the key in the file returns its value.

    :return: It returns the value of that key

    :rtype: str
    """
    return open(data.KEY_FILE_PATH, "rb").read()


def key_check():
    """
    This method checks if the generated key exists or not.

    :return: It returns `True` or `False`

    :rtype: bool
    """
    try:
        if open(data.KEY_FILE_PATH, "rb").read():
            return True
    except FileNotFoundError:
        return False


def key_generator():
    """
    This method generates a file with the necessary key to encrypt and decrypt the passwords if there is non.
    The name of the file and it's directory is designated by the :py:mod:`data` module.
    """
    if not (key_check()):
        key = Fernet.generate_key()
        with open(data.KEY_FILE_PATH, "wb") as keyFile:
            keyFile.write(key)


def encrypt(password):
    """
    This is the main method of the class. It generates a key if there is non making a call to
    :py:func:`keyGenerator()`. Then, it reads the value of the key and generates a `Fernet` object
    which is used to encrypt a string with the generated key.

    :param password: It is the password that the user wants to be encrypted

    :return: It returns the value of the encrypted password

    :rtype: str
    """
    key_generator()
    key = load_key()
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode("utf-8"))
    return encrypted_password.decode("utf-8")


def decrypt(password):
    """
    This method is used to decrypt the password stored in the database.
    It calls :py:func:`loadKey()` function to get the value of the key.
    Then, it generates a `Fernet` object which is used to decrypt the password given.

    :param password: It is the value of the password stored in the database

    :return: It returns the decrypted value of the password

    :rtype: str
    """
    key = load_key()
    f = Fernet(key)
    decrypted_password = f.decrypt(password.encode("utf-8"))
    return decrypted_password.decode("utf-8")
