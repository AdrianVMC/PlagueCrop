import tkinter as tk
from core import CellAutomaton
from visualizer.views.grid_view import GridView
from visualizer.views.results_view import ResultsView
from tkinter import ttk

class SimulationView(tk.Frame):
    def __init__(self, master, controller, settings):
        super().__init__(master)
        self.controller = controller
        self.settings = settings
        self.rows = self.settings.get("rows", 20)
        self.cols = self.settings.get("cols", 20)
        self.cell_size = 20
        self.step_counter = 0
        self.max_steps = self.settings.get("steps", 20)

        self.automaton = CellAutomaton(self.rows, self.cols, self.settings)
        self.automaton.initialize_with_settings(self.settings)

        self.canvas_frame = tk.Frame(self)
        self.canvas_frame.pack(pady=10)

        self.canvas_infestation = tk.Canvas(self.canvas_frame, width=self.cols * self.cell_size, height=self.rows * self.cell_size)
        self.canvas_damage = tk.Canvas(self.canvas_frame, width=self.cols * self.cell_size, height=self.rows * self.cell_size)

        self.canvas_infestation.pack(side="left", padx=10)
        self.canvas_damage.pack(side="right", padx=10)

        self.grid_view_infestation = GridView(self.canvas_infestation, self.automaton, cell_size=self.cell_size, view_mode="infestation")
        self.grid_view_damage = GridView(self.canvas_damage, self.automaton, cell_size=self.cell_size, view_mode="damage")

        self._render_controls()

        self.after(1000, self._run_simulation)

    def _render_controls(self):
        control_frame = tk.Frame(self)
        control_frame.pack()

        self.step_label = tk.Label(control_frame, text="Paso: 0", font=("Helvetica", 12))
        self.step_label.pack(side="left", padx=10)

    def _run_simulation(self):
        if self.step_counter >= self.max_steps:
            self.controller.show_custom_view(ResultsView, grid=self.automaton.grid, settings=self.settings)
            return

        self.automaton.step()
        self.grid_view_infestation.draw()
        self.grid_view_damage.draw()

        self.step_counter += 1
        self.step_label.config(text=f"Paso: {self.step_counter}")
        self.after(1000, self._run_simulation)
