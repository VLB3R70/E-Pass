from cryptography.fernet import Fernet


class Encryptor:

    def keyGenerator(self):
        if not (self.keyCheck()):
            key = Fernet.generate_key()
            with open('private_key', 'wb') as keyFile:
                keyFile.write(key)

    def keyCheck(self):
        try:
            if open('private_key', 'rb').read():
                return True
        except FileNotFoundError:
            return False

    def loadKey(self):
        return open('private_key', 'rb').read()

    def encrypt(self, password):
        key = self.loadKey()
        f = Fernet(key)
        encryptedPassword = f.encrypt(password)
        return encryptedPassword