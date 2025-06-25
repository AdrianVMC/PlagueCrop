import tkinter as tk
from core.cell_state import InfestationState, DamageLevel

class GridView:
    def __init__(self, canvas, automaton, cell_size=20, view_mode="infestation"):
        self.canvas = canvas
        self.automaton = automaton
        self.cell_size = cell_size
        self.view_mode = view_mode
        self._setup_colors()

    def _setup_colors(self):
        # Paleta de colores consistente con el tema
        self.colors = {
            "background": "#2b2b2b",
            "unoccupied": "#1e1e1e",
            "outline": "#444",
            "text": "#ffffff",
            "infestation": {
                "HEALTHY": "#4a90e2",  # Azul claro
                "INFESTED": "#e74c3c",  # Rojo
                "RECOVERED": "#2ecc71"  # Verde
            },
            "damage": {
                "NONE": "#4caf50",     # Verde
                "LOW": "#f39c12",      # Amarillo/naranja
                "MODERATE": "#e67e22", # Naranja
                "SEVERE": "#c0392b"    # Rojo oscuro
            }
        }

    def draw(self):
        self.canvas.delete("all")
        self._draw_grid()
        self._draw_legend()

    def _draw_grid(self):
        for i, row in enumerate(self.automaton.grid):
            for j, cell in enumerate(row):
                x0 = j * self.cell_size
                y0 = i * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size

                fill = self.colors["background"]
                outline = self.colors["outline"]

                if not cell.occupied:
                    fill = self.colors["unoccupied"]
                else:
                    if self.view_mode == "infestation":
                        fill = self.colors["infestation"].get(cell.infestation_state.name, fill)
                    elif self.view_mode == "damage":
                        fill = self.colors["damage"].get(cell.damage_level.name, fill)

                self.canvas.create_rectangle(
                    x0, y0, x1, y1, 
                    fill=fill, 
                    outline=outline,
                    width=1
                )

    def _draw_legend(self):
        legend_data = self._get_legend_data()
        y_offset = self.cell_size * len(self.automaton.grid) + 15
        x_offset = 20
        
        for color, label in legend_data:
            # Cuadrado de color
            self.canvas.create_rectangle(
                x_offset, y_offset, 
                x_offset + 15, y_offset + 15,
                fill=color, 
                outline=self.colors["outline"],
                width=1
            )
            
            # Texto de la leyenda
            self.canvas.create_text(
                x_offset + 25, y_offset + 8,
                anchor="w",
                text=label,
                fill=self.colors["text"],
                font=("Segoe UI", 9)
            )
            
            x_offset += 120  # Espacio entre elementos de leyenda

    def _get_legend_data(self):
        if self.view_mode == "infestation":
            return [
                (self.colors["infestation"]["HEALTHY"], "Sano"),
                (self.colors["infestation"]["INFESTED"], "Infestado"),
                (self.colors["infestation"]["RECOVERED"], "Recuperado")
            ]
        else:
            return [
                (self.colors["damage"]["NONE"], "Sin daño"),
                (self.colors["damage"]["LOW"], "Daño leve"),
                (self.colors["damage"]["MODERATE"], "Daño moderado"),
                (self.colors["damage"]["SEVERE"], "Daño severo")
            ]