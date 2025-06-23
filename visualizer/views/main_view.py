import tkinter as tk
from tkinter import ttk

class MainView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg="#F0F0F0")
        self.controller = controller
        self._create_widgets()
    
    def _create_widgets(self):
        container = tk.Frame(self, bg="#F0F0F0")
        container.pack(expand=True, fill=tk.BOTH, padx=50, pady=50)
        
        title_label = ttk.Label(
            container,
            text="PlagueCrop Simulator",
            style='Title.TLabel'
        )
        title_label.pack(pady=(0, 20))
        
        description_text = (
            "Este simulador permitirá visualizar los posibles escenarios de plagas "
            "en diferentes tipos de cultivos, considerando diferentes tipos de factores "
            "como pesticidas, condiciones ambientales, etc."
        )
        

        desc_label = ttk.Label(
            container,
            text=description_text,
            style='Subtitle.TLabel',
            wraplength=500,
            justify=tk.CENTER
        )
        desc_label.pack(pady=(0, 40))
        
        button_frame = tk.Frame(container, bg="#F0F0F0")
        button_frame.pack()

        buttons = [
            ("Crear", lambda: self.controller.show_view("SettingsView")),
            ("Salir", self.controller.quit)
        ]

        for text, command in buttons:
            style_name = 'Primary.TButton' if text != "Salir" else 'Danger.TButton'
            btn = ttk.Button(button_frame, text=text, command=command, style=style_name)
            btn.pack(side=tk.LEFT, padx=10, pady=10, ipadx=20)
