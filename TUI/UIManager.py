from rich import print as nicePrint
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table


# from EPass.DAODatabase import DAO

def mainMenu():

    optionMenu = createMainMenu()
    nicePrint(optionMenu)

    while True:
        selection = Prompt.ask("[magenta]Enter one of the options given")

        if selection == '0':
            nicePrint(optionMenu)
        elif selection == '1':
            # getUserData()
            nicePrint(createUserDataMenu())
        elif selection == '2':
            siteName = Prompt.ask("[magenta]Enter the site name")
            # getUserPassword(siteName=siteName)
            # copy the password to the clipboard
            nicePrint("[green]Password succesfully copied to the clipboard")
        elif selection == '3':
            newSiteName = Prompt.ask("Enter the site name", default="")
            newUserName = Prompt.ask("Enter your username of the site given", default="")
            newPassword = Prompt.ask("Enter the password of te site given", default="",password=True)

            # saveUserData(siteName=newSiteName, userName=newUserName, password=newPassword)
            nicePrint("[green]Succesfully added a new entry to the database!")
        elif selection == 'exit':
            break


def login():
    logo = """[bold][magenta]________         ________      
|   ____|        |   __  |     
|   |__    ___   |  |__| |  __ _      ____   ____
|   ___|  |___|  |  _____| / _` |    / __/  / __/
|   |___         |  |      |(_| |  __\ \  __\ \ 
|_______|        |__|      \__,_| |____/ |____/"""
    description = "\n\n[bold][blue]Welcome to a fast and smart password manager for the linux terminal lovers.😘"

    console = Console()
    # dao = DAO()

    nicePrint(logo + description)
    election = Prompt.ask(prompt='1. Login with master password. \n2. Create a new user\n', choices=['1', '2'])

    if election == '1':
        masterPassword = Prompt.ask(prompt='[magenta]Enter the master password', default="", password=True)

        if masterPassword == 'Alberto2002':
            nicePrint("[green]Succesful login!")
            mainMenu()
        else:
            nicePrint("[bold][red]Wrong password![yellow]Nice try[/yellow] 😉")
    elif election == '2':
        securityChoice = Prompt.ask(
            "[bold][yellow]WARNING\n[red]If you have a previous user with a master password all the data will be deleted. Are you sure you want to create a new one?",
            choices=['y', 'n'])

        if securityChoice == 'y':
            newMasterPassword = Prompt.ask(prompt="Introduce the new master password", default="", password=True)
            console.log("[bold][italic][red]New master password created and all previous data deleted.")

def createUserDataMenu():
    menu = Table(show_lines=True)
    menu.add_column("Site name")
    menu.add_column("User name")

    return menu

def createMainMenu():
    menu = Table(show_lines=True)
    menu.add_column("Selection number")
    menu.add_column("Description")
    menu.add_row('0','Show menu')
    menu.add_row('1.', 'List user data')
    menu.add_row('2', 'Select a password')
    menu.add_row('3', 'Add new entry')
    menu.add_row('4', 'Update password')
    menu.add_row('5', 'Update user name')
    menu.add_row('6', '[bold][red]Delete an entry')
    menu.add_row('exit','[yellow]Exit')

    return menu

login()
