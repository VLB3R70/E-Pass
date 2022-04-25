from tkinter import *
from tkinter.ttk import *


modifyButtonStyle = Style()
modifyButtonStyle.configure("ModifyButton", background='#6b00ff')

class Entries:
    def __init__(self, root, siteName, user):
        self.root = root
        self.siteName = siteName
        self.user = user

    def newEntry(self):
        Label(self.root, text=self.siteName).grid(row=0, column=0)
        Label(self.root, text=self.user).grid(row=1, column=0)
        Button(self.root, text='Modify', style="ModifyButton").grid(row=0, column=2)
        Button(self.root, text='Copy pass').grid(row=1, column=2)


root = Tk()
e = Entries(root, 'prueba', 'prueba').newEntry()
root.mainloop()
