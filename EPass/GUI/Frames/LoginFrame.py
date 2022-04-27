from tkinter import *

BACKGROUND_COLOR = "#8E24AA"
BUTTON_COLOR = "#4CAF50"


class LoginFrame(Frame):

    def __init__(self, master):
        super().__init__(master)

        self.title = master.title("Log in")
        self.size = master.minsize(500, 200)
        master.config(padx=60, pady=50, bg=BACKGROUND_COLOR)

        self.img = PhotoImage(file='img/candado.png')
        self.epassImage = Label(self, image=self.img, bg=BACKGROUND_COLOR)
        self.epassImage.grid(column=0, row=0, columnspan=2)

        self.masterPasswordLabel = Label(self, text="Master password:", bg=BACKGROUND_COLOR)
        self.masterPasswordLabel.grid(column=0, row=1)
        self.masterPasswordEntry = Entry(self, show='*')
        self.masterPasswordEntry.grid(column=1, row=1)
        self.masterPasswordEntry.focus()

        self.accessButton = Button(self, text="Log in", bg=BUTTON_COLOR)
        self.accessButton.grid(column=0, row=2, columnspan=2, rowspan=2)

        self.pack()
