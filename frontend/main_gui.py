from __future__ import annotations

import tkinter as tk

from backend.controllers import estudiante_controller
from backend.controllers import salud_controller

from .reporte_gui import ReporteGUIEstudents
from .registro_gui import RegistroEstudiante

from .lib_gui.base_window import BaseVentana
from .lib_gui.styles import AppStyle

class SistemaPrincipal(BaseVentana):
    def __init__(self):
        super().__init__("Sistema de Gestión de Estudiantes")
        
        # 1. Título y Subtítulo
        self.crear_titulo("Sistema de Gestión de Estudiantes")
        
        self.lbl_sub = tk.Label(
            self.main_frame, 
            text="Seleccione una opción o busque un estudiante",
            font=AppStyle.FONTS["subtitulo"],
            bg=AppStyle.COLORS["panel"],
            fg="#5a6a7a"
        )
        self.lbl_sub.pack(pady=(0, 20))

        # 2. Botón Registro Estudiantes
        self.btn_estudiantes = tk.Button(self.main_frame, text="📋  Registro de Estudiantes", 
                                        command=self.abrir_registro_de_estudiantes)
        AppStyle.estilo_boton(self.btn_estudiantes)
        self.btn_estudiantes.pack(fill="x", pady=5)

        # 3. Botón Registro Salud (RECUPERADO)
        self.btn_salud = tk.Button(self.main_frame, text="🏥  Registro de Control de Salud", 
                                  command=self.abrir_registro_de_control_de_salud)
        AppStyle.estilo_boton(self.btn_salud)
        self.btn_salud.pack(fill="x", pady=(5, 20))

        # --- Separador ---
        tk.Frame(self.main_frame, bg=AppStyle.COLORS["accent"], height=2).pack(fill="x", pady=15)

        # 4. Buscador (RECUPERADO)
        self.lbl_buscar = tk.Label(self.main_frame, text="🔍  Buscador de Estudiante",
                                  font=AppStyle.FONTS["boton"], bg=AppStyle.COLORS["panel"], 
                                  fg=AppStyle.COLORS["text_dark"])
        self.lbl_buscar.pack(anchor="w")

        # Frame para agrupar Entry + Botones
        search_frame = tk.Frame(self.main_frame, bg=AppStyle.COLORS["panel"])
        search_frame.pack(fill="x", pady=10)

        self.entry_buscador = tk.Entry(search_frame)
        AppStyle.estilo_entrada(self.entry_buscador)
        self.entry_buscador.insert(0, "Nombre o ID del estudiante...")
        self.entry_buscador.config(fg=AppStyle.COLORS["placeholder"])
        
        # Binds para el placeholder
        self.entry_buscador.bind("<FocusIn>", self.on_entry_focus_in)
        self.entry_buscador.bind("<FocusOut>", self.on_entry_focus_out)
        
        # El entry se expande para ocupar el espacio restante
        self.entry_buscador.pack(side="left", fill="x", expand=True, ipady=8, padx=(0, 5))

        # Botón Buscar
        btn_buscar = tk.Button(search_frame, text="Buscar", command=self.abrir_busqueda_estudiante)
        AppStyle.estilo_boton(btn_buscar)
        btn_buscar.config(pady=8) 
        btn_buscar.pack(side="left", padx=5) # Cambiado a side="left" para que queden en fila

        # Nuevo Botón ESTUDIANTES
        # Nota: Usamos la misma configuración que btn_buscar para que sean iguales
        btn_estudiantes = tk.Button(search_frame, text="Estudiantes", command=self.abrir_estudiantes_registrados)
        AppStyle.estilo_boton(btn_estudiantes)
        btn_estudiantes.config(pady=8)
        btn_estudiantes.pack(side="left") # Se coloca a la derecha del anterior

    # --- Lógica de Callbacks ---
    def abrir_registro_de_estudiantes(self):
        RegistroEstudiante(self, estudiante_controller.ControlEstudiante())

    def abrir_estudiantes_registrados(self):
        ReporteGUIEstudents(self, estudiante_controller.ControlEstudiante(), salud_controller.SaludController())

    def abrir_registro_de_control_de_salud(self):
        print("Abriendo Registro de Control de Salud... (Funcionalidad en desarrollo)")

    def abrir_busqueda_estudiante(self):
        query = self.entry_buscador.get()
        if query and query != "Nombre o ID del estudiante...":
            estudiante = estudiante_controller.ControlEstudiante().buscar_estudiante(query)
            if estudiante:
                from .reporte_estudiante import ReporteEstudiante
                ReporteEstudiante(self, estudiante)
            else:
                print(f"No se encontró ningún estudiante con el nombre o ID '{query}'.")
        else:
            print("Por favor, ingrese un nombre o ID válido para buscar.")


    # --- Lógica del Placeholder ---
    def on_entry_focus_in(self, event):
        if self.entry_buscador.get() == "Nombre o ID del estudiante...":
            self.entry_buscador.delete(0, tk.END)
            self.entry_buscador.config(fg=AppStyle.COLORS["text_dark"])

    def on_entry_focus_out(self, event):
        if not self.entry_buscador.get():
            self.entry_buscador.insert(0, "Nombre o ID del estudiante...")
            self.entry_buscador.config(fg=AppStyle.COLORS["placeholder"])

