import sqlite3

from .Decryptor import Decryptor
from .Encryptor import Encryptor


class DAO:
    encryptor = Encryptor
    decryptor = Decryptor

    def __int__(self):
        self.connection = sqlite3.connect("")

    def createMasterPassTable(self):
        SQLMasterTable = \
            'CREATE TABLE IF NOT EXISTS MasterPassword(Master_Password TEXT)'

        with self.connection:
            self.connection.execute(SQLMasterTable)
        # self.connection.commit()

    def saveMasterPassword(self, masterPassword):
        encryptedPass = self.encryptor.encrypt(masterPassword)
        insertMasterPassword = 'INSERT INTO MasterPassword(Master_Password)' \
                               'VALUES(?)'

        with self.connection:
            self.connection.execute(insertMasterPassword, (encryptedPass,))
        # self.connection.commit()

    def getMasterPassword(self):
        selectMasterPassword = 'SELECT * FROM MasterPassword'

        with self.connection:
            result = self.connection.execute(selectMasterPassword)
            # self.connection.commit()
            decryptedPassword = self.decryptor.decrypt(result)
        return decryptedPassword

    def updateMasterPassword(self, newPassword):
        updateMasterPassword = 'UPDATE MasterPassword SET Master_Password=?'

        with self.connection:
            encryptedPassword = self.encryptor.encrypt(newPassword)
            self.connection.execute(updateMasterPassword, (encryptedPassword,))
        # self.connection.commit()

    ########################################################################################

    def createUserDataTable(self):
        SQLUserData = \
            'CREATE TABLE IF NOT EXISTS UserData(Site_name VARCHAR(100), Username VARCHAR(50), Password TEXT)'

    def saveUserData(self, siteName, userName, password):
        encryptedPassword = self.encryptor.encrypt(password)
        insertUserData = 'INSERT INTO UserData(Site_name, Username, Password)' \
                         'VALUES (?,?,?)'

        with self.connection:
            self.connection.execute(insertUserData, (siteName, userName, encryptedPassword))

    def getUserPassword(self, siteName):
        selectUserPassword = 'SELECT Password FROM UserData WHERE Site_name LIKE ?'

        with self.connection:
            userPassword = self.connection.execute(selectUserPassword, (siteName,))
            decryptedPassword = self.decryptor.decrypt(userPassword)

        return decryptedPassword

    def getUserName(self, siteName):
        selectUserName = 'SELECT Username FROM UserData WHERE Site_name LIKE ?'

        with self.connection:
            userName = self.connection.execute(selectUserName, (siteName,))

        return userName

    def updateUsername(self, siteName, newUserName):
        updateUserName = 'UPDATE UserData SET Username = ? WHERE Site_name = ?'

        with self.connection:
            self.connection.execute(updateUserName, (newUserName, siteName))

    def updateUserPassword(self, siteName, newPassword):
        updateUserPassword = 'UPDATE UsreData SET Password=? WHERE Site_name=?'

        with self.connection:
            encryptedPassword = self.encryptor.encrypt(newPassword)
            self.connection.execute(updateUserPassword, (encryptedPassword, siteName))
