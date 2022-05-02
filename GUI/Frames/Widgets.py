from tkinter import *
from tkinter.ttk import Treeview
from .AddPassFrame import AddPassFrame
from API.DAODatabase import DAO

dao = DAO()


class EntriesTable(LabelFrame):
    def __init__(self, root):
        LabelFrame.__init__(self, root)

        scroll = Scrollbar(self, orient=VERTICAL)

        table = Treeview(self, height=10)
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
        self.config(text="Database passwords")
        self.pack(padx=40, pady=40)


class ButtonPanel(PanedWindow):

    def __init__(self, root):
        PanedWindow.__init__(self, root)
        self.addPass = Button(root, text="Add", bg='green', fg='black', activebackground='light green',
                              command=lambda: self.addNewPassword())
        self.modifyPass = Button(root, text="Modify", bg='yellow', fg='black', state=DISABLED)
        self.deletePass = Button(root, text="Delete", bg='red', fg='black', state=DISABLED)

        self.addPass.grid(column=3, row=0, pady=10, padx=20, ipadx=40)
        self.modifyPass.grid(column=3, row=1, pady=10, padx=20, ipadx=30)
        self.deletePass.grid(column=3, row=2, pady=10, padx=20, ipadx=30)

    def addNewPassword(self):
        addPasswordFrame = AddPassFrame(self)
        addPasswordFrame.tkraise()



"""class Filter(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
                labelSiteName = Label(self, text="Site name:")
        entrySiteName = Entry(self)
        entrySiteName.grid(column=1, row=3)
        labelSiteName.grid(column=0, row=3)

        labelUsername = Label(self, text="Username:")
        entryUsername = Entry(self)
        labelUsername.grid(column=0, row=4)
        entryUsername.grid(column=1, row=4)

        

        self.pack()"""
