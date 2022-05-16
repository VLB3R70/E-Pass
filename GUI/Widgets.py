from tkinter import *
from tkinter.ttk import Treeview
from .AddPassFrame import AddPassFrame
from .ModifyPassFrame import ModifyPassFrame
from CORE.DAODatabase import DAO
import tkinter.messagebox as message

dao = DAO()

USER_ID = 0


class EntriesTable(LabelFrame):

    def __init__(self, root, user):
        LabelFrame.__init__(self, root)
        self.idList = []
        global USER_ID
        USER_ID = user
        self.scroll = Scrollbar(self, orient=VERTICAL)

        self.table = Treeview(self, height=10, selectmode="extended")
        self.table.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.table.yview())

        self.table['columns'] = ('ID', 'User', 'Site name', 'Username')
        self.table.column("#0", width=0, stretch=NO)

        for i in self.table['columns']:
            self.table.column(i, anchor=W, width=200)

        self.table.heading("#0", text="", anchor=CENTER)
        for j in self.table['columns']:
            self.table.heading(j, text=j, anchor=W)

        id = 0
        for k in dao.get_user_data(USER_ID):
            self.table.insert(parent='', index=id, iid=str(id), text='', values=k)
            id += 1

        self.table.bind('<<TreeviewSelect>>', lambda event: self.addIdToList())

        self.scroll.pack(side=RIGHT, fill=Y)
        self.table.pack()
        self.config(text="Database passwords")
        self.pack(padx=40, pady=40)

    def addIdToList(self):
        selected = self.table.item(self.table.selection()[0], 'values')[0]
        self.idList.append(selected)


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
        addPasswordFrame = AddPassFrame(root=self.root, master=self.master, user_id=USER_ID)
        addPasswordFrame.tkraise()

    def deletePassword(self):
        try:
            if len(self.root.labelFrame.table.selection()) == 1:
                selected = self.root.labelFrame.table.item(self.root.labelFrame.table.selection()[0], 'values')[0]
                ask = message.askyesno("Deleting password", "Are you sure you want to delete this password?")
                if ask:
                    dao.delete_one_password(id=selected)
                    self.root.refresh_table(self.master)
            else:
                ask = message.askyesno("Deleting password", "Are you sure you want to delete this passwords?")
                if ask:
                    dao.delete_many_passwords(self.root.labelFrame.idList)
                    self.root.refresh_table(self.master, USER_ID)

        except IndexError:
            message.showerror("Error", "You have to select an entry of the table to delete it")

    # try:
    #     selected = self.root.labelFrame.table.item(self.root.labelFrame.table.selection()[0], 'values')[0]
    #     ask = message.askyesno("Deleting password", "Are you sure you want to delete this password?")
    #     if ask:
    #         dao.deleteOnePassword(ID=selected)
    #         self.root.refreshTable(self.master)
    # except IndexError:
    #     message.showerror("Error", "You have to select an entry of the table to delete it")

    def modifyPassword(self):
        try:
            selected = self.root.labelFrame.table.item(self.root.labelFrame.table.selection()[0], 'values')[0]
            modifyPasswordFrame = ModifyPassFrame(root=self.root, master=self.master, password_id=selected, user=USER_ID)
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
