import tkinter as tk
from tkinter import ttk
from visualizer import MainView ,BaseStyles


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PlagueCrop Simulator")
        self.geometry("800x600")
        self.minsize(600, 400)
        self.configure(bg="#F0F0F0")

        try:
            self.iconbitmap('plaguecrop.ico')
        except:
            pass

        self.view_classes = {
            "MainView": MainView
        }

        self.current_view = None

        style = ttk.Style()
        BaseStyles(style)

        self.show_view("MainView")

    def show_view(self, view_name):
        if self.current_view:
            self.current_view.destroy()

        view_class = self.view_classes.get(view_name)
        if not view_class:
            raise ValueError(f"View {view_name} not found")

        self.current_view = view_class(self, self)
        self.current_view.pack(expand=True, fill="both", padx=20, pady=20)

if __name__ == "__main__":
    app = App()
    app.mainloop()
