"""
.. module:: ModifyPassFrame

This module implements all necessary functions to display a simple form to modify a password selected by the user. The
``ModifyPassFrame`` extends from ``tkinter.Toplevel`` and displays a form with the different option to modify from the
entry of the table. It implements one function to check the data entered by the user and modify it.

"""

from tkinter import *
import tkinter.messagebox as message
from CORE.DAODatabase import DAO

dao = DAO()


class ModifyPassFrame(Toplevel):
    """
    This class implements the necessary widgets to display a simple form to modify the password. When the user submits
    the data it calls to :py:meth:`.modify_password`.

    """

    def __init__(self, root, master, password_id, user):
        Toplevel.__init__(self, root)
        self.root = root
        self.master = master
        self.password_id = password_id
        self.user = user

        self.label_site_name = Label(self, text="Enter the new site name")
        self.label_username = Label(self, text="Enter the new username")
        self.label_old_password = Label(self, text="Enter the old password")
        self.label_new_password = Label(self, text="Enter the new password")

        self.entry_site_name = Entry(self)
        self.entry_username = Entry(self)
        self.entry_old_password = Entry(self, show="*")
        self.entry_new_password = Entry(self, show="*")

        self.modify_password = Button(
            self,
            text="Modify",
            bg="orange3",
            activebackground="orange1",
            command=self.modify_password,
        )

        self.label_site_name.grid(column=0, row=0, pady=10)
        self.label_username.grid(column=0, row=1, pady=10)
        self.label_old_password.grid(column=0, row=2, pady=10)
        self.label_new_password.grid(column=0, row=3, pady=10)

        self.entry_site_name.grid(column=1, row=0, pady=10)
        self.entry_username.grid(column=1, row=1, pady=10)
        self.entry_old_password.grid(column=1, row=2, pady=10)
        self.entry_new_password.grid(column=1, row=3, pady=10)

        self.modify_password.grid(column=0, row=4, columnspan=2, ipadx=30)

        self.title("Modifying a password")

    def modify_password(self):
        """
        When the user submits the data from the form this function is called. It checks if the entries are empty or not
        since the user will probably want to modify only the password and not the other entries. If all the entries are
        empty it will show an error message.

        """
        if self.entry_site_name.get() != "":
            dao.update_site_name(
                id=self.password_id, new_site_name=self.entry_site_name.get()
            )
            self.root.refresh_table(self.master, self.user)
        elif self.entry_username.get() != "":
            dao.update_username(self.password_id, self.entry_username.get())
            self.root.refresh_table(self.master, self.user)
        elif self.entry_new_password.get() != "":
            if self.entry_old_password.get() == dao.get_user_password(self.password_id):
                dao.update_user_password(
                    self.password_id, self.entry_new_password.get()
                )
                self.root.refresh_table(self.master, self.user)
            else:
                message.showerror(
                    "Error", "The old password doesn't matches with the given"
                )
        else:
            message.showerror("Error", "You need to provide data in order to modify it")
