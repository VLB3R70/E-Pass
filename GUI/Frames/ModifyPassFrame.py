from tkinter import *
import tkinter.messagebox as message
from API.DAODatabase import DAO

dao = DAO()


class ModifyPassFrame(Toplevel):
    def __init__(self, root, master, passwordId):
        Toplevel.__init__(self, root)
        self.root = root
        self.master = master
        self.passwordId = passwordId

        self.labelSiteName = Label(self, text="Enter the new site name")
        self.labelUsername = Label(self, text="Enter the new username")
        self.labelOldPassword = Label(self, text="Enter the old password")
        self.labelNewPassword = Label(self, text="Enter the new password")

        self.entrySiteName = Entry(self)
        self.entryUsername = Entry(self)
        self.entryOldPassword = Entry(self, show="*")
        self.entryNewPassword = Entry(self, show="*")

        self.modifyPassword = Button(self, text="Modify", bg='yellow', activebackground='light yellow',
                                     command=self.modifyPassword)

        self.labelSiteName.grid(column=0, row=0, pady=10)
        self.labelUsername.grid(column=0, row=1, pady=10)
        self.labelOldPassword.grid(column=0, row=2, pady=10)
        self.labelNewPassword.grid(column=0, row=3, pady=10)

        self.entrySiteName.grid(column=1, row=0, pady=10)
        self.entryUsername.grid(column=1, row=1, pady=10)
        self.entryOldPassword.grid(column=1, row=2, pady=10)
        self.entryNewPassword.grid(column=1, row=3, pady=10)

        self.modifyPassword.grid(column=0, row=4, columnspan=2, ipadx=30)

        self.title("Modifying a password")

    def modifyPassword(self):
        if self.entrySiteName.get() != "":
            dao.updateSitename(ID=self.passwordId, newSitename=self.entrySiteName.get())
            self.root.refreshTable(self.master)
        elif self.entryUsername.get() != "":
            dao.updateUsername(self.passwordId, self.entryUsername.get())
            self.root.refreshTable(self.master)
        elif self.entryNewPassword.get() != "":
            if self.entryOldPassword.get() == dao.getUserPassword(self.passwordId):
                dao.updateUserPassword(self.passwordId, self.entryNewPassword.get())
                self.root.refreshTable(self.master)
            else:
                message.showerror("Error", "The old password doesn't matches with the given")
        else:
            message.showerror("Error", "You need to provide data in order to modify it")
