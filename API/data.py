import os
from pathlib import Path


class Data:
    DATA_DIRECTORY = os.path.join(Path.home(), '.EPass/')

    KEY_FILE_NAME = '.epass.key'
    KEY_FILE_PATH = os.path.join(DATA_DIRECTORY, KEY_FILE_NAME)

    DATABASE_PATH = os.path.join(DATA_DIRECTORY, ".epass.db")

    SQL_COUNT = 'SELECT Master_Password FROM MasterPassword'

    SQL_START = """
            CREATE TABLE IF NOT EXISTS Data (
            id        INTEGER PRIMARY KEY,
            site_name VARCHAR NOT NULL,
            username  VARCHAR NOT NULL,
            password  VARCHAR NOT NULL
            );

            CREATE TABLE User (
            id              INTEGER PRIMARY KEY CONSTRAINT fk_id REFERENCES User (id) 
            ON DELETE CASCADE ON UPDATE CASCADE,
            username        VARCHAR UNIQUE NOT NULL,
            master_password VARCHAR NOT NULL,
            email           VARCHAR);
            """

    SQL_RESET = """
            DROP TABLE IF EXISTS User;
            DROP TABLE IF EXISTS Data;
            """

    INSERT_NEW_USER = 'INSERT INTO User (username, master_password, email) VALUES (?, ?, ?);'

    SELECT_USER_MASTER_PASSWORD = 'SELECT master_password FROM User WHERE id = ?;'

    UPDATE_MASTER_PASSWORD = 'UPDATE User SET master_password = ? WHERE id = ?;'

    INSERT_USER_DATA = 'INSERT INTO Data (site_name, username, password) VALUES (?, ?, ?);'

    SELECT_USER_DATA = 'SELECT * FROM Data WHERE id = ?;'

    SELECT_USER_PASSWORD = 'SELECT password FROM Data WHERE id = ?;'

    SELECT_USER_NAME = 'SELECT username FROM Data WHERE id = ?;'

    UPDATE_USER_NAME = 'UPDATE Data SET username = ? WHERE id = ?;'

    UPDATE_USER_PASSWORD = 'UPDATE Data SET password = ? WHERE id = ?;'

    UPDATE_USER_SITENAME = 'UPDATE Data SET site_name = ? WHERE id = ?;'

    DELETE_ONE_PASSWORD = 'DELETE FROM Data WHERE id =?;'

    DELETE_MANY_PASSWORDS = 'DELETE FROM Data WHERE id =?;'
