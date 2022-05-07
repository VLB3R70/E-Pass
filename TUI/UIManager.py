from rich import print as nicePrint
from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich.table import Table

from API.DAODatabase import DAO
from .TUIHelp import HELP
import signal
import pyperclip as pc

dao = DAO()

USER = ''


def handler(signum, frame):
    nicePrint("\n[magenta][bold]Goodbye! 👋")
    exit(1)


def login():
    global USER
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
                    nicePrint("[green]Succesful login!")
                    mainMenu()
                    login = False
                else:
                    nicePrint("[bold][red]Wrong password![yellow]Nice try[/yellow] 😉")
        elif election == "2":
            # securityChoice = Prompt.ask(
            #     "[bold][yellow]WARNING\n[red]If you have a previous user with a master
            #     password all the data will be deleted. Are you sure you want to create a new one?",
            #     choices=["y", "n"],
            # )
            dao.resetDataBase()
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
    global USER
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

            dao.saveUserData(
                user=USER, siteName=newSiteName, userName=newUserName, password=newPassword
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
    markdown = Markdown(HELP)
    nicePrint(markdown)
    pass


def createUserDataMenu():
    menu = Table(show_lines=True)
    menu.add_column("ID", style="orange1")
    menu.add_column("Site name", style="purple3")
    menu.add_column("User name", style="green1")
    menu.add_column("Password")
    for row in dao.getUserData(user=USER):
        menu.add_row(str(row[0]), row[2], row[3], "*******")

    return menu


def createMainMenu():
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
