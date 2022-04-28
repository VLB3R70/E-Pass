from tkinter import *
import tkinter.messagebox as message

from EPass.API.DAODatabase import DAO
from .HomeFrame import HomeFrame

dao = DAO()
BUTTON_COLOR = "#4CAF50"


class LoginFrame(Frame):

    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.img = PhotoImage(file='Frames/img/candado.png')
        self.epassImage = Label(self, image=self.img)
        self.epassImage.grid(column=0, row=0, columnspan=2, pady=40)

        self.masterPasswordLabel = Label(self, text="Introduce the master password:")
        self.masterPasswordLabel.grid(column=0, row=1)
        self.masterPasswordEntry = Entry(self, show='*')
        self.masterPasswordEntry.grid(column=0, row=2)
        self.masterPasswordEntry.focus()

        self.accessButton = Button(self, text="Log in", bg=BUTTON_COLOR, command=lambda: self.checkPassword())
        self.accessButton.grid(column=0, row=3, columnspan=2, rowspan=2, ipadx=30, pady=40)

        self.root.title("Log in")
        self.root.minsize(500, 200)
        self.pack()

    def checkPassword(self):
        if self.masterPasswordEntry.get() == dao.getMasterPassword():
            self.root.destroy()
            root = Tk()
            homeFrame = HomeFrame(root)
            homeFrame.tkraise()
        else:
            message.showerror("Error", "Incorrect password. Please try again")

