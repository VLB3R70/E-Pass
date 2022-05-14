"""
.. module:: UIManager
    :synopsis:

This module implements the necessary functions to make a functional Terminal User Interface application. This modules uses the `rich <https://pypi.org/project/rich/>`_ package to make a prettier TUI.

.. moduleauthor::
    `Alberto Jiménez <https://github.com/VLB3R70>`_
"""
import signal

import pyperclip as pc
from rich import print as nicePrint
from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich.table import Table
from API.DAODatabase import DAO
from .TUIHelp import HELP

dao = DAO()

USER = ''
USER_ID = 0


def handler(signum, frame):
    nicePrint("\n[magenta][bold]Goodbye! 👋")
    exit(1)


def login():
    """
    This function is the first one to run. It shows the app logo and three decisions.

    * login
    * register
    * remember password

    The user has to select one of them by typing the number given. This function responds if the user types ``Ctrl+C``
    and leaves the app without throwing an exception. This function implements an infinite loop and asks the user for
    the three options. If the user fails during the login it asks about the three options again until enters the data
    successfully.
    When the user finish to register his account the prompt asks once again to select one of the three options.

    1. If the user decides to log in, the prompt ask for the username and the passwords. If they are correct it shows
    the main menu, if not, it asks once again for the password.

    2. If the user decides to register a new one, the prompt ask for the new username, his master password and his email.
    Before that the prompt automatically redirects to the log in prompt again.

    .. note:: The `remember password` function is under development but in resume; this function will email the user with the value of the password.

    """
    global USER
    global USER_ID
    login = True
    logo = """[bold][magenta]________         ________      
|   ____|        |   __  |     
|   |__    ___   |  |__| |  __ _      ____   ____
|   ___|  |___|  |  _____| / _` |    / __/  / __/
|   |___         |  |      |(_| |  __\ \  __\ \ 
|_______|        |__|      \__,_| |____/ |____/"""
    description = "\n\n[bold][blue]Welcome to a fast and smart password manager for the linux terminal lovers.\n\n\n\n"
    signal.signal(signal.SIGINT, handler)
    console = Console()

    nicePrint(logo + description)
    if dao.databaseEmpty():
        nicePrint("[red]There is no user in this database. Please create a new one.\n\n")

    while login:
        election = Prompt.ask(
            prompt="1. Login. \n2. Create a new user\n3. Remember password",
            choices=["1", "2", "3"],
        )
        if election == "1":
            username = Prompt.ask(
                prompt="[magenta]Enter your username:", default=""
            )
            masterPassword = Prompt.ask(
                prompt="[magenta]Enter the master password:", default="", password=True
            )
            USER = username
            for i in dao.getUsers():
                if username in i and masterPassword == dao.getMasterPassword(user=USER):
                    USER_ID = dao.getUserId(username=USER)
                    nicePrint("[green]Succesful login!")
                    mainMenu()
                    login = False
                else:
                    nicePrint("[bold][red]Wrong password![yellow]Nice try[/yellow] 😉")
        elif election == "2":
            newUsername = Prompt.ask(prompt="[cyan]Enter the username:", default="")
            newMasterPassword = Prompt.ask(
                prompt="[cyan]Enter the new master password",
                default="",
                password=True,
            )
            newEmail = Prompt.ask("[cyan]Enter your email", default="")
            dao.newUser(username=newUsername, masterPassword=newMasterPassword, email=newEmail)
            console.log(
                "[bold][italic][red]New master password created and all previous data deleted."
            )
        elif election == "3":
            # send an email with the password
            pass


