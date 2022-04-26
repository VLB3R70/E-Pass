from tkinter import *

from EPass.EPass.DAODatabase import DAO

# modifyButtonStyle = Style()
# modifyButtonStyle.configure("ModifyButton", background='#6b00ff')
dao = DAO()

class EntriesTable:
    def __init__(self, root):
        for i in range(len(dao.getUserData())):
            for j in range(3):
                self.e = Entry(root,
                               font=('Arial', 12, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, dao.getUserData()[i][j])


root = Tk()

table = EntriesTable(root)

root.mainloop()
