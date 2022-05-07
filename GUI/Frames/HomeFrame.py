from tkinter import *
import tkinter.messagebox as message
from API.DAODatabase import DAO
from .Widgets import EntriesTable, ButtonPanel
import pyperclip as pc

dao = DAO()


class HomeFrame(Frame):

    def __init__(self, root, user):
        Frame.__init__(self, root)
        self.root = root
        self.user = user

        self.labelFrame = EntriesTable(self, self.user)
        self.labelFrame.grid(column=0, row=0, rowspan=3)
        self.buttonPanel = ButtonPanel(self, root)
        self.copyToClipboard = Button(self, text="Copy to clipboard", bg='purple3', activebackground='purple2',
                                      command=self.copyToClipboard)
        self.copyToClipboard.grid(column=0, row=7, rowspan=2, ipadx=50, padx=80)

        root.title("Home")
        root.config(menu=self.createMenuBar())
        root.resizable(width=False, height=False)
        self.pack()

    def createMenuBar(self):
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

    def refreshTable(self, root, user):
        self.destroy()
        self.__init__(root, user)

    def copyToClipboard(self):
        try:
            selected = self.labelFrame.table.item(self.labelFrame.table.selection()[0], 'values')[0]
            password = dao.getUserPassword(selected)
            pc.copy(password)
            message.showinfo("Copied", "Password successfully copied to clipboard")
        except IndexError:
            message.showerror("Error", "You need to select an entry of the table")
