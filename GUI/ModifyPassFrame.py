from tkinter import *
import tkinter.messagebox as message
from CORE.DAODatabase import DAO

dao = DAO()


class ModifyPassFrame(Toplevel):
    def __init__(self, root, master, password_id, user):
        Toplevel.__init__(self, root)
        self.root = root
        self.master = master
        self.passwordId = password_id
        self.user = user

        self.labelSiteName = Label(self, text="Enter the new site name")
        self.labelUsername = Label(self, text="Enter the new username")
        self.labelOldPassword = Label(self, text="Enter the old password")
        self.labelNewPassword = Label(self, text="Enter the new password")

        self.entrySiteName = Entry(self)
        self.entryUsername = Entry(self)
        self.entryOldPassword = Entry(self, show="*")
        self.entryNewPassword = Entry(self, show="*")

        self.modifyPassword = Button(self, text="Modify", bg='orange3', activebackground='orange1',
                                     command=self.modify_password)

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

    def modify_password(self):
        if self.entrySiteName.get() != "":
            dao.update_site_name(id=self.passwordId, new_site_name=self.entrySiteName.get())
            self.root.refresh_table(self.master, self.user)
        elif self.entryUsername.get() != "":
            dao.update_username(self.passwordId, self.entryUsername.get())
            self.root.refresh_table(self.master, self.user)
        elif self.entryNewPassword.get() != "":
            if self.entryOldPassword.get() == dao.get_user_password(self.passwordId):
                dao.update_user_password(self.passwordId, self.entryNewPassword.get())
                self.root.refresh_table(self.master, self.user)
            else:
                message.showerror("Error", "The old password doesn't matches with the given")
        else:
            message.showerror("Error", "You need to provide data in order to modify it")
