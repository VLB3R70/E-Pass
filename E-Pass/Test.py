from DAODatabase import DAO

d = DAO()

d.createMasterPassTable()
d.createUserDataTable()

#d.saveMasterPassword("Alberto2002")
#print(d.getMasterPassword())
