import tkinter as tk
from tkinter import ttk
from core import CellAutomaton
from visualizer.views.grid_view import GridView
from visualizer.views.results_view import ResultsView

class SimulationView(tk.Frame):
    def __init__(self, master, controller, settings):
        super().__init__(master)
        self.controller = controller
        self.settings = settings
        self.configure(background="#f5f5f5")
        
        self.rows = self.settings.get("rows", 20)
        self.cols = self.settings.get("cols", 20)
        self.cell_size = 20
        self.step_counter = 0
        self.max_steps = self.settings.get("steps", 20)
        self.is_paused = False
        self.simulation_speed = 1000 
        
        self.automaton = CellAutomaton(self.rows, self.cols, self.settings)
        self.automaton.initialize_with_settings(self.settings)
        

        self._build_ui()
        

        self._run_simulation()

    def _build_ui(self):
        main_frame = ttk.Frame(self, style='TFrame')
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        ttk.Label(
            main_frame, 
            text="Simulación en Progreso", 
            style="Title.TLabel"
        ).pack(pady=(0, 15))
        
        canvas_frame = ttk.Frame(main_frame)
        canvas_frame.pack(pady=10)
        
        self.canvas_infestation = tk.Canvas(
            canvas_frame, 
            width=self.cols * self.cell_size, 
            height=self.rows * self.cell_size,
            bg="#2b2b2b",
            highlightthickness=0
        )
        self.canvas_infestation.pack(side="left", padx=10)
        
        self.canvas_damage = tk.Canvas(
            canvas_frame, 
            width=self.cols * self.cell_size, 
            height=self.rows * self.cell_size,
            bg="#2b2b2b",
            highlightthickness=0
        )
        self.canvas_damage.pack(side="right", padx=10)
        
        self.grid_view_infestation = GridView(
            self.canvas_infestation, 
            self.automaton, 
            cell_size=self.cell_size, 
            view_mode="infestation"
        )
        self.grid_view_damage = GridView(
            self.canvas_damage, 
            self.automaton, 
            cell_size=self.cell_size, 
            view_mode="damage"
        )
        

        self._build_controls(main_frame)
        

        self.grid_view_infestation.draw()
        self.grid_view_damage.draw()

    def _build_controls(self, parent):

        control_frame = ttk.Frame(parent)
        control_frame.pack(fill="x", pady=(15, 5))
        

        self.step_label = ttk.Label(
            control_frame,
            text=f"Paso: {self.step_counter}/{self.max_steps}",
            font=("Segoe UI", 11, "bold"),
            foreground="#4a6fa5"
        )
        self.step_label.pack(side="left", padx=10)

        speed_frame = ttk.Frame(control_frame)
        speed_frame.pack(side="left", padx=20)
        
        ttk.Label(
            speed_frame,
            text="Velocidad:",
            font=("Segoe UI", 9)
        ).pack(side="left")
        
        self.speed_slider = ttk.Scale(
            speed_frame,
            from_=50,
            to=2000,
            value=self.simulation_speed,
            command=self._update_speed
        )
        self.speed_slider.pack(side="left", padx=5)
        
        self.speed_label = ttk.Label(
            speed_frame,
            text=f"{self.simulation_speed}ms",
            width=6
        )
        self.speed_label.pack(side="left")
        

        btn_frame = ttk.Frame(control_frame)
        btn_frame.pack(side="right")

        self.pause_btn = ttk.Button(
            btn_frame,
            text="Pausar",
            style="Secondary.TButton",
            command=self._toggle_pause
        )
        self.pause_btn.pack(side="left", padx=5)
        
        ttk.Button(
            btn_frame,
            text="Terminar",
            style="Danger.TButton",
            command=self._end_simulation
        ).pack(side="left", padx=5)

    def _update_speed(self, value):
        """Actualiza la velocidad de la simulación basada en el slider"""
        self.simulation_speed = int(float(value))
        self.speed_label.config(text=f"{self.simulation_speed}ms")

    def _run_simulation(self):
        if self.step_counter >= self.max_steps:
            self._end_simulation()
            return
        
        if not self.is_paused:
            self.automaton.step()
            self.step_counter += 1
            self.step_label.config(text=f"Paso: {self.step_counter}/{self.max_steps}")
            
            self.grid_view_infestation.draw()
            self.grid_view_damage.draw()
        
        self.after(self.simulation_speed, self._run_simulation)

    def _toggle_pause(self):
        self.is_paused = not self.is_paused
        self.pause_btn.config(
            text="Reanudar" if self.is_paused else "Pausar",
            style="Success.TButton" if self.is_paused else "Secondary.TButton"
        )

    def _end_simulation(self):
        self.controller.show_custom_view(
            ResultsView, 
            grid=self.automaton.grid, 
            settings=self.settings
        )