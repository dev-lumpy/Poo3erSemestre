from __future__ import annotations

import tkinter as tk
from tkinter import messagebox
from typing import Callable

from backend.controllers.estudiante_controller import ControlEstudiante
from backend.image_handler import ImageHandler
from .lib_gui.styles import AppStyle



class RegistroEstudiante(tk.Toplevel):
    def __init__(
        self,
        parent: tk.Misc,
        estudiante_controller: ControlEstudiante,
        on_guardado: Callable[[], None] | None = None,
    ) -> None:
        super().__init__(parent)
        self.title("Registro de Estudiantes")
        self.geometry("700x650")
        self.resizable(False, False)
        self.estudiante_controller = estudiante_controller
        self.on_guardado = on_guardado

        self.nombre_var = tk.StringVar()
        self.identificacion_var = tk.StringVar()
        self.peso_var = tk.StringVar()
        self.altura_var = tk.StringVar()
        self.genero_var = tk.StringVar()
        self.fecha_nacimiento_var = tk.StringVar()
        self.correo_institucional_var = tk.StringVar()
        self.telefono_var = tk.StringVar()
        self.direccion_var = tk.StringVar()
        self.matricula_var = tk.StringVar()
        self.carrera_var = tk.StringVar()
        self.semestre_var = tk.StringVar()
        self.ruta_image = "backend/image/perfil_defecto.png"

        self.vars = {
            "nombre": self.nombre_var,
            "identificacion": self.identificacion_var,
            "fecha_nacimiento": self.fecha_nacimiento_var,
            "correo_institucional": self.correo_institucional_var,
            "telefono": self.telefono_var,
            "direccion": self.direccion_var,
            "matricula": self.matricula_var,
            "carrera": self.carrera_var,
            "semestre": self.semestre_var,
            "genero": self.genero_var,
            "image": self.ruta_image
        }

        self._crear_widgets()

    def _crear_widgets(self) -> None:
        # --- Contenedor Principal (Layout de 2 columnas) ---
        # Dividimos el main_frame en izquierda (datos) y derecha (imagen/botón)
        cuerpo = tk.Frame(self, bg=AppStyle.COLORS["panel"])
        cuerpo.pack(fill="both", expand=True)

        # Donde guardar la imagen
        self.img = ImageHandler()

        # 1. COLUMNA IZQUIERDA (Formulario)
        col_izquierda = tk.Frame(cuerpo, bg=AppStyle.COLORS["panel"])
        col_izquierda.pack(side="left", fill="both", expand=True, padx=(0, 20))

        self.lbl_nombre = tk.Label(col_izquierda, text="NOMBRE COMPLETO", font=("Helvetica", 9, "bold"),
                       bg=AppStyle.COLORS["panel"], fg="#5a6a7a")
        self.lbl_nombre.pack(anchor="w", pady=(5, 0))
        ent_nombre = tk.Entry(col_izquierda, textvariable=self.vars["nombre"])
        AppStyle.estilo_entrada(ent_nombre)
        ent_nombre.pack(fill="x", pady=(0, 10), ipady=4)

        self.lbl_identificacion = tk.Label(col_izquierda, text="IDENTIFICACION", font=("Helvetica", 9, "bold"),
                                      bg=AppStyle.COLORS["panel"], fg="#5a6a7a")
        self.lbl_identificacion.pack(anchor="w", pady=(5, 0))
        ent_identificacion = tk.Entry(col_izquierda, textvariable=self.vars["identificacion"])
        AppStyle.estilo_entrada(ent_identificacion)
        ent_identificacion.pack(fill="x", pady=(0, 10), ipady=4)

        # --- Campo de Género con Checkbutton ---
        self.lbl_gen = tk.Label(col_izquierda, text="GÉNERO (M/F)", font=("Helvetica", 9, "bold"),
                           bg=AppStyle.COLORS["panel"], fg="#5a6a7a")
        self.lbl_gen.pack(anchor="w", pady=(5, 0))

        # El Checkbutton usará tu variable existente self.vars["genero"]
        # onvalue y offvalue definen qué texto se guarda al marcar/desmarcar
        self.chk_genero = tk.Checkbutton(
            col_izquierda, 
            text="Masculino (Marcar) / Femenino (Desmarcar)",
            variable=self.vars["genero"],
            onvalue="M",
            offvalue="F",
            bg=AppStyle.COLORS["panel"],
            fg=AppStyle.COLORS["text_dark"],
            activebackground=AppStyle.COLORS["panel"],
            font=AppStyle.FONTS["subtitulo"],
            cursor="hand2"
        )

        self.chk_genero.pack(anchor="w", pady=(0, 10))
        self.lbl_fecha = tk.Label(col_izquierda, text="FECHA NACIMIENTO", font=("Helvetica", 9, "bold"),
                             bg=AppStyle.COLORS["panel"], fg="#5a6a7a")
        self.lbl_fecha.pack(anchor="w", pady=(5, 0))
        ent_fecha = tk.Entry(col_izquierda, textvariable=self.vars["fecha_nacimiento"])
        AppStyle.estilo_entrada(ent_fecha)
        ent_fecha.pack(fill="x", pady=(0, 10), ipady=4)

        self.lbl_correo = tk.Label(col_izquierda, text="CORREO INST.", font=("Helvetica", 9, "bold"),
                              bg=AppStyle.COLORS["panel"], fg="#5a6a7a")
        self.lbl_correo.pack(anchor="w", pady=(5, 0))
        ent_correo = tk.Entry(col_izquierda, textvariable=self.vars["correo_institucional"])
        AppStyle.estilo_entrada(ent_correo)
        ent_correo.pack(fill="x", pady=(0, 10), ipady=4)

        self.lbl_telefono = tk.Label(col_izquierda, text="TELEFONO", font=("Helvetica", 9, "bold"),
                                bg=AppStyle.COLORS["panel"], fg="#5a6a7a")
        self.lbl_telefono.pack(anchor="w", pady=(5, 0))
        ent_telefono = tk.Entry(col_izquierda, textvariable=self.vars["telefono"])
        AppStyle.estilo_entrada(ent_telefono)
        ent_telefono.pack(fill="x", pady=(0, 10), ipady=4)

        self.lbl_direccion = tk.Label(col_izquierda, text="DIRECCION", font=("Helvetica", 9, "bold"),
                                 bg=AppStyle.COLORS["panel"], fg="#5a6a7a")
        self.lbl_direccion.pack(anchor="w", pady=(5, 0))
        ent_direccion = tk.Entry(col_izquierda, textvariable=self.vars["direccion"])
        AppStyle.estilo_entrada(ent_direccion)
        ent_direccion.pack(fill="x", pady=(0, 10), ipady=4)

        self.lbl_carrera = tk.Label(col_izquierda, text="CARRERA", font=("Helvetica", 9, "bold"),
                               bg=AppStyle.COLORS["panel"], fg="#5a6a7a")
        self.lbl_carrera.pack(anchor="w", pady=(5, 0))
        ent_carrera = tk.Entry(col_izquierda, textvariable=self.vars["carrera"])
        AppStyle.estilo_entrada(ent_carrera)
        ent_carrera.pack(fill="x", pady=(0, 10), ipady=4)

        self.lbl_semestre = tk.Label(col_izquierda, text="SEMESTRE", font=("Helvetica", 9, "bold"),
                                bg=AppStyle.COLORS["panel"], fg="#5a6a7a")
        self.lbl_semestre.pack(anchor="w", pady=(5, 0))
        ent_semestre = tk.Entry(col_izquierda, textvariable=self.vars["semestre"])
        AppStyle.estilo_entrada(ent_semestre)
        ent_semestre.pack(fill="x", pady=(0, 10), ipady=4)

        # 2. COLUMNA DERECHA (Imagen y Botón)
        col_derecha = tk.Frame(cuerpo, bg=AppStyle.COLORS["panel"], width=250)
        col_derecha.pack(side="right", fill="both", padx=(10, 0))

        # --- Espacio para la Imagen ---
        self.lbl_foto = tk.Label(
            col_derecha, 
            text="[IMAGE A SUBIR]", 
            font=AppStyle.FONTS["subtitulo"],
            bg="#e0e6ed", # Un gris ligeramente diferente para el área de imagen
            fg=AppStyle.COLORS["text_dark"],
            width=300, height=300,
            relief="groove", bd=2 # Efecto de borde punteado
        )
        self.lbl_foto.pack(fill="x", pady=(20, 10))
        self.lbl_foto.config(image=self.img.image_defect())
        self.lbl_foto.bind("<Button-1>", self.tocar_label)
        
        # Botón para cargar imagen (Opcional pero recomendado)
        btn_foto = tk.Button(col_derecha, text="Seleccionar Foto", font=("Helvetica", 9), command=self.tocar_label) # type: ignore
        btn_foto.pack(fill="x", pady=(0, 20))

        # --- Espacio para el Botón Guardar (Abajo a la derecha) ---
        # Usamos un frame para empujar el botón al fondo si es necesario
        spacer = tk.Frame(col_derecha, bg=AppStyle.COLORS["panel"])
        spacer.pack(expand=True, fill="both")

        self.btn_guardar = tk.Button(
            col_derecha, 
            text="GUARDAR", 
            command=self._guardar
        )
        AppStyle.estilo_boton(self.btn_guardar)
        # Hacemos el botón más grande/alto para que destaque como en tu dibujo
        self.btn_guardar.config(font=("Helvetica", 12, "bold"), pady=25) 
        self.btn_guardar.pack(fill="x", side="bottom", pady=(0, 10))

    def _guardar(self) -> None:
        try:
            if not self.ruta_image:
                raise ValueError("No se ha seleccionado ninguna imagen.")

            estudiante = self.estudiante_controller.registrar_estudiante(
                nombre=self.vars["nombre"].get(),
                identificacion=self.vars["identificacion"].get(),
                genero_limpio=self.vars["genero"].get(),
                fecha_nacimiento_limpia=self.vars["fecha_nacimiento"].get(),
                correo_institucional_limpio=self.vars["correo_institucional"].get(),
                telefono_limpio=self.vars["telefono"].get(),
                direccion_limpia=self.vars["direccion"].get(),
                matricula_limpia=self.vars["matricula"].get(),
                carrera_limpia=self.vars["carrera"].get(),
                semestre_limpio=self.vars["semestre"].get(),
                image=self.ruta_image
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

    def tocar_label(self, event) -> None:
        ruta = self.img.subir_imagen()
        if not ruta:
            return
        self.image = self.img.cargar_imagen(ruta)
        self.lbl_foto.config(image=self.image)

