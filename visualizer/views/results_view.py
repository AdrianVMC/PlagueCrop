import tkinter as tk
from tkinter import ttk
from datetime import datetime
from utils.report_generator import generate_pdf_report

class ResultsView(tk.Frame):
    def __init__(self, master, controller, grid, settings):
        super().__init__(master)
        self.controller = controller
        self.grid = grid
        self.settings = settings
        self._build_ui()

    def _build_ui(self):
        title = ttk.Label(self, text="Resultados de la Simulación", font=("Arial", 18))
        title.pack(pady=10)

        self.text = tk.Text(self, height=20, width=80, bg="#1e1e1e", fg="white")
        self.text.pack(pady=10)

        self._display_results()

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        back_btn = ttk.Button(button_frame, text="Nueva Simulación", command=self._back_to_settings)
        back_btn.pack(side="left", padx=5)

        export_btn = ttk.Button(button_frame, text="Exportar PDF", command=self._export_pdf)
        export_btn.pack(side="left", padx=5)

    def _display_results(self):
        total = 0
        infected = 0
        recovered = 0
        damage = {"LOW": 0, "MODERATE": 0, "SEVERE": 0}

        for row in self.grid:
            for cell in row:
                if cell.occupied:
                    total += 1
                    if cell.infestation_state.name == "INFESTED":
                        infected += 1
                    elif cell.infestation_state.name == "RECOVERED":
                        recovered += 1

                    dmg = cell.damage_level.name
                    if dmg in damage:
                        damage[dmg] += 1

        self.stats = {
            "Total de celdas ocupadas": total,
            "Celdas infestadas": infected,
            "Celdas recuperadas": recovered,
            "Daño leve": damage["LOW"],
            "Daño moderado": damage["MODERATE"],
            "Daño severo": damage["SEVERE"]
        }

        for k, v in self.stats.items():
            self.text.insert("end", f"{k}: {v}\n")

    def _back_to_settings(self):
        self.controller.show_view("SettingsView")

    def _export_pdf(self):
        path = f"reports/sim_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        generate_pdf_report(path, self.settings, self.stats)
        self.text.insert("end", f"\nReporte exportado como: {path}\n")
