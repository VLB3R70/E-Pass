from tkinter import *


class HomeFrame(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        root.title("Home")
        root.minsize(1000, 600)
        Label(text="Prueba")
        self.pack()
