from tkinter import *
from tkinter.ttk import Treeview

from API.DAODatabase import DAO

dao = DAO()


class EntriesTable(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)

        labelFrame = LabelFrame(self, text="Database passwords")

        scroll = Scrollbar(labelFrame, orient=VERTICAL)

        table = Treeview(labelFrame, height=10)
        table.config(yscrollcommand=scroll.set)
        scroll.config(command=table.yview())

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

        scroll.pack(side=RIGHT, fill=Y)
        table.pack()
        labelFrame.pack()
        self.pack(padx=40, pady=40)


class ButtonPanel(Frame):

    def __init__(self, root):
        Frame.__init__(self, root)
        addPass = Button(self, text="Add", bg='green', fg='black')
        modifyPass = Button(self, text="Modify", bg='yellow', fg='black', state=DISABLED)
        deletePass = Button(self, text="Delete", bg='red', fg='black', state=DISABLED)

        addPass.pack(anchor=N, pady=10, padx=20, ipadx=40)
        modifyPass.pack(anchor=CENTER, pady=10, padx=20, ipadx=30)
        deletePass.pack(anchor=S, pady=10, padx=20, ipadx=30)

        self.pack()


"""class Filter(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        labelSiteName = Label(self, text="Site name:")
        entrySiteName = Entry(self)
        entrySiteName.grid(column=1, row=0)
        labelSiteName.grid(column=0, row=0)

        labelUsername = Label(self, text="Username:")
        entryUsername = Entry(self)
        labelUsername.grid(column=0, row=1)
        entryUsername.grid(column=1, row=1)

        

        self.pack()"""
