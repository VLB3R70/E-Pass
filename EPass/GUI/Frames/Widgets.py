from tkinter import *
from tkinter.ttk import *

from EPass.API.DAODatabase import DAO

dao = DAO()


class EntriesTable(Treeview):
    def __init__(self, root):
        Treeview.__init__(self, root)

        scroll = Scrollbar(self)
        scroll.pack(side=RIGHT, fill=Y)

        scroll = Scrollbar(self, orient='horizontal')
        scroll.pack(side=BOTTOM, fill=X)

        table = Treeview(self, yscrollcommand=scroll.set, xscrollcommand=scroll.set)
        table.pack()

        table['columns'] = ('ID', 'Site name', 'Username')
        table.column("#0", width=0, stretch=NO)

        for i in table['columns']:
            table.column(i, anchor=CENTER, width=60)

        table.heading("#0", text="", anchor=CENTER)
        for j in table['columns']:
            table.heading(j, text=j, anchor=CENTER)

        id = 0
        for k in dao.getUserData():
            table.insert(parent='', index='end', iid=str(id), text='', values=k)
            id += 1

        table.pack()

        self.pack()
