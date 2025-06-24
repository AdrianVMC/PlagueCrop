import tkinter as tk
from core import CellAutomaton
from visualizer.views.grid_view import GridView
import random

class SimulationView(tk.Frame):
    def __init__(self, master, controller, settings):
        super().__init__(master)
        self.controller = controller
        self.settings = settings

        self.rows = self.settings.get("rows", 20)
        self.cols = self.settings.get("cols", 20)
        self.cell_size = 20

        self.info_frame = tk.Frame(self, bg="#F0F0F0")
        self.info_frame.grid(row=0, column=0, sticky="nsw", padx=10, pady=10)

        self._render_config_info()

        canvas_width = self.cols * self.cell_size
        canvas_height = self.rows * self.cell_size

        self.canvas = tk.Canvas(self, width=canvas_width, height=canvas_height, bg="white")
        self.canvas.grid(row=0, column=1, padx=10, pady=10, sticky="nse")

        self.automaton = CellAutomaton(self.rows, self.cols)
        self._initialize_grid()

        self.grid_view = GridView(self.canvas, self.automaton, cell_size=self.cell_size)
        self.after(500, self.update_simulation)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def _render_config_info(self):
        tk.Label(
            self.info_frame,
            text="Simulación con los siguientes parámetros:",
            font=("Arial", 12, "bold"),
            bg="#F0F0F0"
        ).pack(anchor="w", pady=(0, 10))

        for key, value in self.settings.items():
            texto = f"{key.replace('_', ' ').capitalize()}: {value}"
            tk.Label(
                self.info_frame,
                text=texto,
                font=("Arial", 10),
                bg="#F0F0F0"
            ).pack(anchor="w")

    def _initialize_grid(self):
        grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        max_cells = self.rows * self.cols
        count = min(self.settings.get("crop_count", 10), max_cells)

        seed = self.settings.get("seed")
        if seed:
            try:
                random.seed(int(seed))
            except ValueError:
                pass

        while count > 0:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            if grid[r][c] == 0:
                grid[r][c] = 1
                count -= 1

        self.automaton.set_initial_state(grid)

    def update_simulation(self):
        self.automaton.step()
        self.grid_view.draw()
        self.after(500, self.update_simulation)
