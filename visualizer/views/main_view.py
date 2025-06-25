import tkinter as tk
from tkinter import ttk

class MainView(tk.Frame):
    def __init__(self, master, show_view_callback):
        super().__init__(master)
        self.show_view_callback = show_view_callback
        self.configure(background="#f5f5f5") 
        self._build()

    def _build(self):

        container = ttk.Frame(self, style='TFrame')
        container.pack(expand=True, fill="both", padx=20, pady=20)
        

        title = ttk.Label(container, 
                         text="Bienvenido a PlagueCrop Simulator", 
                         style="Title.TLabel")
        title.pack(pady=(30, 10))

        subtitle = ttk.Label(container, 
                            text="Simulador de propagación de plagas en cultivos", 
                            style="Subtitle.TLabel")
        subtitle.pack(pady=(0, 40))
        

        start_button = ttk.Button(container, 
                                text="Iniciar simulación", 
                                style="Primary.TButton",
                                command=lambda: self.show_view_callback("SimulationView"))
        start_button.pack(pady=20, ipadx=20, ipady=5)