import tkinter as tk
from core.cell_state import InfestationState, DamageLevel

class GridView:
    def __init__(self, canvas, automaton, cell_size=20, view_mode="infestation"):
        self.canvas = canvas
        self.automaton = automaton
        self.cell_size = cell_size
        self.view_mode = view_mode
        self._setup_colors()
        self.legend_height = 40

    def _setup_colors(self):
        self.colors = {
            "background": "#2b2b2b",
            "unoccupied": "#00e7f8",
            "outline": "#444",
            "text": "#ffffff",
            "legend_bg": "#333333",
            "infestation": {
                "HEALTHY": "#00ff15",
                "EXPOSED": "#a200ff",   
                "INFESTED_LIGHT": "#002fff",  
                "INFESTED_SEVERE": "#e74c3c",  
                "RECOVERED": "#2ecc71" 
            },
            "damage": {
                "NONE": "#ffffff", 
                "LOW": "#bebebe",
                "MODERATE": "#7b7b7b",
                "SEVERE": "#000000"
            }
        }

    def _get_legend_data(self):
        """Devuelve los datos de la leyenda según el modo de vista"""
        if self.view_mode == "infestation":
            return [
                (self.colors["infestation"]["HEALTHY"], "Sano"),
                (self.colors["infestation"]["EXPOSED"], "Expuesto"),
                (self.colors["infestation"]["INFESTED_LIGHT"], "Infest. leve"),
                (self.colors["infestation"]["INFESTED_SEVERE"], "Infest. grave"),
                (self.colors["infestation"]["RECOVERED"], "Recuperado")
            ]
        else:
            return [
                (self.colors["damage"]["NONE"], "Sin daño"),
                (self.colors["damage"]["LOW"], "Leve"),
                (self.colors["damage"]["MODERATE"], "Moderado"),
                (self.colors["damage"]["SEVERE"], "Severo")
            ]

    def draw(self):
        self.canvas.delete("all")
        self._draw_grid()
        self._draw_legend()

    def _draw_grid(self):
        grid_height = len(self.automaton.grid) * self.cell_size
        self.canvas.config(height=grid_height + self.legend_height)
        
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
        grid_height = len(self.automaton.grid) * self.cell_size
        legend_y = grid_height + 10
        

        self.canvas.create_rectangle(
            0, grid_height,
            self.canvas.winfo_width(), grid_height + self.legend_height,
            fill=self.colors["legend_bg"],
            outline=""
        )
        
        title = "Infestación" if self.view_mode == "infestation" else "Daño"
        self.canvas.create_text(
            10, legend_y + 5,
            anchor="nw",
            text=title + ":",
            fill=self.colors["text"],
            font=("Segoe UI", 9, "bold")
        )
        
        x_offset = 120
        for color, label in legend_data:
            self.canvas.create_rectangle(
                x_offset, legend_y + 5,
                x_offset + 15, legend_y + 20,
                fill=color,
                outline=self.colors["outline"],
                width=1
            )
            
            self.canvas.create_text(
                x_offset + 20, legend_y + 12,
                anchor="w",
                text=label,
                fill=self.colors["text"],
                font=("Segoe UI", 9)
            )
            
            x_offset += 120

        self.canvas.create_line(
            0, grid_height,
            self.canvas.winfo_width(), grid_height,
            fill=self.colors["outline"],
            width=1
        )