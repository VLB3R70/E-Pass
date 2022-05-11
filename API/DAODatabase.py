import os
import sqlite3

from .Encryption import Encryptor, Decryptor
from .data import Data

data = Data()

databaseCreated = True


class DAO:
    encryptor = Encryptor()
    decryptor = Decryptor()

    def __init__(self):
        try:
            self.connection = sqlite3.connect(data.DATABASE_PATH, check_same_thread=False)
            self.setupDataBase()
        except sqlite3.OperationalError:
            os.mkdir(data.DATA_DIRECTORY)
            open(data.DATABASE_PATH, 'w')

    def databaseEmpty(self):
        with self.connection:
            notEmpty = self.connection.execute(data.USER_COUNT).fetchone()

            if notEmpty:
                return False
            else:
                return True

    def setupDataBase(self):
        with self.connection:
            self.connection.executescript(data.SQL_START)

    def resetDataBase(self):
        with self.connection:
            self.connection.executescript(data.SQL_RESET)
            self.setupDataBase()

    def newUser(self, username, masterPassword, email):
        encryptedPass = self.encryptor.encrypt(password=masterPassword)

        with self.connection:
            self.connection.execute(data.INSERT_NEW_USER, (username, encryptedPass, email))

    def getUsers(self):
        with self.connection:
            users = self.connection.execute(data.USER_COUNT).fetchall()
            return users

    def getUserId(self, username):
        with self.connection:
            id = self.connection.execute(data.SELECT_USER_ID, (username,)).fetchone()

        return id[0]

    def getMasterPassword(self, user):
        with self.connection:
            result = self.connection.execute(data.SELECT_USER_MASTER_PASSWORD, (user,)).fetchone()
            decryptedPassword = self.decryptor.decrypt(password=result[0])
        return decryptedPassword

    def updateMasterPassword(self, newPassword, user):
        with self.connection:
            encryptedPassword = self.encryptor.encrypt(newPassword)
            self.connection.execute(data.UPDATE_MASTER_PASSWORD, (encryptedPassword, user))

    ########################################################################################

    def saveUserData(self, id, user_id, siteName, userName, password):
        encryptedPassword = self.encryptor.encrypt(password=password)
        with self.connection:
            self.connection.execute(data.INSERT_USER_DATA, (id, user_id, userName, siteName, encryptedPassword))

    def getUserData(self, user_id):
        with self.connection:
            userData = self.connection.execute(data.SELECT_USER_DATA, (user_id,)).fetchall()
        return userData

    def getUserPassword(self, id):
        with self.connection:
            userPassword = self.connection.execute(data.SELECT_USER_PASSWORD, (id,)).fetchone()
            decryptedPassword = self.decryptor.decrypt(password=userPassword[0])

        return decryptedPassword

    def getNumPasswords(self, user_id):
        with self.connection:
            num_passwords = self.connection.execute(data.SELECT_COUNT_PASSWORDS, (user_id,)).fetchone()

        return num_passwords[0]

    def getUserName(self, id):
        with self.connection:
            userName = self.connection.execute(data.SELECT_USER_NAME, (id,)).fetchone()

        return userName[0]

    def updateSitename(self, id, newSitename):
        with self.connection:
            self.connection.execute(data.UPDATE_USER_SITENAME, (newSitename, id))

    def updateUsername(self, id, newUserName):
        with self.connection:
            self.connection.execute(data.UPDATE_USER_NAME, (newUserName, id))

    def updateUserPassword(self, id, newPassword):
        with self.connection:
            encryptedPassword = self.encryptor.encrypt(newPassword)
            self.connection.execute(data.UPDATE_USER_PASSWORD, (encryptedPassword, id))

    def deleteOnePassword(self, id):
        with self.connection:
            self.connection.execute(data.DELETE_ONE_PASSWORD, (id,))

    def deleteManyPasswords(self, IDList):
        with self.connection:
            for i in IDList:
                self.connection.execute(data.DELETE_MANY_PASSWORDS, (i,))
