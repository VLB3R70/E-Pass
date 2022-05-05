from tkinter import *
from tkinter.ttk import Treeview
from .AddPassFrame import AddPassFrame
from .ModifyPassFrame import ModifyPassFrame
from API.DAODatabase import DAO
import tkinter.messagebox as message

dao = DAO()


class EntriesTable(LabelFrame):
    def __init__(self, root):
        LabelFrame.__init__(self, root)

        self.scroll = Scrollbar(self, orient=VERTICAL)

        self.table = Treeview(self, height=10)
        self.table.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.table.yview())

        self.table['columns'] = ('ID', 'Site name', 'Username')
        self.table.column("#0", width=0, stretch=NO)

        for i in self.table['columns']:
            self.table.column(i, anchor=W, width=200)

        self.table.heading("#0", text="", anchor=CENTER)
        for j in self.table['columns']:
            self.table.heading(j, text=j, anchor=W)

        id = 0
        for k in dao.getUserData():
            self.table.insert(parent='', index=id, iid=str(id), text='', values=k)
            id += 1

        self.scroll.pack(side=RIGHT, fill=Y)
        self.table.pack()
        self.config(text="Database passwords")
        self.pack(padx=40, pady=40)


class ButtonPanel(PanedWindow):

    def __init__(self, root, master):
        PanedWindow.__init__(self, root)
        self.master = master
        self.root = root
        self.addPass = Button(root, text="Add", bg='green3', fg='black', activebackground='green1',
                              command=lambda: self.addNewPassword())
        self.modifyPass = Button(root, text="Modify", bg='orange3', activebackground='orange1', fg='black',
                                 command=self.modifyPassword)
        self.deletePass = Button(root, text="Delete", bg='red3', activebackground='red1', fg='black',
                                 command=self.deletePassword)

        self.addPass.grid(column=3, row=0, pady=10, padx=20, ipadx=40)
        self.modifyPass.grid(column=3, row=1, pady=10, padx=20, ipadx=30)
        self.deletePass.grid(column=3, row=2, pady=10, padx=20, ipadx=30)

    def addNewPassword(self):
        addPasswordFrame = AddPassFrame(root=self.root, master=self.master)
        addPasswordFrame.tkraise()

    def deletePassword(self):
        try:
            selected = self.root.labelFrame.table.item(self.root.labelFrame.table.selection()[0], 'values')[0]
            ask = message.askyesno("Deleting password", "Are you sure you want to delete this password?")
            if ask:
                dao.deleteOnePassword(ID=selected)
                self.root.refreshTable(self.master)
        except IndexError:
            message.showerror("Error", "You have to select an entry of the table to delete it")

    def modifyPassword(self):
        try:
            selected = self.root.labelFrame.table.item(self.root.labelFrame.table.selection()[0], 'values')[0]
            modifyPasswordFrame = ModifyPassFrame(root=self.root, master=self.master, passwordId=selected)
            modifyPasswordFrame.tkraise()
        except IndexError:
            message.showerror("Error", "You need to select first an entry to modify it")


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
