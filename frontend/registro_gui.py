from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, ttk
from typing import Callable

from backend.controllers.estudiante_controller import EstudianteController


class RegistroGUI(tk.Toplevel):
    def __init__(
        self,
        parent: tk.Misc,
        estudiante_controller: EstudianteController,
        on_guardado: Callable[[], None] | None = None,
    ) -> None:
        super().__init__(parent)
        self.title("Registro de Estudiantes")
        self.geometry("420x320")
        self.resizable(False, False)
        self.estudiante_controller = estudiante_controller
        self.on_guardado = on_guardado

        self.nombre_var = tk.StringVar()
        self.identificacion_var = tk.StringVar()
        self.peso_var = tk.StringVar()
        self.altura_var = tk.StringVar()

        self._crear_widgets()

    def _crear_widgets(self) -> None:
        contenedor = ttk.Frame(self, padding=20)
        contenedor.pack(fill="both", expand=True)

        ttk.Label(contenedor, text="Registro de Salud Escolar", font=("Segoe UI", 14, "bold")).grid(
            row=0, column=0, columnspan=2, pady=(0, 18)
        )

        campos = [
            ("Nombre", self.nombre_var),
            ("Identificacion", self.identificacion_var),
            ("Peso (kg)", self.peso_var),
            ("Altura (m)", self.altura_var),
        ]

        for fila, (etiqueta, variable) in enumerate(campos, start=1):
            ttk.Label(contenedor, text=etiqueta).grid(row=fila, column=0, sticky="w", pady=6)
            ttk.Entry(contenedor, textvariable=variable, width=28).grid(row=fila, column=1, sticky="ew", pady=6)

        botones = ttk.Frame(contenedor)
        botones.grid(row=5, column=0, columnspan=2, pady=(18, 0), sticky="e")

        ttk.Button(botones, text="Guardar", command=self._guardar).pack(side="left", padx=(0, 8))
        ttk.Button(botones, text="Cerrar", command=self.destroy).pack(side="left")

        contenedor.columnconfigure(1, weight=1)

    def _guardar(self) -> None:
        try:
            estudiante = self.estudiante_controller.registrar_estudiante(
                nombre=self.nombre_var.get(),
                identificacion=self.identificacion_var.get(),
                peso=float(self.peso_var.get()),
                altura=float(self.altura_var.get()),
            )
        except ValueError as error:
            messagebox.showerror("Validacion", str(error), parent=self)
            return
        except Exception as error:  # pragma: no cover - defensa de interfaz
            messagebox.showerror("Error", f"No fue posible guardar el registro: {error}", parent=self)
            return

        messagebox.showinfo(
            "Exito",
            f"Estudiante {estudiante.nombre} registrado correctamente.",
            parent=self,
        )
        self.nombre_var.set("")
        self.identificacion_var.set("")
        self.peso_var.set("")
        self.altura_var.set("")
        if self.on_guardado is not None:
            self.on_guardado()
