from tkinter import *
from tkinter.ttk import *

from EPass.API.DAODatabase import DAO

dao = DAO()


class EntriesTable(LabelFrame):
    def __init__(self, root):
        LabelFrame.__init__(self, root)

        scroll = Scrollbar(self, orient=VERTICAL)
        scroll.pack(side=RIGHT, fill=Y)

        table = Treeview(self)
        table.config(yscrollcommand=scroll.set)
        scroll.config(command=table.yview())
        table.pack()

        table['columns'] = ('ID', 'Site name', 'Username')
        table.column("#0", width=0, stretch=YES)

        for i in table['columns']:
            table.column(i, anchor=CENTER, width=200)

        table.heading("#0", text="", anchor=CENTER)
        for j in table['columns']:
            table.heading(j, text=j, anchor=CENTER)

        id = 0
        for k in dao.getUserData():
            table.insert(parent='', index=id, iid=str(id), text='', values=k)
            id += 1

        self.config(text="Password tables")
        self.pack()
