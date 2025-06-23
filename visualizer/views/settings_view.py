import tkinter as tk
from tkinter import ttk

class SettingsView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg="#F0F0F0")
        self.controller = controller
        self._create_widgets()
    
    def _create_widgets(self):
        section_plague = ttk.LabelFrame(self, text="Entorno", style="Section.TLabelframe")
        section_plague.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        section_env = ttk.LabelFrame(self, text="Cultivos", style="Section.TLabelframe")
        section_env.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        section_crop = ttk.LabelFrame(self, text="Plaga", style="Section.TLabelframe")
        section_crop.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Label(section_plague, text="Opciones del entorno...").pack(padx=5, pady=5)
        ttk.Label(section_env, text="Opciones de los cultivos...").pack(padx=5, pady=5)
        ttk.Label(section_crop, text="Opciones de la plaga...").pack(padx=5, pady=5)

        section_footer = tk.Frame(self, bg="#DDDDDD")
        section_footer.grid(row=3, column=0, pady=10)

        ttk.Button(section_footer, text="Continuar", style="Primary.TButton").pack(pady=5)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=0)
        self.grid_columnconfigure(0, weight=1)
