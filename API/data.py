import os
from pathlib import Path


class Data:
    DATA_DIRECTORY = os.path.join(Path.home(), 'EPass/')

    KEY_FILE_NAME = '.epass.key'
    KEY_FILE_PATH = os.path.join(DATA_DIRECTORY, KEY_FILE_NAME)

    DATABASE_PATH = os.path.join(DATA_DIRECTORY, "epass.db")

    USER_COUNT = 'SELECT name FROM User'

    SQL_START = '''CREATE TABLE IF NOT EXISTS [User] (
                    [id] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    [name] TEXT NOT NULL UNIQUE,
                    [master_password] TEXT NOT NULL,
                    [email] TEXT NOT NULL);

                    CREATE TABLE IF NOT EXISTS [Data] (
                    [id] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    [user_id] INTEGER NOT NULL,[site_name] TEXT NOT NULL,
                    [username] TEXT NOT NULL,[password] TEXT NOT NULL,
                    FOREIGN KEY([user_id]) REFERENCES [User]([id]) ON DELETE CASCADE ON UPDATE CASCADE);
                    '''

    SQL_RESET = """
            DROP TABLE IF EXISTS User;
            DROP TABLE IF EXISTS Data;
            """

    INSERT_NEW_USER = 'INSERT INTO User(name, master_password, email) VALUES(?, ?, ?);'

    SELECT_USER_MASTER_PASSWORD = 'SELECT master_password FROM User WHERE name = ?;'

    UPDATE_MASTER_PASSWORD = 'UPDATE User SET master_password = ? WHERE name = ?;'

    SELECT_USER_ID = 'SELECT id FROM User WHERE name=?'

    INSERT_USER_DATA = 'INSERT INTO Data (user_id,username,site_name, password) VALUES (?,?, ?, ?);'

    SELECT_USER_DATA = 'SELECT * FROM Data WHERE user_id = ?;'

    SELECT_USER_PASSWORD = 'SELECT password FROM Data WHERE id = ?;'

    SELECT_USER_NAME = 'SELECT username FROM Data WHERE id = ?;'

    UPDATE_USER_NAME = 'UPDATE Data SET username = ? WHERE id = ?;'

    UPDATE_USER_PASSWORD = 'UPDATE Data SET password = ? WHERE id = ?;'

    UPDATE_USER_SITENAME = 'UPDATE Data SET site_name = ? WHERE id = ?;'

    DELETE_ONE_PASSWORD = 'DELETE FROM Data WHERE id =?;'

    DELETE_MANY_PASSWORDS = 'DELETE FROM Data WHERE id =?;'
