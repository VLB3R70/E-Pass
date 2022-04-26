import sqlite3

from .Encryption import Encryptor, Decryptor
from .data import Data

data = Data()


class DAO:
    encryptor = Encryptor()
    decryptor = Decryptor()

    def __init__(self):
        self.connection = sqlite3.connect(data.DATABASE_PATH)
        self.setupDataBase()
        
    def checkDataBase(self):
        with self.connection:
            isEmpty = self.connection.execute(data.SQL_COUNT).fetchall()
            
            if len(isEmpty) == 0:
                return True
            else:
                return False

    def setupDataBase(self):
        with self.connection:
            self.connection.executescript(data.SQL_START)

    def resetDataBase(self):
        with self.connection:
            self.connection.executescript(data.SQL_RESET)
            self.setupDataBase()

    def saveMasterPassword(self, masterPassword, email):
        encryptedPass = self.encryptor.encrypt(password=masterPassword)

        with self.connection:
            self.connection.execute(data.INSERT_MASTER_PASSWORD, (encryptedPass, email))

    def getMasterPassword(self):
        with self.connection:
            result = self.connection.execute(data.SELECT_MASTER_PASSWORD).fetchone()
            decryptedPassword = self.decryptor.decrypt(password=result[0])
        return decryptedPassword

    def updateMasterPassword(self, newPassword):
        with self.connection:
            encryptedPassword = self.encryptor.encrypt(newPassword)
            self.connection.execute(data.UPDATE_MASTER_PASSWORD, (encryptedPassword,))

    ########################################################################################

    def saveUserData(self, siteName, userName, password):
        encryptedPassword = self.encryptor.encrypt(password=password)
        with self.connection:
            self.connection.execute(data.INSERT_USER_DATA, (siteName, userName, encryptedPassword))

    def getUserData(self):
        with self.connection:
            userData = self.connection.execute(data.SELECT_USER_DATA).fetchall()
        return userData

    def getUserPassword(self, ID):
        with self.connection:
            userPassword = self.connection.execute(data.SELECT_USER_PASSWORD, (ID,)).fetchone()
            decryptedPassword = self.decryptor.decrypt(password=userPassword[0])

        return decryptedPassword

    def getUserName(self, ID):
        with self.connection:
            userName = self.connection.execute(data.SELECT_USER_NAME, (ID,)).fetchone()

        return userName[0]

    def updateUsername(self, ID, newUserName):
        with self.connection:
            self.connection.execute(data.UPDATE_USER_NAME, (newUserName, ID))

    def updateUserPassword(self, ID, newPassword):
        with self.connection:
            encryptedPassword = self.encryptor.encrypt(newPassword)
            self.connection.execute(data.UPDATE_USER_PASSWORD, (encryptedPassword, ID))

    def deleteOnePassword(self, ID):
        with self.connection:
            self.connection.execute(data.DELETE_ONE_PASSWORD, (ID,))

    def deleteManyPasswords(self, IDList):
        with self.connection:
            for i in IDList:
                self.connection.execute(data.DELETE_MANY_PASSWORDS, (i,))
