from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from backend.controllers.estudiante_controller import ControlEstudiante
from backend.controllers.salud_controller import SaludController
from backend.controllers import estudiante_controller
from backend.controllers import salud_controller

from frontend.reporte_gui import ReporteGUI
from frontend.registro_gui import RegistroEstudiante

from .lib_gui.style_main_gui import StyleMainGUI


class SistemaPrincipal(StyleMainGUI):
    # ── Callbacks para botones ───────────────────────────────────────────────────

    def abrir_registro_de_estudiantes(self):
        RegistroEstudiante(self.root, estudiante_controller, salud_controller)


    def abrir_registro_de_control_de_salud(self):
        ReporteGUI(self.root, ControlEstudiante(), SaludController())

    def abrir_busqueda_estudiante(self):
        print(super().abrir_busqueda_estudiante())


