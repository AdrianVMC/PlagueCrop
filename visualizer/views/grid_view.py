import tkinter as tk
from core.cell_state import InfestationState, DamageLevel

class GridView:
    def __init__(self, canvas: tk.Canvas, automaton, cell_size=20):
        self.canvas = canvas
        self.automaton = automaton
        self.cell_size = cell_size
        self.view_mode = "infestation"  # or "damage"

    def set_view_mode(self, mode: str):
        if mode in ["infestation", "damage"]:
            self.view_mode = mode

    def toggle_view_mode(self):
        self.view_mode = "damage" if self.view_mode == "infestation" else "infestation"

    def draw(self):
        self.canvas.delete("all")
        grid = self.automaton.get_grid()

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                x1 = j * self.cell_size
                y1 = i * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                color = self._get_color(cell)
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="#222")

    def _get_color(self, cell):
        if self.view_mode == "infestation":
            if cell.infestation_state == InfestationState.HEALTHY:
                return "#4caf50"  # verde
            elif cell.infestation_state == InfestationState.INFESTED:
                return "#f44336"  # rojo
            elif cell.infestation_state == InfestationState.RECOVERED:
                return "#6a5acd"  # azul/morado
            else:
                return "#9e9e9e"  # gris

        elif self.view_mode == "damage":
            if cell.damage_level == DamageLevel.NONE:
                return "#4caf50"  # verde
            elif cell.damage_level == DamageLevel.LOW:
                return "#ffeb3b"  # amarillo
            elif cell.damage_level == DamageLevel.MODERATE:
                return "#ff9800"  # naranja
            elif cell.damage_level == DamageLevel.SEVERE:
                return "#b71c1c"  # rojo oscuro
            else:
                return "#9e9e9e"
