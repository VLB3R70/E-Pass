from tkinter import *
from tkinter.ttk import *

from .Widgets import EntriesTable


class HomeFrame(PanedWindow):

    def __init__(self, root):
        PanedWindow.__init__(self, root)

        window = PanedWindow(root, orient=VERTICAL)
        self.pack(fill=BOTH, expand=1)
        table = EntriesTable(self)
        self.add(table)

        root.title("Home")
        root.minsize(1000, 600)
        self.pack()
