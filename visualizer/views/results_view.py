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
        self.configure(background="#f5f5f5")  # Fondo del tema
        self._build_ui()

    def _build_ui(self):
        # Contenedor principal para mejor organización
        main_container = ttk.Frame(self, style='TFrame')
        main_container.pack(fill="both", expand=True, padx=20, pady=20)

        # Título con estilo del tema
        title = ttk.Label(main_container, 
                         text="Resultados de la Simulación", 
                         style="Title.TLabel")
        title.pack(pady=(0, 15))

        # Frame para los resultados con scroll
        results_frame = ttk.LabelFrame(main_container, 
                                     text="Estadísticas de la Simulación", 
                                     style="Section.TLabelframe")
        results_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Text widget con scrollbar
        text_container = ttk.Frame(results_frame)
        text_container.pack(fill="both", expand=True, padx=5, pady=5)

        scrollbar = ttk.Scrollbar(text_container)
        scrollbar.pack(side="right", fill="y")

        self.text = tk.Text(text_container, 
                          height=20, 
                          width=80, 
                          yscrollcommand=scrollbar.set,
                          bg="#ffffff",  # Fondo blanco
                          fg="#333333",  # Texto oscuro
                          font=("Consolas", 10),  # Fuente monoespaciada
                          wrap="word",
                          padx=10,
                          pady=10,
                          relief="flat",
                          borderwidth=1)
        self.text.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.text.yview)

        # Mostrar resultados
        self._display_results()

        # Frame para botones
        button_frame = ttk.Frame(main_container)
        button_frame.pack(fill="x", pady=(15, 5))

        # Botón para nueva simulación
        new_sim_btn = ttk.Button(button_frame, 
                               text="Nueva Simulación", 
                               style="Primary.TButton",
                               command=self._back_to_settings)
        new_sim_btn.pack(side="left", padx=5, ipadx=10)

        # Botón para exportar PDF
        export_btn = ttk.Button(button_frame, 
                              text="Exportar PDF", 
                              style="Success.TButton",
                              command=self._export_pdf)
        export_btn.pack(side="right", padx=5, ipadx=10)

    def _display_results(self):
        # Limpiar el texto existente
        self.text.delete(1.0, "end")
        
        # Configurar tags para formato especial
        self.text.tag_configure("header", font=("Segoe UI", 11, "bold"), foreground="#4a6fa5")
        self.text.tag_configure("highlight", foreground="#e74c3c")
        self.text.tag_configure("positive", foreground="#28a745")
        
        # Calcular estadísticas
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

        # Mostrar resultados con formato
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

        # Añadir configuración usada
        self.text.insert("end", "\nCONFIGURACIÓN USADA\n", "header")
        self.text.insert("end", "="*30 + "\n\n")
        
        for k, v in self.settings.items():
            self.text.insert("end", f"• {k}: ")
            self.text.insert("end", f"{v}\n")

    def _back_to_settings(self):
        self.controller.show_view("SettingsView")

    def _export_pdf(self):
        path = f"reports/sim_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        generate_pdf_report(path, self.settings, self.stats)
        
        # Mostrar mensaje de confirmación
        self.text.insert("end", "\n\n", "header")
        self.text.insert("end", "✓ Reporte exportado exitosamente\n", "positive")
        self.text.insert("end", f"Ubicación: {path}\n")
        self.text.see("end")  # Auto-scroll al final