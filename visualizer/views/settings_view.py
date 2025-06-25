import tkinter as tk
from tkinter import ttk

class SettingsView(tk.Frame):
    def __init__(self, master, on_continue):
        super().__init__(master)
        self.on_continue = on_continue
        self.settings = {}
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.configure(background="#f5f5f5")
        self._build_ui()

    def _build_ui(self):
        outer_container = ttk.Frame(self)
        outer_container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        canvas = tk.Canvas(outer_container, bg="#f5f5f5", highlightthickness=0)
        h_scrollbar = ttk.Scrollbar(outer_container, orient="horizontal", command=canvas.xview)
        v_scrollbar = ttk.Scrollbar(outer_container, orient="vertical", command=canvas.yview)
        
        scrollable_frame = ttk.Frame(canvas)
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(xscrollcommand=h_scrollbar.set, yscrollcommand=v_scrollbar.set)
        
        canvas.grid(row=0, column=0, sticky="nsew")
        v_scrollbar.grid(row=0, column=1, sticky="ns")
        h_scrollbar.grid(row=1, column=0, sticky="ew")
        outer_container.grid_rowconfigure(0, weight=1)
        outer_container.grid_columnconfigure(0, weight=1)

        self._build_form_content(scrollable_frame)

    def _build_form_content(self, parent):
        ttk.Label(parent, text="Configuración de la Simulación", style="Title.TLabel")\
            .grid(row=0, column=0, columnspan=4, pady=(0, 20), sticky="w")

        for i in range(4):
            parent.grid_columnconfigure(i, weight=1, minsize=120)
        
        env_frame = ttk.LabelFrame(parent, text="Condiciones Ambientales", style="Section.TLabelframe")
        env_frame.grid(row=1, column=0, columnspan=4, sticky="ew", padx=5, pady=5, ipadx=5, ipady=5)
        self._create_radio_group(env_frame, "Nivel de humedad", "humidity", 2, 3)
        self._create_radio_group(env_frame, "Intensidad solar", "solar", 2, 3, row=1)
        self._create_radio_group(env_frame, "Nivel de pesticidas", "pesticide", 1, 3, row=2)
        self._create_entry(env_frame, "Calidad del suelo (0-100)", "soil_quality", 75, row=3)

        crop_frame = ttk.LabelFrame(parent, text="Cultivo", style="Section.TLabelframe")
        crop_frame.grid(row=2, column=0, columnspan=4, sticky="ew", padx=5, pady=5, ipadx=5, ipady=5)
        self._create_combobox(crop_frame, "Etapa del cultivo", "stage", ["GRAIN", "GROWING", "MATURE"], "GROWING")
        self._create_combobox(crop_frame, "Tipo de cultivo", "crop", ["MAIZE", "WHEAT", "BEAN"], "MAIZE", row=1)

        plague_frame = ttk.LabelFrame(parent, text="Plaga", style="Section.TLabelframe")
        plague_frame.grid(row=3, column=0, columnspan=4, sticky="ew", padx=5, pady=5, ipadx=5, ipady=5)
        self._create_combobox(plague_frame, "Tipo de plaga", "plague", ["WORM", "BUG", "FLY"], "WORM")
        self._create_combobox(plague_frame, "Densidad de infestación inicial", "infestation", ["LOW", "MEDIUM", "HIGH"], "MEDIUM", row=1)
        self._create_entry(plague_frame, "Capacidad de infestación (1-3)", "infestation_power", 2, row=2)

        sim_frame = ttk.LabelFrame(parent, text="Simulación", style="Section.TLabelframe")
        sim_frame.grid(row=4, column=0, columnspan=4, sticky="ew", padx=5, pady=5, ipadx=5, ipady=5)
        self._create_entry(sim_frame, "Densidad de ocupación (%)", "occupation", 80, col=0)
        self._create_entry(sim_frame, "Duración de infección", "infection_duration", 3, row=1, col=0)
        self._create_entry(sim_frame, "Cooldown recuperación", "recovery_cooldown", 5, row=2, col=0)
        self._create_entry(sim_frame, "Cooldown susceptibilidad", "susceptibility_cooldown", 3, col=1)
        self._create_entry(sim_frame, "Filas de la cuadrícula", "rows", 20, row=1, col=1)
        self._create_entry(sim_frame, "Columnas de la cuadrícula", "cols", 20, row=2, col=1)
        self._create_entry(sim_frame, "Número de pasos", "steps", 20, row=3, col=1)

        btn_frame = ttk.Frame(parent)
        btn_frame.grid(row=5, column=0, columnspan=4, pady=(15, 5))
        ttk.Button(btn_frame, text="Iniciar Simulación", style="Primary.TButton", command=self._submit)\
            .pack(pady=5, ipadx=20, ipady=5)

    def _create_radio_group(self, parent, label_text, var_name, default_value, max_value, row=0):
        label = ttk.Label(parent, text=label_text)
        label.grid(row=row, column=0, sticky="e", padx=5, pady=5)
        var = tk.IntVar(value=default_value)
        setattr(self, f"{var_name}_var", var)
        for i in range(1, max_value + 1):
            rb = ttk.Radiobutton(parent, text=str(i), variable=var, value=i)
            rb.grid(row=row, column=i, padx=5, pady=5, sticky="w")

    def _create_combobox(self, parent, label_text, var_name, values, default_value, row=0):
        label = ttk.Label(parent, text=label_text)
        label.grid(row=row, column=0, sticky="e", padx=5, pady=5)
        var = tk.StringVar(value=default_value)
        setattr(self, f"{var_name}_var", var)
        cb = ttk.Combobox(parent, textvariable=var, values=values, state="readonly", width=18)
        cb.grid(row=row, column=1, padx=5, pady=5, sticky="ew")

    def _create_entry(self, parent, label_text, var_name, default_value, row=0, col=0):
        label = ttk.Label(parent, text=label_text)
        label.grid(row=row, column=col*2, sticky="e", padx=5, pady=5)
        var = tk.IntVar(value=default_value)
        setattr(self, f"{var_name}_var", var)
        entry = ttk.Entry(parent, textvariable=var, width=20)
        entry.grid(row=row, column=col*2+1, padx=5, pady=5, sticky="ew")

    def _submit(self):
        self.settings = {
            "humidity": self.humidity_var.get(),
            "solar_intensity": self.solar_var.get(),
            "pesticide_level": self.pesticide_var.get(),
            "soil_quality": self.soil_quality_var.get(),
            "crop_stage": self.stage_var.get(),
            "crop_type": self.crop_var.get(),
            "plague_type": self.plague_var.get(),
            "infestation_density": self.infestation_var.get(),
            "occupation_density": self.occupation_var.get(),
            "infestation_power": self.infestation_power_var.get(),
            "infection_duration_threshold": self.infection_duration_var.get(),
            "recovery_cooldown": self.recovery_cooldown_var.get(),
            "susceptibility_cooldown": self.susceptibility_cooldown_var.get(),
            "rows": self.rows_var.get(),
            "cols": self.cols_var.get(),
            "steps": self.steps_var.get()
        }
        self.on_continue()

    def get_settings(self):
        return self.settings
