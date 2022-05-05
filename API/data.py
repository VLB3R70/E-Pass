import os
from pathlib import Path


class Data:
    DATA_DIRECTORY = os.path.join(Path.home(), '.EPass/')

    KEY_FILE_NAME = '.epass.key'
    KEY_FILE_PATH = os.path.join(DATA_DIRECTORY, KEY_FILE_NAME)

    DATABASE_PATH = os.path.join(DATA_DIRECTORY, ".epass.db")

    SQL_COUNT = 'SELECT Master_Password FROM MasterPassword'

    SQL_START = """
            CREATE TABLE IF NOT EXISTS MasterPassword(
            Master_Password TEXT, 
            EMail VARCHAR(50));
    
            CREATE TABLE IF NOT EXISTS UserData(
            ID INTEGER primary key AUTOINCREMENT , 
            Site_name VARCHAR(100), 
            Username VARCHAR(50), 
            Password TEXT);
            """

    SQL_RESET = """
            DROP TABLE IF EXISTS MasterPassword;
            DROP TABLE IF EXISTS UserData;
            """

    INSERT_MASTER_PASSWORD = 'INSERT INTO MasterPassword(Master_Password, EMail)' \
                             'VALUES(?,?)'

    SELECT_MASTER_PASSWORD = 'SELECT Master_Password FROM MasterPassword'

    UPDATE_MASTER_PASSWORD = 'UPDATE MasterPassword SET Master_Password=?'

    INSERT_USER_DATA = 'INSERT INTO UserData(Site_name, Username, Password)' \
                       'VALUES (?,?,?)'

    SELECT_USER_DATA = 'SELECT * FROM UserData'

    SELECT_USER_PASSWORD = 'SELECT Password FROM UserData WHERE ID LIKE ?'

    SELECT_USER_NAME = 'SELECT Username FROM UserData WHERE ID LIKE ?'

    UPDATE_USER_NAME = 'UPDATE UserData SET Username = ? WHERE ID = ?'

    UPDATE_USER_PASSWORD = 'UPDATE UserData SET Password=? WHERE ID=?'

    UPDATE_USER_SITENAME = 'UPDATE UserData SET Site_name=? WHERE ID=?'

    DELETE_ONE_PASSWORD = 'DELETE FROM UserData WHERE ID=?'

    DELETE_MANY_PASSWORDS = 'DELETE FROM UserData WHERE ID=?'
