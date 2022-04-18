import sqlite3
from pathlib import Path

from Encryption import Encryptor, Decryptor


class DAO:
    encryptor = Encryptor()
    decryptor = Decryptor()

    databasePath = str(Path.home())
    databaseName = '.e-pass.db'

    def __init__(self):
        self.connection = sqlite3.connect(self.databaseName)

    def createMasterPassTable(self):
        SQLMasterTable = \
            'CREATE TABLE IF NOT EXISTS MasterPassword(Master_Password TEXT)'

        with self.connection:
            self.connection.execute(SQLMasterTable)

    def saveMasterPassword(self, masterPassword):
        encryptedPass = self.encryptor.encrypt(password=masterPassword)
        insertMasterPassword = 'INSERT INTO MasterPassword(Master_Password)' \
                               'VALUES(?)'

        with self.connection:
            self.connection.execute(insertMasterPassword, (encryptedPass,))

    def getMasterPassword(self):
        selectMasterPassword = 'SELECT * FROM MasterPassword'

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

    def createUserDataTable(self):
        SQLUserData = \
            'CREATE TABLE IF NOT EXISTS UserData(Site_name VARCHAR(100), Username VARCHAR(50), Password TEXT)'

        with self.connection:
            self.connection.execute(SQLUserData)

    def saveUserData(self, siteName, userName, password):
        encryptedPassword = self.encryptor.encrypt(password=password)
        insertUserData = 'INSERT INTO UserData(Site_name, Username, Password)' \
                         'VALUES (?,?,?)'

        with self.connection:
            self.connection.execute(insertUserData, (siteName, userName, encryptedPassword))

    def getUserPassword(self, siteName):
        selectUserPassword = 'SELECT Password FROM UserData WHERE Site_name LIKE ?'

        with self.connection:
            userPassword = self.connection.execute(selectUserPassword, (siteName,)).fetchone()
            decryptedPassword = self.decryptor.decrypt(password=userPassword[0])

        return decryptedPassword

    def getUserName(self, siteName):
        selectUserName = 'SELECT Username FROM UserData WHERE Site_name LIKE ?'

        with self.connection:
            userName = self.connection.execute(selectUserName, (siteName,)).fetchone()

        return userName[0]

    def updateUsername(self, siteName, newUserName):
        updateUserName = 'UPDATE UserData SET Username = ? WHERE Site_name = ?'

        with self.connection:
            self.connection.execute(updateUserName, (newUserName, siteName))

    def updateUserPassword(self, siteName, newPassword):
        updateUserPassword = 'UPDATE UserData SET Password=? WHERE Site_name=?'

        with self.connection:
            encryptedPassword = self.encryptor.encrypt(newPassword)
            self.connection.execute(updateUserPassword, (encryptedPassword, siteName))
