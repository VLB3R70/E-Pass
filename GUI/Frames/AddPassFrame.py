import tkinter.messagebox as message
from tkinter import *

from API.DAODatabase import DAO
dao = DAO()


class AddPassFrame(Toplevel):
    def __init__(self, root, master):
        Toplevel.__init__(self, root)
        self.master = master
        self.root = root

        self.labelSiteName = Label(self, text="Site name:", anchor=E)
        self.entrySiteName = Entry(self)

        self.labelUsername = Label(self, text="Username:", anchor=E)
        self.entryUsername = Entry(self)

        self.labelPassword = Label(self, text="Enter the password:", anchor=E)
        self.labelPassword2 = Label(self, text="Enter the password again:", anchor=E)
        self.entryPassword = Entry(self, show="*")
        self.entryPassword2 = Entry(self, show="*")

        self.addPassword = Button(self, text="Add", bg='green', activebackground='light green',
                                  command=lambda: self.checkPassword())

        self.labelSiteName.grid(column=0, row=0, pady=10)
        self.labelUsername.grid(column=0, row=1, pady=10)
        self.labelPassword.grid(column=0, row=2, pady=10)
        self.labelPassword2.grid(column=0, row=3, pady=10)

        self.entrySiteName.grid(column=1, row=0, pady=10)
        self.entryUsername.grid(column=1, row=1, pady=10)
        self.entryPassword.grid(column=1, row=2, pady=10)
        self.entryPassword2.grid(column=1, row=3, pady=10)

        self.addPassword.grid(column=0, row=4, columnspan=2, ipadx=30)
        self.title("Add new password")

    def checkPassword(self):
        if self.entryPassword.get() == self.entryPassword2.get():
            dao.saveUserData(siteName=self.entrySiteName.get(), userName=self.entryUsername.get(),
                             password=self.entryPassword.get())
        else:
            message.showerror("Wrong password", "You must introduce the same password twice. Please try again")

        self.root.refreshTable(self.master)
        self.destroy()

