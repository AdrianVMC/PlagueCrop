import tkinter as tk
from core.cell_state import InfestationState, DamageLevel

class GridView:
    def __init__(self, canvas, automaton, cell_size=20, view_mode="infestation"):
        self.canvas = canvas
        self.automaton = automaton
        self.cell_size = cell_size
        self.view_mode = view_mode

    def draw(self):
        self.canvas.delete("all")
        for i, row in enumerate(self.automaton.grid):
            for j, cell in enumerate(row):
                x0 = j * self.cell_size
                y0 = i * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size

                fill = "#2b2b2b"  # default background
                outline = "#444"

                if not cell.occupied:
                    fill = "#1e1e1e"
                else:
                    if self.view_mode == "infestation":
                        if cell.infestation_state.name == "INFESTED":
                            fill = "#ff5555"
                        elif cell.infestation_state.name == "RECOVERED":
                            fill = "#55ff55"
                        elif cell.infestation_state.name == "HEALTHY":
                            fill = "#88c0d0"
                    elif self.view_mode == "damage":
                        if cell.damage_level.name == "LOW":
                            fill = "#ffcc00"
                        elif cell.damage_level.name == "MODERATE":
                            fill = "#ff8800"
                        elif cell.damage_level.name == "SEVERE":
                            fill = "#cc0000"
                        else:
                            fill = "#4caf50"

                self.canvas.create_rectangle(x0, y0, x1, y1, fill=fill, outline=outline)

        # Añadir leyenda en parte inferior
        if self.view_mode == "infestation":
            legend = [
                ("#88c0d0", "HEALTHY"),
                ("#ff5555", "INFESTED"),
                ("#55ff55", "RECOVERED")
            ]
        else:
            legend = [
                ("#4caf50", "NONE"),
                ("#ffcc00", "LOW"),
                ("#ff8800", "MODERATE"),
                ("#cc0000", "SEVERE")
            ]

        y_offset = self.cell_size * len(self.automaton.grid) + 10
        x_offset = 10
        for color, label in legend:
            self.canvas.create_rectangle(x_offset, y_offset, x_offset + 20, y_offset + 20, fill=color, outline="#444")
            self.canvas.create_text(x_offset + 30, y_offset + 10, anchor="w", text=label, fill="white", font=("Arial", 10))
            x_offset += 100