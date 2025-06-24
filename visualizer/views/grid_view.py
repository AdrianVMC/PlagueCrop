import tkinter as tk

class GridView:
    def __init__(self, canvas, automaton, cell_size=20):
        self.canvas = canvas
        self.automaton = automaton
        self.cell_size = cell_size

    def draw(self):
        self.canvas.delete("all")
        for r in range(self.automaton.rows):
            for c in range(self.automaton.cols):
                color = "green" if self.automaton.grid[r][c] else "white"
                x1 = c * self.cell_size
                y1 = r * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")
