HELP = """
# EPass TUI

This password manager it is developed in a TUI (Terminal User Interface)

## Login
The first *window* that appears is a simple *login*. You have three possible options:

1. Login with the master password
2. Create a new user
3. Remember password

- If the user selects the first option it ask for the master password of the
database; if the typed password is correct it redirects the user to the main menu, if not,
it asks again for the password. If the password is incorrect the program closes automatically.


- If the user selects the second option a new user will be created. If there are any previous data on the database
it will be **deleted** so if you have lost the master password it is recommended to use the third option instead.
When the user is going to create a new account EPass ask for a new master password and an e-mail. This data is needed
for the login.


- If the user selects the third option it will send and e-mail to the account registered in the database; if you
type a different e-mail nothing will happen.

##### IF YOU CREATE A NEW USER WITHOUT AN EMAIL ALL YOUR DATA WILL POSSIBLY BE LOST BECAUSE YOU WILL NOT HAVE ANY BACKUP METHOD.

## Main Menu

If the user have successfully login it will appear a *Main Menu*. This Main Menu it is composed by a table
that shows different options. A little prompt always ask for the next move of the user. There are six possible options:

1. List all data
2. Select a password
3. Add a new entry
4. Update a password
5. Update a user name
6. Delete an entry

- If the user selects the first option it will appear a little table with all the data of the DB. For security reasons
the table will only show the site name and the username.

- If the user selects the second option the prompt will ask for the site name and will copy in the clipboard that password.

- If the user selects the third option, the prompt will ask him to enter all the necessary data being these the site name, the username and his password.


"""
