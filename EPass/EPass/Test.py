from DAODatabase import DAO

d = DAO()

d.createMasterPassTable()
d.createUserDataTable()

# d.saveMasterPassword('Alberto2002')
# print(d.getMasterPassword())

d.saveUserData(siteName='amazon.com',userName='vlb3r70',password='MiContraseñaDeAmazon')
d.saveUserData(siteName='minecraft.net',userName='vlb3r70',password='MiContraseñaDeMinecraft')
print(d.getUserName(siteName='amazon.com'))
print(d.getUserPassword(siteName='amazon.com'))
