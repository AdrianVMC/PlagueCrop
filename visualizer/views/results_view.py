import tkinter as tk
from core.cell_state import InfestationState, DamageLevel


class ResultsView(tk.Frame):
    def __init__(self, master, controller, grid, settings):
        super().__init__(master, bg="#1e1e1e")
        self.controller = controller
        self.grid = grid
        self.settings = settings
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

        self._render_results()

    def _render_results(self):
        total = self.rows * self.cols
        occupied = 0
        infected = 0
        recovered = 0
        damaged = 0

        for row in self.grid:
            for cell in row:
                if not cell.occupied:
                    continue
                occupied += 1
                if cell.infestation_state == InfestationState.INFESTED:
                    infected += 1
                elif cell.infestation_state == InfestationState.RECOVERED:
                    recovered += 1

                if cell.damage_level != DamageLevel.NONE:
                    damaged += 1

        def pct(n):
            return f"{(n / occupied * 100):.1f}%" if occupied > 0 else "0%"

        title = tk.Label(self, text="Resultados de la Simulación", font=("Helvetica", 18, "bold"), bg="#1e1e1e", fg="white")
        title.pack(pady=20)

        results = [
            f"Celdas ocupadas: {occupied} / {total}",
            f"Celdas infestadas al final: {infected} ({pct(infected)})",
            f"Celdas recuperadas: {recovered} ({pct(recovered)})",
            f"Celdas con daño: {damaged} ({pct(damaged)})",
            f"Duración de la simulación: {self.settings.get('steps', '?')} pasos"
        ]

        for line in results:
            tk.Label(self, text=line, font=("Helvetica", 14), bg="#1e1e1e", fg="white").pack(pady=3)

        tk.Button(self, text="Volver a Configuración", command=lambda: self.controller.show_view("SettingsView"), font=("Helvetica", 12)).pack(pady=30)
