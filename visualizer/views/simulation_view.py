import tkinter as tk
from core import CellAutomaton
from visualizer.views.grid_view import GridView

class SimulationView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.canvas = tk.Canvas(self, width=400, height=400)
        self.canvas.pack()

        self.automaton = CellAutomaton(20, 20)
        self.automaton.set_initial_state([
            [0]*20 for _ in range(20)
        ])
        self.automaton.grid[10][10] = 1

        self.grid_view = GridView(self.canvas, self.automaton)
        self.after(500, self.update_simulation)

    def update_simulation(self):
        self.automaton.step()
        self.grid_view.draw()
        self.after(500, self.update_simulation)