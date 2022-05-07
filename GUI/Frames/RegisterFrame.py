import tkinter.messagebox as message
from tkinter import *

from API.DAODatabase import DAO

dao = DAO()


class RegisterFrame(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root

        self.userLabel = Label(self, text="Enter the new username:")
        self.userLabel.grid(column=0, row=1)
        self.masterPasswordLabel = Label(self, text="Enter the new master password:")
        self.masterPasswordLabel.grid(column=0, row=2)
        self.emailLabel = Label(self, text="Enter your e-mail:")
        self.emailLabel.grid(column=0, row=3)

        self.usernameEntry = Entry(self)
        self.usernameEntry.grid(column=1, row=1)
        self.masterPasswordEntry = Entry(self, show='*')
        self.masterPasswordEntry.grid(column=1, row=2)
        self.masterPasswordEntry.bind("<Return>", lambda event: self.registerUser())
        self.emailEntry = Entry(self)
        self.emailEntry.grid(column=1, row=3)
        self.emailEntry.bind("<Return>", lambda event: self.registerUser())

        self.registerButton = Button(self, text="Register", bg="#4CAF50", activebackground="#81c784",
                                     command=lambda: self.registerUser())
        self.registerButton.grid(column=0, row=4, columnspan=2, rowspan=2, ipadx=30, pady=40)

        self.root.title("Registration")
        self.root.configure(padx=60, pady=20)
        self.root.minsize(300, 200)
        self.root.maxsize(500, 200)
        self.pack()

    def registerUser(self):
        if self.emptyEntries():
            message.showwarning("Empty values", "There are empty entries, please enter the necessary data")
        else:
            ask = message.askyesno("Caution",
                                   "Are you sure you want to create a new user?")
            if ask:
                dao.newUser(self.usernameEntry.get(), self.masterPasswordEntry.get(), self.emailEntry.get())
                info = message.showinfo("Success", "User created successfully")
                self.root.destroy()
            else:
                pass

    def emptyEntries(self):
        if self.masterPasswordEntry.get() == '' or self.emailEntry.get() == '':
            return True
        else:
            return False
