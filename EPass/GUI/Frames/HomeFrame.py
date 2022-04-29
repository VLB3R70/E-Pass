from tkinter import *
from tkinter.ttk import *

from .Widgets import EntriesTable


class HomeFrame(Frame):

    def __init__(self, root):
        Frame.__init__(self, root)
        self.option_add('*tearOff', FALSE)

        # window = PanedWindow(root, orient=VERTICAL)
        table = EntriesTable(self)
        table.grid(column=0, row=0, pady=40)

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