def mainMenu():
    """
    This function shows a main menu with six different options that the user can select.
    This function uses an infinite loop and the user selects one of the options given; to exit the
    loop the user has to enter ``Crtl+C``.
    The six options for now are this:

    0. `Show menu` : this option shows again the menu with the different options

    1. `List user data` : this option shows all the data of the user logged

    2. `Select a password` : this options ask for the ID of the password, and then it copies the password value to the clipboard

    3. `Add a new entry` : this option ask the user to enter all the necessary data for the passwords such as the username, the site name and the password

    4. `Update password` : this option ask the user to enter the ID of the password that wants to update, and then it asks for the new password

    5. `Update username` : this option ask the user the ID of the username that wants to update, then it asks for the new username

    6. `Delete an entry` :  this option ask the user the ID of the password that wants to delete

    `exit` : this option exits the infinite loop and the app

    """
    global USER_ID
    optionMenu = createMainMenu()
    nicePrint(optionMenu)
    signal.signal(signal.SIGINT, handler)

    while True:
        selection = Prompt.ask("[magenta]Enter one of the options given")

        if selection == "0":
            nicePrint(optionMenu)
        elif selection == "1":
            nicePrint(createUserDataMenu())
        elif selection == "2":
            id = Prompt.ask("[cyan]Enter the ID of the password you want to get")
            password = dao.getUserPassword(id=id)
            pc.copy(password)
            nicePrint("[green]Password succesfully copied to the clipboard")
        elif selection == "3":
            newSiteName = Prompt.ask("[cyan]Enter the site name", default="")
            newUserName = Prompt.ask(
                "[cyan]Enter your username of the site given", default=""
            )
            newPassword = Prompt.ask(
                "[cyan]Enter the password of te site given", default="", password=True
            )
            num_passwords = dao.getNumPasswords(USER_ID)
            dao.saveUserData(
                id=str((num_passwords + 1)), user_id=str(USER_ID), siteName=newSiteName, userName=newUserName,
                password=newPassword
            )
            nicePrint("[green]Succesfully added a new entry to the database!")
        elif selection == "4":
            id = Prompt.ask("[cyan]Enter the ID of the password you want to update")
            newPassword = Prompt.ask(
                "[cyan]Enter the new password", default="", password=True
            )

            dao.updateUserPassword(id=id, newPassword=newPassword)
            nicePrint("[green]Password succesfully updated!")
        elif selection == "5":
            id = Prompt.ask("[cyan]Enter the ID of the username yo want to update")
            newUserName = Prompt.ask("[cyan]Enter the new username")

            dao.updateUsername(id=id, newUserName=newUserName)
            nicePrint("[green]Username succesfully updated!")
        elif selection == '6':
            deleteSelection = Prompt.ask("[orange]Do you want to delete one entry or more", default="",
                                         choices=['one', 'more'])

            if deleteSelection == 'one':
                id = Prompt.ask("[cyan]Enter the ID of the password")
                dao.deleteOnePassword(id=id)
                nicePrint("[green]Password successfully deleted")
            elif deleteSelection == "more":
                id = Prompt.ask(
                    "[cyan]Enter the ID's of the passwords you want to delete.\n"
                    "[yellow]To enter more than one ID just simply enter the number and leave a blank space"
                )
                IDList = list(id.replace(' ', ''))
                dao.deleteManyPasswords(IDList=IDList)
                nicePrint("[green]Succesfully deleted all passwords!")

        elif selection == "exit":
            nicePrint("[magenta][bold]Goodbye! 👋")
            break


def TUIHelp():
    """
    This function just simply shows a simple help for the user. It prints all the data from .. module:: TUI.TUIHelp
    and then it exists the app
    """
    markdown = Markdown(HELP)
    nicePrint(markdown)
    pass


def createUserDataMenu():
    """
    This function prints a table with all the data of the user. This function is called by the :py:func:`mainMenu()`
    when the user selects the option: 1. `List user data`

    :return: It returns a table with all the data

    :rtype: ``rich.table.Table``
    """
    menu = Table(show_lines=True)
    menu.add_column("ID", style="orange1")
    menu.add_column("Site name", style="purple3")
    menu.add_column("User name", style="green1")
    menu.add_column("Password")
    for row in dao.getUserData(user_id=USER_ID):
        menu.add_row(str(row[0]), row[2], row[3], "*******")

    return menu


def createMainMenu():
    """
    This function prints a table with all the options to the user. This function is called by the :py:func:`mainMenu()`

    :return: It returns the table with the six options

    :rtype: ``rich.table.Table``
    """
    menu = Table(show_lines=True)
    menu.add_column("Selection number")
    menu.add_column("Description")
    menu.add_row("0", "Show menu")
    menu.add_row("1.", "List user data")
    menu.add_row("2", "Select a password")
    menu.add_row("3", "Add new entry")
    menu.add_row("4", "Update password")
    menu.add_row("5", "Update username")
    menu.add_row("6", "[bold][red]Delete an entry")
    menu.add_row("exit", "[yellow]Exit")

    return menu
