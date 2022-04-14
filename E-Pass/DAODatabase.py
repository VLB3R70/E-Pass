import sqlite3

from Decryptor import Decryptor
from Encryptor import Encryptor


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
            self.connection.execute(insertMasterPassword, (encryptedPass))
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
            self.connection.execute(updateMasterPassword, (encryptedPassword))
        # self.connection.commit()

    def createUserDataTable(self):
        SQLUserData = \
            'CREATE TABLE IF NOT EXISTS UserData(Site_name VARCHAR(100), Username VARCHAR(50), Password TEXT)'

    def saveUserData(self):
        pass

    def getUserPassword(self):
        pass

    def updateUsername(self):
        pass

    def updateUserPassword(self):
        pass
