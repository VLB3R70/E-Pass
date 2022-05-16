from tkinter import *
from GUI.LoginFrame import LoginFrame


def manager():
    root = Tk()
    login_frame = LoginFrame(root)
    login_frame.mainloop()


if __name__ == "__main__":
    manager()
