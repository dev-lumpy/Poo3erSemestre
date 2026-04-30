from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from backend.controllers.estudiante_controller import EstudianteController
from backend.controllers.salud_controller import SaludController
from frontend.reporte_gui import ReporteGUI
from frontend.registro_gui import RegistroGUI


class MainGUI:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Sistema de Seguimiento de Salud Escolar")
        self.root.geometry("560x360")
        self.root.minsize(560, 360)

        self.estudiante_controller = EstudianteController()
        self.salud_controller = SaludController()

        self._crear_interfaz()

    def _crear_interfaz(self) -> None:
        self.root.configure(bg="#f5f7fb")

        contenedor = ttk.Frame(self.root, padding=28)
        contenedor.pack(fill="both", expand=True)

        ttk.Label(
            contenedor,
            text="Sistema de Seguimiento de Salud Escolar",
            font=("Segoe UI", 18, "bold"),
        ).pack(pady=(6, 10))

        ttk.Label(
            contenedor,
            text="Registra estudiantes, calcula IMC y revisa sus clasificaciones nutricionales.",
            wraplength=460,
            justify="center",
        ).pack(pady=(0, 24))

        acciones = ttk.Frame(contenedor)
        acciones.pack()

        ttk.Button(acciones, text="Registrar estudiante", command=self.abrir_registro, width=24).grid(
            row=0, column=0, padx=10, pady=8
        )
        ttk.Button(acciones, text="Ver reporte", command=self.abrir_reporte, width=24).grid(
            row=1, column=0, padx=10, pady=8
        )
        ttk.Button(acciones, text="Salir", command=self.root.destroy, width=24).grid(
            row=2, column=0, padx=10, pady=8
        )

    def abrir_registro(self) -> None:
        RegistroGUI(self.root, self.estudiante_controller, on_guardado=self._notificar_actualizacion)

    def abrir_reporte(self) -> None:
        ReporteGUI(self.root, self.estudiante_controller, self.salud_controller)

    def _notificar_actualizacion(self) -> None:
        # El reporte se refresca manualmente; este enlace mantiene la navegacion simple.
        return None

    def ejecutar(self) -> None:
        self.root.mainloop()
