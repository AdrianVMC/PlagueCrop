import tkinter as tk
from core.cell_automaton import CellAutomaton
from visualizer.views.grid_view import GridView


class SimulationView(tk.Frame):
    def __init__(self, master, controller, settings):
        super().__init__(master)
        self.controller = controller
        self.settings = settings
        self.steps = self.settings.get("steps", 20)
        self.current_step = 0

        self.rows = self.settings.get("rows", 20)
        self.cols = self.settings.get("cols", 20)
        self.cell_size = 20

        self.canvas = tk.Canvas(self, width=self.cols * self.cell_size, height=self.rows * self.cell_size)
        self.canvas.pack(pady=10)

        self.automaton = CellAutomaton(self.rows, self.cols)
        self.automaton.initialize_with_settings(self.settings)

        self.grid_view = GridView(self.canvas, self.automaton, cell_size=self.cell_size)

        # Botones de control
        control_frame = tk.Frame(self, bg="#1e1e1e")
        control_frame.pack(pady=10)

        tk.Button(control_frame, text="Reiniciar Simulación", command=self._restart_simulation).pack(side="left", padx=5)
        tk.Button(control_frame, text="Volver a Configuración", command=lambda: controller.show_view("SettingsView")).pack(side="left", padx=5)

        self.after(500, self._run_simulation)

    def _run_simulation(self):
        if self.current_step < self.steps:
            self.automaton.step()
            self.grid_view.draw()
            self.current_step += 1
            self.after(500, self._run_simulation)

    def _restart_simulation(self):
        self.current_step = 0
        self.automaton = CellAutomaton(self.rows, self.cols)
        self.automaton.initialize_with_settings(self.settings)
        self.grid_view = GridView(self.canvas, self.automaton, cell_size=self.cell_size)
        self.grid_view.draw()
        self.after(500, self._run_simulation)
