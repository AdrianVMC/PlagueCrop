import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from pathlib import Path
from utils.report_generator import generate_pdf_report

class ResultsView(tk.Frame):
    def __init__(self, master, controller, grid, settings):
        super().__init__(master)
        self.controller = controller
        self.grid = grid
        self.settings = settings
        self.configure(background="#f5f5f5")
        self._build_ui()

    def _build_ui(self):
        main_container = ttk.Frame(self, style='TFrame')
        main_container.pack(fill="both", expand=True, padx=20, pady=20)

        title = ttk.Label(main_container, 
                         text="Resultados de la Simulación", 
                         style="Title.TLabel")
        title.pack(pady=(0, 15))

        results_frame = ttk.LabelFrame(main_container, 
                                     text="Estadísticas de la Simulación", 
                                     style="Section.TLabelframe")
        results_frame.pack(fill="both", expand=True, padx=10, pady=10)

        text_container = ttk.Frame(results_frame)
        text_container.pack(fill="both", expand=True, padx=5, pady=5)

        scrollbar = ttk.Scrollbar(text_container)
        scrollbar.pack(side="right", fill="y")

        self.text = tk.Text(text_container, 
                          height=20, 
                          width=80, 
                          yscrollcommand=scrollbar.set,
                          bg="#ffffff", 
                          fg="#333333",
                          font=("Consolas", 10),
                          wrap="word",
                          padx=10,
                          pady=10,
                          relief="flat",
                          borderwidth=1)
        self.text.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.text.yview)

        self._display_results()

        button_frame = ttk.Frame(main_container)
        button_frame.pack(fill="x", pady=(15, 5))

        new_sim_btn = ttk.Button(button_frame, 
                               text="Nueva Simulación", 
                               style="Primary.TButton",
                               command=self._back_to_settings)
        new_sim_btn.pack(side="left", padx=5, ipadx=10)

        export_btn = ttk.Button(button_frame, 
                              text="Exportar PDF", 
                              style="Success.TButton",
                              command=self._export_pdf)
        export_btn.pack(side="right", padx=5, ipadx=10)

    def _display_results(self):
        self.text.delete(1.0, "end")
        
        self.text.tag_configure("header", font=("Segoe UI", 11, "bold"), foreground="#4a6fa5")
        self.text.tag_configure("highlight", foreground="#e74c3c")
        self.text.tag_configure("positive", foreground="#28a745")
        
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
            "Daño leve": damage["LOW"],
            "Daño moderado": damage["MODERATE"],
            "Daño severo": damage["SEVERE"]
        }

        self.text.insert("end", "RESUMEN DE LA SIMULACIÓN\n", "header")
        self.text.insert("end", "="*30 + "\n\n")
        
        for k, v in self.stats.items():
            tag = ""
            if "infestadas" in k:
                tag = "highlight"
            elif "recuperadas" in k:
                tag = "positive"
                
            self.text.insert("end", f"• {k}: ", "header")
            self.text.insert("end", f"{v}\n", tag)

        self.text.insert("end", "\nCONFIGURACIÓN USADA\n", "header")
        self.text.insert("end", "="*30 + "\n\n")
        
        for k, v in self.settings.items():
            self.text.insert("end", f"• {k}: ")
            self.text.insert("end", f"{v}\n")

    def _back_to_settings(self):
        self.controller.show_view("SettingsView")

    def _export_pdf(self):
        # Crear carpeta segura en Documentos
        base_dir = Path.home() / "Documents" / "PlagueCrop_Reports"
        base_dir.mkdir(parents=True, exist_ok=True)

        # Nombre con fecha y hora
        path = base_dir / f"sim_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

        # Generar el PDF
        generate_pdf_report(path, self.settings, self.stats)

        # Mostrar resultado en la interfaz
        self.text.insert("end", "\n\n", "header")
        self.text.insert("end", "✓ Reporte exportado exitosamente\n", "positive")
        self.text.insert("end", f"Ubicación: {path}\n")
        self.text.see("end")

        # Mostrar alerta al usuario
        messagebox.showinfo("Reporte Exportado", f"El PDF fue guardado en:\n{path}")
