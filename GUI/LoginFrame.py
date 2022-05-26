"""
.. module:: LoginFrame
    :synopsis:

This module implements one class named `LoginFrame` that extends the :py:mod:`tkinter.ttk.Frame` module to show a simple
login frame with two text fields for the username and the master password and a button to check the data.

If the user enters its data correctly the login frame closes, and it calls to the :py:mod:`GUI.HomeFrame`

"""
import tkinter.messagebox as message
from tkinter import *
from tkinter.ttk import Frame

from CORE.DAODatabase import DAO
from .HomeFrame import HomeFrame
from .RegisterFrame import RegisterFrame

dao = DAO()
BUTTON_COLOR = "#4CAF50"
USER_ID = 0


class LoginFrame(Frame):
    """
    .. class:: LoginFrame

    This class setups all the widgets on a `ttk.Frame` and implements two functions to check if the data entered is
    correct and the other one is to register a new user in the database. If the data that the user enters is correct,
    the frame closes and the :py:mod:`GUI.HomeFrame` raises.

    """

    global USER_ID

    def __init__(self, root):
        super().__init__(root)
        self.root = root
        # self.image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img/candado.png")
        # self.img = PhotoImage(file=self.image_path)
        # self.epassImage = Label(self)
        # self.epassImage.grid(column=0, row=0, columnspan=2, pady=40)
        # self.epassImage.pack()

        self.username_label = Label(self, text="Enter your username:")
        self.username_label.grid(column=0, row=1)
        self.username_entry = Entry(self)
        self.username_entry.grid(column=0, row=2)
        self.master_password_label = Label(self, text="Enter the master password:")
        self.master_password_label.grid(column=0, row=3)
        self.master_password_entry = Entry(self, show="*")
        self.master_password_entry.bind("<Return>", lambda event: self.check_password())
        self.master_password_entry.grid(column=0, row=4)
        self.master_password_entry.focus()

        self.access_button = Button(self, text="Log in", bg=BUTTON_COLOR, activebackground="#81c784",
                                    command=lambda: self.check_password(), )
        self.access_button.grid(column=0, row=5, columnspan=2, rowspan=2, ipadx=30, pady=60)

        self.register_label = Label(self, text="I don't have a user. Register me.",
                                    font=("Helveticabold", 9, "underline"),
                                    foreground="blue", cursor="hand2", )
        self.register_label.grid(column=0, row=6, columnspan=2, rowspan=2)
        self.register_label.bind("<Button-1>", lambda e: self.register_user())

        self.root.title("Log in")
        self.root.minsize(400, 200)
        self.root.resizable(width=False, height=False)
        self.pack()

    def check_password(self):
        """

        This function checks if the password entered by the user is correct or not. If the username is in the database
        and the password it's correct, the function raise the :py:mod:`GUI.HomeFrame` with all the data from the
        database

        """
        global USER_ID
        user = self.username_entry.get()
        USER_ID = dao.get_user_id(username=user)

        # sqlite3 fetchall() function returns a list of tuples and this two lines convert it into a list
        users = dao.get_users()
        users_list = [user for i in users for user in i]

        if (self.username_entry.get() in users_list and self.master_password_entry.get() == dao.get_master_password(
                self.username_entry.get())):
            self.root.destroy()
            root = Tk()
            home_frame = HomeFrame(root, USER_ID)
            home_frame.tkraise()
        else:
            message.showerror("Error", "Incorrect password or username. Please try again")

    def register_user(self):
        """

        This functions raises the :py:mod:`GUI.RegisterFrame` to add a new user in the database. When added, the frame
        closes and the user can log in with the new username.

        """
        root = Tk()
        register_frame = RegisterFrame(root)
        register_frame.tkraise()
