import os
import sqlite3
from pathlib import Path

from .Encryption import Encryptor, Decryptor


class DAO:
    DATABASE_NAME = os.path.join(Path.home(), ".epass.db")

    encryptor = Encryptor()
    decryptor = Decryptor()

    def __init__(self):
        self.connection = sqlite3.connect(self.DATABASE_NAME)
        self.setupDataBase()

    def setupDataBase(self):
        SQLStart = """
        CREATE TABLE IF NOT EXISTS MasterPassword(Master_Password TEXT, EMail VARCHAR(50));
        CREATE TABLE IF NOT EXISTS UserData(ID INTEGER primary key AUTOINCREMENT , Site_name VARCHAR(100), Username VARCHAR(50), Password TEXT);
        """

        with self.connection:
            self.connection.executescript(SQLStart)

    def resetDataBase(self):
        SQLReset = """
        DROP TABLE IF EXISTS MasterPassword;
        DROP TABLE IF EXISTS UserData;
        CREATE TABLE IF NOT EXISTS MasterPassword(Master_Password TEXT, EMail VARCHAR(50));
        CREATE TABLE IF NOT EXISTS UserData(ID INTEGER primary key AUTOINCREMENT , Site_name VARCHAR(100), Username VARCHAR(50), Password TEXT);
        """

        with self.connection:
            self.connection.executescript(SQLReset)

    def saveMasterPassword(self, masterPassword, email):
        encryptedPass = self.encryptor.encrypt(password=masterPassword)
        insertMasterPassword = 'INSERT INTO MasterPassword(Master_Password, EMail)' \
                               'VALUES(?,?)'

        with self.connection:
            self.connection.execute(insertMasterPassword, (encryptedPass, email))

    def getMasterPassword(self):
        selectMasterPassword = 'SELECT Master_Password FROM MasterPassword'

        with self.connection:
            result = self.connection.execute(selectMasterPassword).fetchone()
            decryptedPassword = self.decryptor.decrypt(password=result[0])
        return decryptedPassword

    def updateMasterPassword(self, newPassword):
        updateMasterPassword = 'UPDATE MasterPassword SET Master_Password=?'

        with self.connection:
            encryptedPassword = self.encryptor.encrypt(newPassword)
            self.connection.execute(updateMasterPassword, (encryptedPassword,))

    ########################################################################################

    def saveUserData(self, siteName, userName, password):
        encryptedPassword = self.encryptor.encrypt(password=password)
        insertUserData = 'INSERT INTO UserData(Site_name, Username, Password)' \
                         'VALUES (?,?,?)'

        with self.connection:
            self.connection.execute(insertUserData, (siteName, userName, encryptedPassword))

    def getUserData(self):
        selectUserData = 'SELECT * FROM UserData'
        with self.connection:
            userData = self.connection.execute(selectUserData).fetchall()
        return userData

    def getUserPassword(self, ID):
        selectUserPassword = 'SELECT Password FROM UserData WHERE ID LIKE ?'

        with self.connection:
            userPassword = self.connection.execute(selectUserPassword, (ID,)).fetchone()
            decryptedPassword = self.decryptor.decrypt(password=userPassword[0])

        return decryptedPassword

    def getUserName(self, ID):
        selectUserName = 'SELECT Username FROM UserData WHERE ID LIKE ?'

        with self.connection:
            userName = self.connection.execute(selectUserName, (ID,)).fetchone()

        return userName[0]

    def updateUsername(self, ID, newUserName):
        updateUserName = 'UPDATE UserData SET Username = ? WHERE ID = ?'

        with self.connection:
            self.connection.execute(updateUserName, (newUserName, ID))

    def updateUserPassword(self, ID, newPassword):
        updateUserPassword = 'UPDATE UserData SET Password=? WHERE ID=?'

        with self.connection:
            encryptedPassword = self.encryptor.encrypt(newPassword)
            self.connection.execute(updateUserPassword, (encryptedPassword, ID))

    def deleteOnePassword(self, ID):
        deleteOnePassword = 'DELETE FROM UserData WHERE ID=?'

        with self.connection:
            self.connection.execute(deleteOnePassword, (ID,))

    def deleteManyPasswords(self, IDList):
        deleteManyPasswords = 'DELETE FROM UserData WHERE ID=?'

        with self.connection:
            for i in IDList:
                self.connection.execute(deleteManyPasswords, (i,))

