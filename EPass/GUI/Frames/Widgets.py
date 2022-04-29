from tkinter import *
from tkinter.ttk import Treeview

from EPass.API.DAODatabase import DAO

dao = DAO()


class EntriesTable(PanedWindow):
    def __init__(self, root):
        PanedWindow.__init__(self, root)

        labelFrame = LabelFrame(self, text="Database passwords")
        labelFrame.pack()

        scroll = Scrollbar(self, orient=VERTICAL)
        scroll.pack(side=RIGHT, fill=Y)

        table = Treeview(labelFrame, height=10)
        table.config(yscrollcommand=scroll.set)
        scroll.config(command=table.yview())
        table.pack()

        table['columns'] = ('ID', 'Site name', 'Username')
        table.column("#0", width=0, stretch=NO)

        for i in table['columns']:
            table.column(i, anchor=W, width=200)

        table.heading("#0", text="", anchor=CENTER)
        for j in table['columns']:
            table.heading(j, text=j, anchor=W)

        id = 0
        for k in dao.getUserData():
            table.insert(parent='', index=id, iid=str(id), text='', values=k)
            id += 1

        self.pack(padx=40, pady=40)


class ButtonPanel(PanedWindow):
    def __init__(self, root):
        PanedWindow.__init__(self, root)

        addPass = Button(self, text="Add", bg='green', fg='black')
        addPass.pack(anchor=N, pady=10, padx=20, ipadx=40)

        modifyPass = Button(self, text="Modify", bg='yellow', fg='black', state=DISABLED)
        modifyPass.pack(anchor=CENTER, pady=10, padx=20, ipadx=30)

        deletePass = Button(self, text="Delete", bg='red', fg='black', state=DISABLED)
        deletePass.pack(anchor=S, pady=10, padx=20, ipadx=30)

        self.pack()
