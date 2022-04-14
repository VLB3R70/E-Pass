from cryptography.fernet import Fernet


class Decryptor:

    def loadKey(self):
        return open('private_key', 'rb').read()

    def decrypt(self, password):
        key = self.loadKey()
        f = Fernet(key)
        decryptedPassword = f.decrypt(password)
        return decryptedPassword