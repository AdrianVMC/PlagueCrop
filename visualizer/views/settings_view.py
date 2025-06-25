import tkinter as tk
from tkinter import ttk


class SettingsView(tk.Frame):
    def __init__(self, master, on_continue):
        super().__init__(master)
        self.on_continue = on_continue
        self.settings = {}

        self._build_ui()

    def _build_ui(self):
        tk.Label(self, text="Configuración de la Simulación", font=("Arial", 16, "bold")).pack(pady=10)
        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        row = 0

        # Humedad
        tk.Label(form_frame, text="Nivel de humedad").grid(row=row, column=0, sticky="e", pady=5)
        self.humidity_var = tk.IntVar(value=2)
        for i in range(1, 4):
            tk.Radiobutton(form_frame, text=str(i), variable=self.humidity_var, value=i).grid(row=row, column=i)
        row += 1

        # Solar
        tk.Label(form_frame, text="Intensidad solar").grid(row=row, column=0, sticky="e", pady=5)
        self.solar_var = tk.IntVar(value=2)
        for i in range(1, 4):
            tk.Radiobutton(form_frame, text=str(i), variable=self.solar_var, value=i).grid(row=row, column=i)
        row += 1

        # Pesticidas
        tk.Label(form_frame, text="Nivel de pesticidas").grid(row=row, column=0, sticky="e", pady=5)
        self.pesticide_var = tk.IntVar(value=1)
        for i in range(1, 4):
            tk.Radiobutton(form_frame, text=str(i), variable=self.pesticide_var, value=i).grid(row=row, column=i)
        row += 1

        # Etapa del cultivo
        tk.Label(form_frame, text="Etapa del cultivo").grid(row=row, column=0, sticky="e", pady=5)
        self.stage_var = tk.StringVar(value="GROWING")
        ttk.Combobox(form_frame, textvariable=self.stage_var, values=["GRAIN", "GROWING", "MATURE"]).grid(row=row, column=1)
        row += 1

        # Tipo de cultivo
        tk.Label(form_frame, text="Tipo de cultivo").grid(row=row, column=0, sticky="e", pady=5)
        self.crop_var = tk.StringVar(value="MAIZE")
        ttk.Combobox(form_frame, textvariable=self.crop_var, values=["MAIZE", "WHEAT", "BEAN"]).grid(row=row, column=1)
        row += 1

        # Tipo de plaga
        tk.Label(form_frame, text="Tipo de plaga").grid(row=row, column=0, sticky="e", pady=5)
        self.plague_var = tk.StringVar(value="WORM")
        ttk.Combobox(form_frame, textvariable=self.plague_var, values=["WORM", "BUG", "FLY"]).grid(row=row, column=1)
        row += 1

        # Densidad de infestación inicial
        tk.Label(form_frame, text="Densidad de infestación inicial").grid(row=row, column=0, sticky="e", pady=5)
        self.infestation_var = tk.StringVar(value="MEDIUM")
        ttk.Combobox(form_frame, textvariable=self.infestation_var, values=["LOW", "MEDIUM", "HIGH"]).grid(row=row, column=1)
        row += 1

        # Densidad de ocupación
        tk.Label(form_frame, text="Densidad de ocupación de cultivos (%)").grid(row=row, column=0, sticky="e", pady=5)
        self.occupation_var = tk.IntVar(value=80)
        tk.Entry(form_frame, textvariable=self.occupation_var).grid(row=row, column=1)
        row += 1

        # Capacidad de infestación
        tk.Label(form_frame, text="Capacidad de infestación (1-3)").grid(row=row, column=0, sticky="e", pady=5)
        self.infestation_power_var = tk.IntVar(value=2)
        tk.Entry(form_frame, textvariable=self.infestation_power_var).grid(row=row, column=1)
        row += 1

        # Duración de infección (pasos)
        tk.Label(form_frame, text="Duración de infección").grid(row=row, column=0, sticky="e", pady=5)
        self.infection_duration_var = tk.IntVar(value=3)
        tk.Entry(form_frame, textvariable=self.infection_duration_var).grid(row=row, column=1)
        row += 1

        # Cooldown recuperación (pasos)
        tk.Label(form_frame, text="Cooldown de recuperación").grid(row=row, column=0, sticky="e", pady=5)
        self.recovery_cooldown_var = tk.IntVar(value=5)
        tk.Entry(form_frame, textvariable=self.recovery_cooldown_var).grid(row=row, column=1)
        row += 1

        # Tamaño del grid
        tk.Label(form_frame, text="Filas de la cuadrícula").grid(row=row, column=0, sticky="e", pady=5)
        self.rows_var = tk.IntVar(value=20)
        tk.Entry(form_frame, textvariable=self.rows_var).grid(row=row, column=1)
        row += 1

        tk.Label(form_frame, text="Columnas de la cuadrícula").grid(row=row, column=0, sticky="e", pady=5)
        self.cols_var = tk.IntVar(value=20)
        tk.Entry(form_frame, textvariable=self.cols_var).grid(row=row, column=1)
        row += 1

        # Número de pasos
        tk.Label(form_frame, text="Número de pasos").grid(row=row, column=0, sticky="e", pady=5)
        self.steps_var = tk.IntVar(value=20)
        tk.Entry(form_frame, textvariable=self.steps_var).grid(row=row, column=1)
        row += 1

        # Botón de iniciar
        tk.Button(self, text="Iniciar Simulación", command=self._submit).pack(pady=10)

    def _submit(self):
        self.settings = {
            "humidity": self.humidity_var.get(),
            "solar_intensity": self.solar_var.get(),
            "pesticide_level": self.pesticide_var.get(),
            "crop_stage": self.stage_var.get(),
            "crop_type": self.crop_var.get(),
            "plague_type": self.plague_var.get(),
            "infestation_density": self.infestation_var.get(),
            "occupation_density": self.occupation_var.get(),
            "infestation_power": self.infestation_power_var.get(),
            "infection_duration_threshold": self.infection_duration_var.get(),
            "recovery_cooldown": self.recovery_cooldown_var.get(),
            "rows": self.rows_var.get(),
            "cols": self.cols_var.get(),
            "steps": self.steps_var.get()
        }
        self.on_continue()

    def get_settings(self):
        return self.settings