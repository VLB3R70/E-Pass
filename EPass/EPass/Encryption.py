from cryptography.fernet import Fernet


class Encryptor:
    def keyGenerator(self):
        if not (self.keyCheck()):
            key = Fernet.generate_key()
            with open("e-pass.key", "wb") as keyFile:
                keyFile.write(key)

    def keyCheck(self):
        try:
            if open("e-pass.key", "rb").read():
                return True
        except FileNotFoundError:
            return False

    def loadKey(self):
        return open("e-pass.key", "rb").read()

    def encrypt(self, password):
        self.keyGenerator()
        key = self.loadKey()
        f = Fernet(key)
        encryptedPassword = f.encrypt(password.encode("utf-8"))
        return encryptedPassword


class Decryptor:
    def loadKey(self):
        return open("e-pass.key", "rb").read()

    def decrypt(self, password):
        key = self.loadKey()
        f = Fernet(key)
        decryptedPassword = f.decrypt(password)
        return decryptedPassword.decode("utf-8")
