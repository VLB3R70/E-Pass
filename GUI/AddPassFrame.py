"""
.. module:: AddPassFrame
    :synopsis:

This module implements one class named `AddPassFrame` that extends the :py:mod:`tkinter.TopLevel`. This module displays
a window on the top of the one who raise it. This window displays a form to enter a new password into the database.
When submitted, the windows calls to :py:meth:`.HomeFrame.refresh_table` and then it destroys itself.

"""

import tkinter.messagebox as message
from tkinter import *

from CORE.DAODatabase import DAO

dao = DAO()


class AddPassFrame(Toplevel):
    """
    This class implements the necessary functions to display a simple form to add a new password into the database.
    When submitted, the window checks if the password is correctly entered twice and if it is correct the windows
    makes a call to :py:meth:`.HomeFrame.refresh_table` and destroys itself.
    """
    def __init__(self, root, master, user_id):
        Toplevel.__init__(self, root)
        self.master = master
        self.root = root
        self.user_id = user_id

        self.labelSiteName = Label(self, text="Site name:", anchor=E)
        self.entrySiteName = Entry(self)

        self.labelUsername = Label(self, text="Username:", anchor=E)
        self.entryUsername = Entry(self)

        self.labelPassword = Label(self, text="Enter the password:", anchor=E)
        self.labelPassword2 = Label(self, text="Enter the password again:", anchor=E)
        self.entryPassword = Entry(self, show="*")
        self.entryPassword2 = Entry(self, show="*")

        self.addPassword = Button(self, text="Add", bg='green3', activebackground='green1',
                                  command=lambda: self.check_password())

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

    def check_password(self):
        """
        This function checks if the password is correctly entered twice; if is correct it saves the data in the
        database, refreshes the table in the home frame, and then it closes. If the passwords are wrong it shows an
        error message.

        """
        if self.entryPassword.get() == self.entryPassword2.get():
            num_passwords = dao.get_num_passwords(self.user_id)
            dao.save_user_data(id=str((num_passwords + 1)), user_id=self.user_id, site_name=self.entrySiteName.get(),
                               username=self.entryUsername.get(), password=self.entryPassword.get())
        else:
            message.showerror("Wrong password", "You must introduce the same password twice. Please try again")

        self.root.refresh_table(self.master, self.user_id)
        self.destroy()
