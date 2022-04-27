from tkinter import *
from tkinter.ttk import *
from EPass.API.DAODatabase import DAO
from LoginFrame import LoginFrame
dao = DAO()


def manager():
    root = Tk()
    loginFrame = LoginFrame(root)
    loginFrame.mainloop()

# if database is empty    ->  show registerFrame   else     ->  show loginFrame

manager()

