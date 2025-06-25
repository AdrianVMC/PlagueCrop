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

        # Contenedor para ambas grillas
        grid_frame = tk.Frame(self)
        grid_frame.pack(pady=10)

        canvas_width = self.cols * self.cell_size
        canvas_height = self.rows * self.cell_size

        self.canvas_infestation = tk.Canvas(grid_frame, width=canvas_width, height=canvas_height, bg="#1e1e1e")
        self.canvas_infestation.pack(side="left", padx=10)

        self.canvas_damage = tk.Canvas(grid_frame, width=canvas_width, height=canvas_height, bg="#1e1e1e")
        self.canvas_damage.pack(side="left", padx=10)

        self.automaton = CellAutomaton(self.rows, self.cols)
        self.automaton.initialize_with_settings(self.settings)

        self.grid_view_infestation = GridView(self.canvas_infestation, self.automaton, cell_size=self.cell_size)
        self.grid_view_infestation.set_view_mode("infestation")

        self.grid_view_damage = GridView(self.canvas_damage, self.automaton, cell_size=self.cell_size)
        self.grid_view_damage.set_view_mode("damage")

        # Botones de control
        control_frame = tk.Frame(self, bg="#1e1e1e")
        control_frame.pack(pady=10)

        tk.Button(control_frame, text="Reiniciar Simulación", command=self._restart_simulation).pack(side="left", padx=5)
        tk.Button(control_frame, text="Volver a Configuración", command=lambda: controller.show_view("SettingsView")).pack(side="left", padx=5)

        self.after(500, self._run_simulation)

    def _run_simulation(self):
        if self.current_step < self.steps:
            self.automaton.step()
            self.grid_view_infestation.draw()
            self.grid_view_damage.draw()
            self.current_step += 1
            self.after(500, self._run_simulation)

    def _restart_simulation(self):
        self.current_step = 0
        self.automaton = CellAutomaton(self.rows, self.cols)
        self.automaton.initialize_with_settings(self.settings)

        self.grid_view_infestation = GridView(self.canvas_infestation, self.automaton, cell_size=self.cell_size)
        self.grid_view_infestation.set_view_mode("infestation")

        self.grid_view_damage = GridView(self.canvas_damage, self.automaton, cell_size=self.cell_size)
        self.grid_view_damage.set_view_mode("damage")

        self.grid_view_infestation.draw()
        self.grid_view_damage.draw()
        self.after(500, self._run_simulation)
