from tkinter import *
from tkinter.ttk import *


class LoginFrame(Frame):

    def __init__(self, master):
        super().__init__(master)

        self.title = master.title("Log in")
        self.size = master.minsize(500, 200)

        self.img = PhotoImage(file='img/candado.png')
        self.epassImage = Label(self,image=self.img)
        self.epassImage.grid(column=2, row=3, pady=15,columnspan=2)

        self.masterPasswordLabel = Label(self, text="Master password:")
        self.masterPasswordLabel.grid(column=2, row=6, pady=70)
        self.masterPasswordEntry = Entry(self)
        self.masterPasswordEntry.grid(column=3, row=6, pady=70)

        self.pack()
