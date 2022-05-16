"""
.. module:: RegisterFrame
    :synopsis:

This module implements all necessary functions to display a simple form of registration. The ``RegisterFrame`` class
extends from ``tkinter.Frame`` and implements two functions to check if the entries of the form are empty and to
register a new user into the database.

"""

import tkinter.messagebox as message
from tkinter import *

from CORE.DAODatabase import DAO

dao = DAO()


class RegisterFrame(Frame):
    """
    This class implements the necessary widgets from `Tkinter
    <https://docs.python.org/3/library/tkinter.html?highlight=tkinter#module-tkinter>`_ to display a simple registration
    form. This frame will ask for the `username`, the `master password` and the `email`. When submitted, it checks if
    there is an empty entry, and then it adds a new user to the database.
    """

    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root

        self.user_label = Label(self, text="Enter the new username:")
        self.user_label.grid(column=0, row=1)
        self.master_password_label = Label(self, text="Enter the new master password:")
        self.master_password_label.grid(column=0, row=2)
        self.email_label = Label(self, text="Enter your e-mail:")
        self.email_label.grid(column=0, row=3)

        self.username_entry = Entry(self)
        self.username_entry.grid(column=1, row=1)
        self.master_password_entry = Entry(self, show='*')
        self.master_password_entry.grid(column=1, row=2)
        self.master_password_entry.bind("<Return>", lambda event: self.register_user())
        self.email_entry = Entry(self)
        self.email_entry.grid(column=1, row=3)
        self.email_entry.bind("<Return>", lambda event: self.register_user())

        self.register_button = Button(self, text="Register", bg="#4CAF50", activebackground="#81c784",
                                      command=lambda: self.register_user())
        self.register_button.grid(column=0, row=4, columnspan=2, rowspan=2, ipadx=30, pady=40)

        self.root.title("Registration")
        self.root.configure(padx=60, pady=20)
        self.root.minsize(300, 200)
        self.root.maxsize(500, 200)
        self.pack()

    def register_user(self):
        """
        This function is called when the user submits the form, it also calls the :py:meth:`.empty_entries` method to
        check if either the master password or the username entry are empty. When is checked, this function adds a new
        user in the database with the data submitted.

        """
        if self.empty_entries():
            message.showwarning("Empty values", "There are empty entries, please enter the necessary data")
        else:
            ask = message.askyesno("Caution", "Are you sure you want to create a new user?")
            if ask:
                dao.new_user(self.username_entry.get(), self.master_password_entry.get(), self.email_entry.get())
                info = message.showinfo("Success", "User created successfully")
                self.root.destroy()
            else:
                pass

    def empty_entries(self):
        """
        This function checks if the value of the entries equals a blank space or not and returns a boolean value.

        :return: If there are empty entries it returns ``True`` if not it returns ``False``

        :rtype: bool

        """
        if self.master_password_entry.get() == '' or self.username_entry.get() == '':
            return True
        else:
            return False
