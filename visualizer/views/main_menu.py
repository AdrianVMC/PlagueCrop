from tkinter import *
from tkinter import ttk

class MainMenu(Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.configure(bg='white')
        self.build_ui()

    def build_ui(self):
        label = Label(self, text="Menú Principal", font=("Helvetica", 16), bg="white", fg='black')
        label.pack(pady=20)

