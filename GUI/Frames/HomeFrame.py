from tkinter import *
from tkinter.ttk import Treeview

from API.DAODatabase import DAO
from .AddPassFrame import AddPassFrame

dao = DAO()


class HomeFrame(Frame):

    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root
        self.setupUI()
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

    def createTable(self):
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
        labelFrame.grid(column=0, row=0, rowspan=3, columnspan=3)

    def setupUI(self):
        self.createTable()

        self.addPass = Button(self, text="Add", bg='green', fg='black', activebackground='light green',
                              command=lambda: self.addNewPassword())
        self.modifyPass = Button(self, text="Modify", bg='yellow', fg='black', state=DISABLED)
        self.deletePass = Button(self, text="Delete", bg='red', fg='black', state=DISABLED)

        self.addPass.grid(column=3, row=0, pady=10, padx=20, ipadx=40)
        self.modifyPass.grid(column=3, row=1, pady=10, padx=20, ipadx=30)
        self.deletePass.grid(column=3, row=2, pady=10, padx=20, ipadx=30)

    def addNewPassword(self):
        root = Tk()
        addPassFrame = AddPassFrame(root)
        addPassFrame.tkraise()
