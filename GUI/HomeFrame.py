"""
.. module:: HomeFrame
    :synopsis:

This module implements one class named `HomeFrame` that extends the :py:mod:`tkinter.ttk.Frame` module to show some
widgets. This frame implements a table, a panel of buttons to add, modify and delete passwords; a button to copy the
selected password to clipboard and a menu bar.

When the user adds, modify or deletes a password the table automatically refreshes.

"""
from tkinter import *
import tkinter.messagebox as message
from CORE.DAODatabase import DAO
from .Widgets import EntriesTable, ButtonPanel
import pyperclip as pc

dao = DAO()


class HomeFrame(Frame):
    """
    This class implements the necessary functions to show to the user a simple table with all his data and four optional
    buttons. It also implements a menu bar with the same functions as the buttons.
    """

    def __init__(self, root, user_id):
        Frame.__init__(self, root)
        self.root = root
        self.user_id = user_id

        self.label_frame = EntriesTable(self, self.user_id)
        self.label_frame.grid(column=0, row=0, rowspan=3)
        self.button_panel = ButtonPanel(self, root)
        self.copy_to_clipboard = Button(self, text="Copy to clipboard", bg='purple3', activebackground='purple2',
                                        command=self.copy_to_clipboard)
        self.copy_to_clipboard.grid(column=0, row=7, rowspan=2, ipadx=50, padx=80)

        root.title("Home")
        root.config(menu=self.create_menu_bar())
        root.resizable(width=False, height=False)
        self.pack()

    def create_menu_bar(self):
        """
        This function creates and displays a menu bar with different options in the main frame. The options are:

        * Add
        * Modify
        * Delete

        :return: It returns the created menu bar

        :rtype: `tkinter.Menu`

        """
        menubar = Menu(self, foreground='black', activebackground='white',
                       activeforeground='black')

        add = Menu(menubar, tearoff=1, foreground='black')
        add.add_command(label="New password")
        menubar.add_cascade(label="Add", menu=add)

        modify = Menu(menubar, tearoff=1, foreground='black')
        modify.add_command(label="Selected password")
        modify.add_command(label="More than one password")
        menubar.add_cascade(label="Modify", menu=modify)

        delete = Menu(menubar, tearoff=1, foreground='black')
        delete.add_command(label="Selected passwords")
        menubar.add_cascade(label="Delete", menu=delete)

        return menubar

    def refresh_table(self, root, user_id):
        """
        This function refresh the main frame and all its widgets. The function destroys the frame and raise it again.

        :param root: It is the `Tk <https://docs.python.org/3/library/tkinter.html?highlight=tkinter#tkinter.Tk>`_
            object needed to raise a tkinter object such as a `Frame`.

        :param user_id: Is the id of the user logged. It's used for the :doc:`core` functions

        """
        self.destroy()
        self.__init__(root, user_id)

    def copy_to_clipboard(self):
        """
        This functions copies to the clipboard the selected password from the table. When copied it shows a message with
        a successful message. If the user clicks the button and there is no password selected it shows an error message.

        """
        try:
            selected = self.label_frame.idList[0]
            password = dao.get_user_password(selected)
            pc.copy(password)
            message.showinfo("Copied", "Password successfully copied to clipboard")
        except IndexError:
            message.showerror("Error", "You need to select an entry of the table")
