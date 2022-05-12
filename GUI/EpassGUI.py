from tkinter import *

from API.DAODatabase import DAO
from Frames.LoginFrame import LoginFrame

dao = DAO()


def manager():
    root = Tk()
    loginFrame = LoginFrame(root)
    loginFrame.mainloop()


if __name__ == '__main__':
    manager()

# if database is empty    ->  show registerFrame   else     ->  show loginFrame
