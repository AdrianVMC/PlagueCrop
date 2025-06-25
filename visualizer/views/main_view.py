import tkinter as tk

class MainView(tk.Frame):
    def __init__(self, master, show_view_callback):
        super().__init__(master)
        self.show_view_callback = show_view_callback
        self._build()

    def _build(self):
        title = tk.Label(self, text="Bienvenido a PlagueCrop Simulator", font=("Arial", 16, "bold"))
        title.pack(pady=30)

        subtitle = tk.Label(self, text="Simulador de propagación de plagas en cultivos", font=("Arial", 12))
        subtitle.pack(pady=10)

        start_button = tk.Button(self, text="Iniciar simulación", font=("Arial", 12, "bold"),
                                 command=lambda: self.show_view_callback("SimulationView"))
        start_button.pack(pady=40)
