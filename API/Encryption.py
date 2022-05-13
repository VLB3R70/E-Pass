"""
.. module:: Encryption
    :synopsis:

.. moduleauthor:: Alberto Jiménez <https://github.com/VLB3R70>

This module has two classes, one for password encryption and the other one for the decryption. This module uses the `cryptography <https://pypi.org/project/cryptography/>`_ package for the encryption.
"""
from cryptography.fernet import Fernet

from .data import Data as data


class Encryptor:
    """
    .. class:: Encryptor

    The `Encryptor` class is used to encrypt the passwords before insert them in the database with a generated key.
    """

    def keyGenerator(self):
        """
        This method generates a file with the necessary key to encrypt and decrypt the passwords if there is non.
        The name of the file and it's directory is designated by the .. module::data module.
        """
        if not (self.keyCheck()):
            key = Fernet.generate_key()
            with open(data.KEY_FILE_PATH, 'wb') as keyFile:
                keyFile.write(key)

    def keyCheck(self):
        """
        This method checks if the generated key exists or not.

        :return: It returns `True` or `False`

        :rtype: bool
        """
        try:
            if open(data.KEY_FILE_PATH, 'rb').read():
                return True
        except FileNotFoundError:
            return False

    def loadKey(self):
        """
        This method reads the key in the file returns its value.

        :return: It returns the value of that key

        :rtype: str
        """
        return open(data.KEY_FILE_PATH, 'rb').read()

    def encrypt(self, password):
        """
        This is the main method of the class. It generates a key if there is non making a call to
        :py:func:`keyGenerator()`. Then, it reads the value of the key and generates a `Fernet` object
        which is used to encrypt a string with the generated key.

        :param password: It is the password that the user wants to be encrypted

        :return: It returns the value of the encrypted password

        :rtype: str
        """
        self.keyGenerator()
        key = self.loadKey()
        f = Fernet(key)
        encryptedPassword = f.encrypt(password.encode('utf-8'))
        return encryptedPassword.decode('utf-8')


class Decryptor:
    """
    .. class:: Decryptor

    This class is used to decrypt the passwords that are stored in the database. It uses the key that the
    :py:class:`Encryptor` class generates.
    """

    def loadKey(self):
        """
        This method reads the value of the key file

        :return: It returns the value of the key

        :rtype: str
        """
        return open(data.KEY_FILE_PATH, 'rb').read()

    def decrypt(self, password):
        """
        This method is used to decrypt the password stored in the database.
        It calls :py:func:`loadKey()` function to get the value of the key.
        Then, it generates a `Fernet` object which is used to decrypt the password given.

        :param password: It is the value of the password stored in the database

        :return: It returns the decrypted value of the password

        :rtype: str
        """
        key = self.loadKey()
        f = Fernet(key)
        decryptedPassword = f.decrypt(password.encode('utf-8'))
        return decryptedPassword.decode("utf-8")
