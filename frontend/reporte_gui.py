from __future__ import annotations
import logging

import tkinter as tk
from tkinter import ttk
from typing import cast, Any

from backend.controllers.estudiante_controller import ControlEstudiante
from backend.controllers.salud_controller import SaludController
from frontend.reporte_estudiante import ReporteEstudiante

logger = logging.getLogger(__name__)

class ReporteGUIEstudents(tk.Toplevel):
    def __init__(
        self,
        parent: tk.Misc,
        estudiante_controller: ControlEstudiante,
        salud_controller: SaludController,
    ) -> None:
        super().__init__(parent)
        self.title("Reporte de Estudiantes Registrados")
        self.geometry("760x420")
        self.estudiante_controller = estudiante_controller
        self.salud_controller = salud_controller
        self.estudiantes_dict = {}

        self._crear_widgets()
        self._cargar_datos()

        self.transient(cast(Any, parent))
        self.grab_set()


    def _crear_widgets(self) -> None:
        logger.debug("Creando widgets para el reporte de estudiantes")
        contenedor = ttk.Frame(self, padding=16)
        contenedor.pack(fill="both", expand=True)

        encabezado = ttk.Frame(contenedor)
        encabezado.pack(fill="x", pady=(0, 12))
        ttk.Label(encabezado, text="Reporte de estudiantes registrados", font=("Segoe UI", 14, "bold")).pack(
            side="left"
        )
        ttk.Button(encabezado, text="Actualizar", command=self._cargar_datos).pack(side="right")

        columnas = (
            "nombre",
            "identificacion",
            "genero",
            "fecha_nacimiento",
            "correo_institucional",
            "telefono",
            "direccion",
            "carrera",
            "semestre",
            "matricula",
            "peso",
            "altura",
        )
        self.tabla = ttk.Treeview(contenedor, columns=columnas, show="headings", height=12)

        encabezados = {
            "nombre": "Nombre",
            "identificacion": "Identificacion",
            "genero": "Género",
            "fecha_nacimiento": "Fecha Nac.",
            "correo_institucional": "Correo",
            "telefono": "Teléfono",
            "direccion": "Dirección",
            "carrera": "Carrera",
            "semestre": "Semestre",
            "matricula": "Matrícula",
            "peso": "Peso",
            "altura": "Altura",
        }
        anchos = {
            "nombre": 150,
            "identificacion": 120,
            "genero": 70,
            "fecha_nacimiento": 120,
            "correo_institucional": 150,
            "telefono": 100,
            "direccion": 120,
            "carrera": 120,
            "semestre": 90,
            "matricula": 100,
            "peso": 80,
            "altura": 80,
        }

        for columna in columnas:
            self.tabla.heading(columna, text=encabezados[columna])
            self.tabla.column(columna, width=anchos[columna], anchor="center")

        barra = ttk.Scrollbar(contenedor, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=barra.set)

        self.tabla.pack(side="left", fill="both", expand=True)
        barra.pack(side="right", fill="y")
        
        self.tabla.bind("<Double-1>", self._abrir_perfil_estudiante)
        

    def _cargar_datos(self) -> None:
        logger.debug("Cargando datos para el reporte completo de estudiantes...")
        
        # 1. Limpiar la tabla antes de recargar
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        
        self.estudiantes_dict.clear()

        # 2. Obtener la lista de objetos Estudiante
        estudiantes = self.estudiante_controller.listar_estudiantes()

        # 3. Iterar directamente sobre la lista de objetos
        for est in estudiantes:
            # Insertamos en la tabla accediendo a las propiedades del objeto Estudiante
            item_id = self.tabla.insert(
                "",
                "end",
                values=(
                    est.nombre,
                    est.identificacion,
                    est.genero,
                    est.fecha_nacimiento,
                    est.correo_institucional,
                    est.telefono,
                    est.direccion,
                    est.carrera,
                    est.semestre,
                    est.matricula,
                    f"{est.peso} kg",
                    f"{est.altura} m",
                ),
            )
            # Guardar referencia al estudiante
            self.estudiantes_dict[item_id] = est
        
        logger.debug(f"Se han cargado {len(estudiantes)} estudiantes a la tabla.")
    
    def _abrir_perfil_estudiante(self, event) -> None:
        """Abre el perfil elegante del estudiante al hacer doble clic en la tabla."""
        seleccion = self.tabla.selection()
        if not seleccion:
            return
        
        item_id = seleccion[0]
        if item_id in self.estudiantes_dict:
            estudiante = self.estudiantes_dict[item_id]
            ReporteEstudiante(self, estudiante)
            logger.debug(f"Abriendo perfil de {estudiante.nombre}")

