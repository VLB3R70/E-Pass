from tkinter import *
from tkinter.ttk import *

from EPass.EPass.DAODatabase import DAO

# modifyButtonStyle = Style()
# modifyButtonStyle.configure("ModifyButton", background='#6b00ff')
dao = DAO()

class EntriesTable:
    def __init__(self, root):
        for i in range(len(dao.getUserData())):
            for j in range(3):
                self.e = Entry(root, width=20,
                               font=('Arial', 16, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, dao.getUserData()[i][j])

class Entries:
    def __init__(self, root):
        self.root = root

    def newEntry(self,siteName, userName):
        Label(self.root, text=siteName).grid(row=0, column=0)
        Label(self.root, text=userName).grid(row=1, column=0)
        Button(self.root, text='Modify').grid(row=0, column=2)
        Button(self.root, text='Copy pass').grid(row=1, column=2)
        return self


root = Tk()

table = EntriesTable(root)

root.mainloop()
