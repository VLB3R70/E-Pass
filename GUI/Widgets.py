"""
.. module:: Widgets

This module implements two custom widgets to add more functionalities to the :py:mod:`GUI.HomeFrame`. the two widgets
are: a ``tkinter.LabelFrame`` to set up a custom table and a ``tkinter.PanedWindows`` to set up the three main buttons.

"""

from tkinter import *
from tkinter.ttk import Treeview
from .AddPassFrame import AddPassFrame
from .ModifyPassFrame import ModifyPassFrame
from CORE.DAODatabase import DAO
import tkinter.messagebox as message

dao = DAO()

USER_ID = 0


class EntriesTable(LabelFrame):
    """
    .. class:: EntriesTable

    This class is used to display a custom table with all the data from the user logged. The label frame contains a
    `Treeview widget <https://tkdocs.com/tutorial/tree.html>`_ which is used to create a table since tkinter does not
    have a table widget implemented. The data is requested to the database and then is entered into the ``Treeview``
    with loops. It also has bound an event to detect when the user selects a row of the table.

    """

    def __init__(self, root, user):
        LabelFrame.__init__(self, root)
        self.idList = []
        global USER_ID
        USER_ID = user
        self.scroll = Scrollbar(self, orient=VERTICAL)

        self.table = Treeview(self, height=10, selectmode="extended")
        self.table.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.table.yview())

        self.table["columns"] = ("ID", "User", "Site name", "Username")
        self.table.column("#0", width=0, stretch=NO)

        for i in self.table["columns"]:
            self.table.column(i, anchor=W, width=200)

        self.table.heading("#0", text="", anchor=CENTER)
        for j in self.table["columns"]:
            self.table.heading(j, text=j, anchor=W)

        id = 0
        for k in dao.get_user_data(USER_ID):
            self.table.insert(parent="", index=id, iid=str(id), text="", values=k)
            id += 1

        self.table.bind("<<TreeviewSelect>>", lambda event: self.add_id_to_list())

        self.scroll.pack(side=RIGHT, fill=Y)
        self.table.pack()
        self.config(text="Database passwords")
        self.pack(padx=40, pady=40)

    def add_id_to_list(self):
        """

        This method is called when the user clicks into a table row and adds the id of the password to the list. This
        list is called by :py:meth:`.HomeFrame.copy_to_clipboard`

        """
        selected = self.table.item(self.table.selection()[0], "values")[0]
        self.idList.insert(0, selected)


class ButtonPanel(PanedWindow):
    """
    .. class:: ButtonPanel

    This class is used to display a custom panel with three buttons. These buttons are the ones to `add`, `modify` and
    `delete` passwords. When these buttons are pressed they raise their respective frames to perform the actions
    except to delete a password.

    """

    def __init__(self, root, master):
        PanedWindow.__init__(self, root)
        self.master = master
        self.root = root
        self.add_password = Button(
            root,
            text="Add",
            bg="green3",
            fg="black",
            activebackground="green1",
            command=lambda: self.add_new_password(),
        )
        self.modify_password = Button(
            root,
            text="Modify",
            bg="orange3",
            activebackground="orange1",
            fg="black",
            command=self.modify_password,
        )
        self.delete_password = Button(
            root,
            text="Delete",
            bg="red3",
            activebackground="red1",
            fg="black",
            command=self.delete_password,
        )

        self.add_password.grid(column=3, row=0, pady=10, padx=20, ipadx=40)
        self.modify_password.grid(column=3, row=1, pady=10, padx=20, ipadx=30)
        self.delete_password.grid(column=3, row=2, pady=10, padx=20, ipadx=30)

    def add_new_password(self):
        """

        This function is called when the user clicks the ``Add password`` button. When called, this function raises
        the :py:mod:`GUI.AddPassFrame`.

        """
        add_password_frame = AddPassFrame(
            root=self.root, master=self.master, user_id=USER_ID
        )
        add_password_frame.tkraise()

    def delete_password(self):
        """

        This function is called when the user clicks the ``Delete password`` button. To delete a password the user
        just needs to select the row wanted and press the button. This function will check the id of the password
        selected and delete it after the user confirms the questions.

        :except: This function excepts an ``IndexError`` if the user did not select any row from the table

        """
        try:
            if len(self.root.label_frame.table.selection()) == 1:
                selected = self.root.label_frame.table.item(
                    self.root.label_frame.table.selection()[0], "values"
                )[0]
                ask = message.askyesno(
                    "Deleting password",
                    "Are you sure you want to delete this password?",
                )
                if ask:
                    dao.delete_one_password(id=selected)
                    self.root.refresh_table(self.master)
            else:
                ask = message.askyesno(
                    "Deleting password",
                    "Are you sure you want to delete this passwords?",
                )
                if ask:
                    dao.delete_many_passwords(self.root.label_frame.idList)
                    self.root.refresh_table(self.master, USER_ID)

        except IndexError:
            message.showerror(
                "Error", "You have to select an entry of the table to delete it"
            )

    # try:
    #     selected = self.root.labelFrame.table.item(self.root.labelFrame.table.selection()[0], 'values')[0]
    #     ask = message.askyesno("Deleting password", "Are you sure you want to delete this password?")
    #     if ask:
    #         dao.deleteOnePassword(ID=selected)
    #         self.root.refreshTable(self.master)
    # except IndexError:
    #     message.showerror("Error", "You have to select an entry of the table to delete it")

    def modify_password(self):
        """

        This function is called when the user clicks the ``Modify password`` button. To modify a password the user
        has to select the password wanted in the database and then click the button.

        The function checks the id of the password selected and then raises the :py:mod:`GUI.ModifyPassFrame`. If the
        user did not select a password and clicks the button it will show an error message.

        :except: This functions excepts an ``IndexError`` if the user did not select any row from the table and displays
            an error message

        """
        try:
            selected = self.root.label_frame.table.item(
                self.root.label_frame.table.selection()[0], "values"
            )[0]
            modify_password_frame = ModifyPassFrame(
                root=self.root, master=self.master, password_id=selected, user=USER_ID
            )
            modify_password_frame.tkraise()
        except IndexError:
            message.showerror("Error", "You need to select first an entry to modify it")
