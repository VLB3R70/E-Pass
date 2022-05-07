import os
from pathlib import Path


class Data:
    DATA_DIRECTORY = os.path.join(Path.home(), '.EPass/')

    KEY_FILE_NAME = '.epass.key'
    KEY_FILE_PATH = os.path.join(DATA_DIRECTORY, KEY_FILE_NAME)

    DATABASE_PATH = os.path.join(DATA_DIRECTORY, ".epass.sqlite")

    USER_COUNT = 'SELECT name FROM User'

    SQL_START = """
            CREATE TABLE IF NOT EXISTS User (
            name            VARCHAR (50)  NOT NULL
                                  PRIMARY KEY,
            master_password VARCHAR (100) NOT NULL,
            email           VARCHAR (100) 
            );
            CREATE TABLE IF NOT EXISTS Data (
            id        INTEGER       PRIMARY KEY,
            user      VARCHAR (50)  NOT NULL
                                    CONSTRAINT fk_user REFERENCES User (name) ON DELETE CASCADE
                                                                              ON UPDATE CASCADE,
            site_name VARCHAR (100) NOT NULL,
            username  VARCHAR (100) NOT NULL,
            password  VARCHAR (100) NOT NULL
            );
            """

    SQL_RESET = """
            DROP TABLE IF EXISTS User;
            DROP TABLE IF EXISTS Data;
            """

    INSERT_NEW_USER = 'INSERT INTO User (name, master_password, email) VALUES (?, ?, ?);'

    SELECT_USER_MASTER_PASSWORD = 'SELECT master_password FROM User WHERE name = ?;'

    UPDATE_MASTER_PASSWORD = 'UPDATE User SET master_password = ? WHERE name = ?;'

    INSERT_USER_DATA = 'INSERT INTO Data (user,username,site_name, password) VALUES (?,?, ?, ?);'

    SELECT_USER_DATA = 'SELECT * FROM Data WHERE user = ?;'

    SELECT_USER_PASSWORD = 'SELECT password FROM Data WHERE id = ?;'

    SELECT_USER_NAME = 'SELECT username FROM Data WHERE id = ?;'

    UPDATE_USER_NAME = 'UPDATE Data SET username = ? WHERE id = ?;'

    UPDATE_USER_PASSWORD = 'UPDATE Data SET password = ? WHERE id = ?;'

    UPDATE_USER_SITENAME = 'UPDATE Data SET site_name = ? WHERE id = ?;'

    DELETE_ONE_PASSWORD = 'DELETE FROM Data WHERE id =?;'

    DELETE_MANY_PASSWORDS = 'DELETE FROM Data WHERE id =?;'
