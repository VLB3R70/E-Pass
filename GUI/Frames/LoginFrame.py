import tkinter.messagebox as message
from tkinter import *
from tkinter.ttk import Frame

from API.DAODatabase import DAO
from .HomeFrame import HomeFrame
from .RegisterFrame import RegisterFrame

dao = DAO()
BUTTON_COLOR = "#4CAF50"
USER_ID = 0


class LoginFrame(Frame):
    global USER_ID

    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.img = PhotoImage(file='Frames/img/candado.png')
        self.epassImage = Label(self, image=self.img)
        self.epassImage.grid(column=0, row=0, columnspan=2, pady=40)

        self.usernameLabel = Label(self, text="Enter your username:")
        self.usernameLabel.grid(column=0, row=1)
        self.usernameEntry = Entry(self)
        self.usernameEntry.grid(column=0, row=2)
        self.masterPasswordLabel = Label(self, text="Enter the master password:")
        self.masterPasswordLabel.grid(column=0, row=3)
        self.masterPasswordEntry = Entry(self, show='*')
        self.masterPasswordEntry.bind("<Return>", lambda event: self.checkPassword())
        self.masterPasswordEntry.grid(column=0, row=4)
        self.masterPasswordEntry.focus()

        self.accessButton = Button(self, text="Log in", bg=BUTTON_COLOR, activebackground="#81c784",
                                   command=lambda: self.checkPassword())
        self.accessButton.grid(column=0, row=5, columnspan=2, rowspan=2, ipadx=30, pady=60)

        self.registerLabel = Label(self, text="I don't have a user. Register.",
                                   font=("Helveticabold", 9, "underline"), foreground='blue', cursor='hand2')
        self.registerLabel.grid(column=0, row=6, columnspan=2, rowspan=2)
        self.registerLabel.bind("<Button-1>", lambda event: self.registerUser())

        self.root.title("Log in")
        self.root.minsize(500, 400)
        self.root.resizable(width=False, height=False)
        self.pack()

    def checkPassword(self):
        global USER_ID
        user = self.usernameEntry.get()
        USER_ID = dao.getUserId(username=user)
        for i in dao.getUsers():
            if self.usernameEntry.get() in i and self.masterPasswordEntry.get() == dao.getMasterPassword(
                    self.usernameEntry.get()):
                self.root.destroy()
                root = Tk()
                homeFrame = HomeFrame(root, USER_ID)
                homeFrame.tkraise()
            else:
                message.showerror("Error", "Incorrect password or username. Please try again")

    def registerUser(self):
        self.root
        root = Tk()
        registerFrame = RegisterFrame(root)
        registerFrame.tkraise()
