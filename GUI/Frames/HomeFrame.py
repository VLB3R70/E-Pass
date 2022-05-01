from tkinter import *

from .Widgets import EntriesTable, ButtonPanel


class HomeFrame(PanedWindow):

    def __init__(self, root):
        PanedWindow.__init__(self, root)

        table = EntriesTable(self)
        table.pack(side=TOP)
        self.add(table)

        buttons = ButtonPanel(self)
        buttons.pack(side=LEFT)
        self.add(buttons)

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
