import tkinter as tk
from tkinter import ttk
from visualizer import MainView, SettingsView, SimulationView, BaseStyles

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

        style = ttk.Style(self)
        BaseStyles(style)

        self.view_classes = {
            "MainView": MainView,
            "SettingsView": SettingsView,
            "SimulationView": SimulationView
        }

        self.current_view = None
        self.settings = {}

        self.show_view("MainView")

    def show_view(self, view_name):
        if self.current_view:
            self.current_view.destroy()

        view_class = self.view_classes.get(view_name)
        if not view_class:
            raise ValueError(f"View {view_name} not found")

        if view_name == "SettingsView":
            self.current_view = view_class(self, self.on_continue)
        elif view_name == "SimulationView":
            self.current_view = view_class(self, self, self.settings)
        else:
            self.current_view = view_class(self, self)

        self.current_view.pack(expand=True, fill="both", padx=20, pady=20)

    def on_continue(self):
        if hasattr(self.current_view, "get_settings"):
            self.settings = self.current_view.get_settings()
        self.show_view("SimulationView")

if __name__ == "__main__":
    app = App()
    app.mainloop()
