import tkinter as tk
from tkinter import ttk

class SettingsView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg="#F0F0F0")
        self.controller = controller
        self._create_widgets()
    
    def _create_widgets(self):
        section_env = ttk.LabelFrame(self, text="Entorno", style="Section.TLabelframe")
        section_env.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        #ttk.Label(section_env, text="Filas:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        #self.entry_rows = ttk.Spinbox(section_env, from_=5, to=100, width=10)
        #self.entry_rows.grid(row=0, column=1, padx=5, pady=5)

        #ttk.Label(section_env, text="Columnas:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        #self.entry_cols = ttk.Spinbox(section_env, from_=5, to=100, width=10)
        #self.entry_cols.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(section_env, text="Semilla aleatoria:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_seed = ttk.Entry(section_env, width=12)
        self.entry_seed.grid(row=2, column=1, padx=5, pady=5)

        section_crop = ttk.LabelFrame(self, text="Cultivos", style="Section.TLabelframe")
        section_crop.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        ttk.Label(section_crop, text="Tipo de cultivo:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.combo_crop_type = ttk.Combobox(section_crop, values=["Maíz", "Trigo", "Arroz"], width=15)
        self.combo_crop_type.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(section_crop, text="Cantidad inicial:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_crop_count = ttk.Spinbox(section_crop, from_=1, to=500, width=10)
        self.entry_crop_count.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(section_crop, text="Distribución:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.combo_distribution = ttk.Combobox(section_crop, values=["Uniforme", "Agrupada", "Aleatoria"], width=15)
        self.combo_distribution.grid(row=2, column=1, padx=5, pady=5)

        section_plague = ttk.LabelFrame(self, text="Plaga", style="Section.TLabelframe")
        section_plague.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        ttk.Label(section_plague, text="Tipo de plaga:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.combo_plague_type = ttk.Combobox(section_plague, values=["Langosta", "Gusano", "Roya"], width=15)
        self.combo_plague_type.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(section_plague, text="Intensidad inicial:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_intensity = ttk.Spinbox(section_plague, from_=1, to=100, width=10)
        self.entry_intensity.grid(row=1, column=1, padx=5, pady=5)


        section_footer = tk.Frame(self, bg="#F0F0F0")
        section_footer.grid(row=3, column=0, pady=10)

        ttk.Button(section_footer, text="Continuar",
                   style="Primary.TButton",
                   command=self.controller
        ).pack(pady=5)

        self.grid_columnconfigure(0, weight=1)

    def get_settings(self):
        return {
            "seed": self.entry_seed.get(),
            "crop_type": self.combo_crop_type.get(),
            "crop_count": int(self.entry_crop_count.get()),
            "distribution": self.combo_distribution.get(),
            "plague_type": self.combo_plague_type.get(),
            "intensity": int(self.entry_intensity.get())
        }
