import tkinter as tk
from visualizer import MainMenu

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PlagueCrop App")
        self.geometry("400x300")
        self.views = {}
        self.current_view = None

        self.view_classes = {
            "MainMenu": MainMenu,
        }

        self.show_view("MainMenu")

    def show_view(self, name):
        if self.current_view:
            self.current_view.destroy()
        view_class = self.view_classes[name]
        self.current_view = view_class(self, self)
        self.current_view.pack(expand=True, fill="both")
