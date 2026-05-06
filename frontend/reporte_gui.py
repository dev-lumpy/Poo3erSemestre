from __future__ import annotations
import logging

import tkinter as tk
from tkinter import ttk
from typing import cast, Any

from backend.controllers.estudiante_controller import ControlEstudiante
from backend.controllers.salud_controller import SaludController

logger = logging.getLogger(__name__)

class ReporteGUI(tk.Toplevel):
    def __init__(
        self,
        parent: tk.Misc,
        estudiante_controller: ControlEstudiante,
        salud_controller: SaludController,
    ) -> None:
        super().__init__(parent)
        self.title("Reporte de Salud")
        self.geometry("760x420")
        self.estudiante_controller = estudiante_controller
        self.salud_controller = salud_controller

        self._crear_widgets()
        self._cargar_datos()

        self.attributes('-type', 'dialog') # Le dice a Sway: "Soy un cuadro de diálogo" 
        self.transient(cast(Any, parent))  # "Soy hija de la ventana principal"
        self.grab_set()                    # "Soy la ventana principal"

    def _crear_widgets(self) -> None:
        contenedor = ttk.Frame(self, padding=16)
        contenedor.pack(fill="both", expand=True)

        encabezado = ttk.Frame(contenedor)
        encabezado.pack(fill="x", pady=(0, 12))
        ttk.Label(encabezado, text="Reporte de estudiantes registrados", font=("Segoe UI", 14, "bold")).pack(
            side="left"
        )
        ttk.Button(encabezado, text="Actualizar", command=self._cargar_datos).pack(side="right")

        columnas = ("nombre", "identificacion", "peso", "altura", "imc", "clasificacion")
        self.tabla = ttk.Treeview(contenedor, columns=columnas, show="headings", height=12)

        encabezados = {
            "nombre": "Nombre",
            "identificacion": "Identificacion",
            "peso": "Peso",
            "altura": "Altura",
            "imc": "IMC",
            "clasificacion": "Clasificacion",
        }
        anchos = {
            "nombre": 170,
            "identificacion": 120,
            "peso": 90,
            "altura": 90,
            "imc": 80,
            "clasificacion": 150,
        }

        for columna in columnas:
            self.tabla.heading(columna, text=encabezados[columna])
            self.tabla.column(columna, width=anchos[columna], anchor="center")

        barra = ttk.Scrollbar(contenedor, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=barra.set)

        self.tabla.pack(side="left", fill="both", expand=True)
        barra.pack(side="right", fill="y")

    def _cargar_datos(self) -> None:
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        estudiantes = self.estudiante_controller.listar_estudiantes()
        reportes = self.salud_controller.obtener_resumenes(estudiantes)

        for reporte in reportes:
            self.tabla.insert(
                "",
                "end",
                values=(
                    reporte["nombre"],
                    reporte["identificacion"],
                    reporte["peso"],
                    reporte["altura"],
                    reporte["imc"],
                    reporte["clasificacion"],
                ),
            )
