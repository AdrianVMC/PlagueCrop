import tkinter as tk
from core.cell_state import InfestationState

class GridView:
    def __init__(self, canvas: tk.Canvas, automaton, cell_size=20):
        self.canvas = canvas
        self.automaton = automaton
        self.cell_size = cell_size

    def draw(self):
        self.canvas.delete("all")
        grid = self.automaton.get_grid()

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                x1 = j * self.cell_size
                y1 = i * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                color = self._get_color(cell.infestation_state)
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="#222")

    def _get_color(self, state: InfestationState):
        if state == InfestationState.HEALTHY:
            return "#4caf50"  # Verde
        elif state == InfestationState.INFESTED:
            return "#f44336"  # Rojo
        elif state == InfestationState.DAMAGED:
            return "#000000"  # Negro
        else:
            return "#9e9e9e"  # Gris por defecto
