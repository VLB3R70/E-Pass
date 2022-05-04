from cryptography.fernet import Fernet

from .data import Data as data


class Encryptor:
    def keyGenerator(self):
        if not (self.keyCheck()):
            key = Fernet.generate_key()
            with open(data.KEY_FILE_PATH, 'wb') as keyFile:
                keyFile.write(key)

    def keyCheck(self):
        try:
            if open(data.KEY_FILE_PATH, 'rb').read():
                return True
        except FileNotFoundError:
            return False

    def loadKey(self):
        return open(data.KEY_FILE_PATH, 'rb').read()

    def encrypt(self, password):
        self.keyGenerator()
        key = self.loadKey()
        f = Fernet(key)
        encryptedPassword = f.encrypt(password.encode('utf-8'))
        return encryptedPassword.decode('utf-8')


class Decryptor:
    def loadKey(self):
        return open(data.KEY_FILE_PATH, 'rb').read()

    def decrypt(self, password):
        key = self.loadKey()
        f = Fernet(key)
        decryptedPassword = f.decrypt(password.encode('utf-8'))
        return decryptedPassword.decode("utf-8")
