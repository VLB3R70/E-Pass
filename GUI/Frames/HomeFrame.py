from tkinter import *
from tkinter.ttk import Treeview
import tkinter.messagebox as message
from .Widgets import EntriesTable, ButtonPanel
from API.DAODatabase import DAO

dao = DAO()


class HomeFrame(Frame):

    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root
        self.labelFrame = EntriesTable(self)
        self.labelFrame.grid(column=0, row=0, rowspan=3)
        self.buttonPanel = ButtonPanel(self)
        root.title("Home")
        root.config(menu=self.createMenuBar())
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
