from __future__ import annotations

import tkinter as tk
from tkinter import messagebox
from typing import Callable
from tkcalendar import DateEntry
import datetime

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
        self.genero_var = tk.StringVar(value="M")  # Por defecto Masculino
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
            "correo_institucional": self.correo_institucional_var,
            "telefono": self.telefono_var,
            "direccion": self.direccion_var,
            "matricula": self.matricula_var,
            "carrera": self.carrera_var,
            "semestre": self.semestre_var,
            "genero": self.genero_var,
        }

        self._crear_widgets()

    def _crear_widgets(self) -> None:
        # --- Contenedor Principal (Layout de 2 columnas) ---
        cuerpo = tk.Frame(self, bg=AppStyle.COLORS["panel"])
        cuerpo.pack(fill="both", expand=True)

        # Donde guardar la imagen
        self.img = ImageHandler()

        # 1. COLUMNA IZQUIERDA (Formulario)
        col_izquierda = tk.Frame(cuerpo, bg=AppStyle.COLORS["panel"])
        col_izquierda.pack(side="left", fill="both", expand=True, padx=(0, 20))

        # --- Nombre ---
        self.lbl_nombre = tk.Label(col_izquierda, text="NOMBRE COMPLETO", font=("Helvetica", 9, "bold"),
                       bg=AppStyle.COLORS["panel"], fg="#5a6a7a")
        self.lbl_nombre.pack(anchor="w", pady=(5, 0))
        self.ent_nombre = tk.Entry(col_izquierda, textvariable=self.vars["nombre"])
        AppStyle.estilo_entrada(self.ent_nombre)
        self.ent_nombre.pack(fill="x", pady=(0, 2), ipady=4)
        self.lbl_error_nombre = tk.Label(col_izquierda, text="", font=("Helvetica", 7, "italic"),
                                         bg=AppStyle.COLORS["panel"], fg="#e74c3c")
        self.lbl_error_nombre.pack(anchor="w", pady=(0, 4))

        # --- Identificación ---
        self.lbl_identificacion = tk.Label(col_izquierda, text="IDENTIFICACION", font=("Helvetica", 9, "bold"),
                                      bg=AppStyle.COLORS["panel"], fg="#5a6a7a")
        self.lbl_identificacion.pack(anchor="w", pady=(5, 0))
        self.ent_identificacion = tk.Entry(col_izquierda, textvariable=self.vars["identificacion"])
        AppStyle.estilo_entrada(self.ent_identificacion)
        self.ent_identificacion.pack(fill="x", pady=(0, 2), ipady=4)
        self.lbl_error_identificacion = tk.Label(col_izquierda, text="", font=("Helvetica", 7, "italic"),
                                                  bg=AppStyle.COLORS["panel"], fg="#e74c3c")
        self.lbl_error_identificacion.pack(anchor="w", pady=(0, 4))

        # --- Campo de Género con Radiobuttons ---
        self.lbl_gen = tk.Label(col_izquierda, text="GÉNERO", font=("Helvetica", 9, "bold"),
                           bg=AppStyle.COLORS["panel"], fg="#5a6a7a")
        self.lbl_gen.pack(anchor="w", pady=(5, 0))

        frame_genero = tk.Frame(col_izquierda, bg=AppStyle.COLORS["panel"])
        frame_genero.pack(anchor="w", pady=(0, 10))

        self.rb_masculino = tk.Radiobutton(
            frame_genero,
            text="Masculino",
            variable=self.vars["genero"],
            value="M",
            bg=AppStyle.COLORS["panel"],
            fg=AppStyle.COLORS["text_dark"],
            activebackground=AppStyle.COLORS["panel"],
            font=AppStyle.FONTS["subtitulo"],
            cursor="hand2",
        )
        self.rb_masculino.pack(side="left", padx=(0, 20))

        self.rb_femenino = tk.Radiobutton(
            frame_genero,
            text="Femenino",
            variable=self.vars["genero"],
            value="F",
            bg=AppStyle.COLORS["panel"],
            fg=AppStyle.COLORS["text_dark"],
            activebackground=AppStyle.COLORS["panel"],
            font=AppStyle.FONTS["subtitulo"],
            cursor="hand2",
        )
        self.rb_femenino.pack(side="left")

        # --- Fecha de Nacimiento ---
        self.lbl_fecha = tk.Label(col_izquierda, text="FECHA NACIMIENTO", font=("Helvetica", 9, "bold"),
                             bg=AppStyle.COLORS["panel"], fg="#5a6a7a")
        self.lbl_fecha.pack(anchor="w", pady=(5, 0))
        self.cal_fecha = DateEntry(
            col_izquierda,
            width=28,
            background="#2c7be5",
            foreground="white",
            borderwidth=2,
            date_pattern="dd/MM/yyyy",
            locale="es_ES",
            font=AppStyle.FONTS["subtitulo"],
        )
        self.cal_fecha.pack(fill="x", pady=(0, 10), ipady=4)

        # --- Correo ---
        self.lbl_correo = tk.Label(col_izquierda, text="CORREO INST.", font=("Helvetica", 9, "bold"),
                              bg=AppStyle.COLORS["panel"], fg="#5a6a7a")
        self.lbl_correo.pack(anchor="w", pady=(5, 0))
        self.ent_correo = tk.Entry(col_izquierda, textvariable=self.vars["correo_institucional"])
        AppStyle.estilo_entrada(self.ent_correo)
        self.ent_correo.pack(fill="x", pady=(0, 2), ipady=4)
        self.lbl_error_correo = tk.Label(col_izquierda, text="", font=("Helvetica", 7, "italic"),
                                          bg=AppStyle.COLORS["panel"], fg="#e74c3c")
        self.lbl_error_correo.pack(anchor="w", pady=(0, 4))

        # --- Teléfono ---
        self.lbl_telefono = tk.Label(col_izquierda, text="TELEFONO", font=("Helvetica", 9, "bold"),
                                bg=AppStyle.COLORS["panel"], fg="#5a6a7a")
        self.lbl_telefono.pack(anchor="w", pady=(5, 0))
        self.ent_telefono = tk.Entry(col_izquierda, textvariable=self.vars["telefono"])
        AppStyle.estilo_entrada(self.ent_telefono)
        self.ent_telefono.pack(fill="x", pady=(0, 2), ipady=4)
        self.lbl_error_telefono = tk.Label(col_izquierda, text="", font=("Helvetica", 7, "italic"),
                                            bg=AppStyle.COLORS["panel"], fg="#e74c3c")
        self.lbl_error_telefono.pack(anchor="w", pady=(0, 4))

        # --- Dirección ---
        self.lbl_direccion = tk.Label(col_izquierda, text="DIRECCION", font=("Helvetica", 9, "bold"),
                                 bg=AppStyle.COLORS["panel"], fg="#5a6a7a")
        self.lbl_direccion.pack(anchor="w", pady=(5, 0))
        self.ent_direccion = tk.Entry(col_izquierda, textvariable=self.vars["direccion"])
        AppStyle.estilo_entrada(self.ent_direccion)
        self.ent_direccion.pack(fill="x", pady=(0, 2), ipady=4)
        self.lbl_error_direccion = tk.Label(col_izquierda, text="", font=("Helvetica", 7, "italic"),
                                             bg=AppStyle.COLORS["panel"], fg="#e74c3c")
        self.lbl_error_direccion.pack(anchor="w", pady=(0, 4))

        # --- Carrera ---
        self.lbl_carrera = tk.Label(col_izquierda, text="CARRERA", font=("Helvetica", 9, "bold"),
                               bg=AppStyle.COLORS["panel"], fg="#5a6a7a")
        self.lbl_carrera.pack(anchor="w", pady=(5, 0))
        self.ent_carrera = tk.Entry(col_izquierda, textvariable=self.vars["carrera"])
        AppStyle.estilo_entrada(self.ent_carrera)
        self.ent_carrera.pack(fill="x", pady=(0, 2), ipady=4)
        self.lbl_error_carrera = tk.Label(col_izquierda, text="", font=("Helvetica", 7, "italic"),
                                           bg=AppStyle.COLORS["panel"], fg="#e74c3c")
        self.lbl_error_carrera.pack(anchor="w", pady=(0, 4))

        # --- Semestre ---
        self.lbl_semestre = tk.Label(col_izquierda, text="SEMESTRE", font=("Helvetica", 9, "bold"),
                                bg=AppStyle.COLORS["panel"], fg="#5a6a7a")
        self.lbl_semestre.pack(anchor="w", pady=(5, 0))
        self.ent_semestre = tk.Entry(col_izquierda, textvariable=self.vars["semestre"])
        AppStyle.estilo_entrada(self.ent_semestre)
        self.ent_semestre.pack(fill="x", pady=(0, 2), ipady=4)
        self.lbl_error_semestre = tk.Label(col_izquierda, text="", font=("Helvetica", 7, "italic"),
                                            bg=AppStyle.COLORS["panel"], fg="#e74c3c")
        self.lbl_error_semestre.pack(anchor="w", pady=(0, 4))

        # 2. COLUMNA DERECHA (Imagen y Botón)
        col_derecha = tk.Frame(cuerpo, bg=AppStyle.COLORS["panel"], width=250)
        col_derecha.pack(side="right", fill="both", padx=(10, 0))

        # --- Espacio para la Imagen ---
        self.lbl_foto = tk.Label(
            col_derecha,
            text="[IMAGE A SUBIR]",
            font=AppStyle.FONTS["subtitulo"],
            bg="#e0e6ed",
            fg=AppStyle.COLORS["text_dark"],
            width=300, height=300,
            relief="groove", bd=2
        )
        self.lbl_foto.pack(fill="x", pady=(20, 10))
        self.lbl_foto.config(image=self.img.image_defect())
        self.lbl_foto.bind("<Button-1>", self.tocar_label)

        btn_foto = tk.Button(col_derecha, text="Seleccionar Foto", font=("Helvetica", 9), command=self.tocar_label)  # type: ignore
        btn_foto.pack(fill="x", pady=(0, 20))

        spacer = tk.Frame(col_derecha, bg=AppStyle.COLORS["panel"])
        spacer.pack(expand=True, fill="both")

        self.btn_guardar = tk.Button(
            col_derecha,
            text="GUARDAR",
            command=self._guardar
        )
        AppStyle.estilo_boton(self.btn_guardar)
        self.btn_guardar.config(font=("Helvetica", 12, "bold"), pady=25)
        self.btn_guardar.pack(fill="x", side="bottom", pady=(0, 10))

    def _validar_campos(self) -> bool:
        """
        Valida que todos los campos obligatorios estén llenos.
        Muestra un mensaje de error inline debajo de cada campo vacío.
        Devuelve True si todo es válido, False si hay algún error.
        """
        # Mapa: variable -> (label de error, nombre legible del campo, widget entry)
        campos = [
            (self.vars["nombre"],                self.lbl_error_nombre,          "El nombre no puede estar vacío",           self.ent_nombre),
            (self.vars["identificacion"],         self.lbl_error_identificacion,  "La identificación no puede estar vacía",   self.ent_identificacion),
            (self.vars["correo_institucional"],   self.lbl_error_correo,          "El correo no puede estar vacío",           self.ent_correo),
            (self.vars["telefono"],               self.lbl_error_telefono,        "El teléfono no puede estar vacío",         self.ent_telefono),
            (self.vars["direccion"],              self.lbl_error_direccion,       "La dirección no puede estar vacía",        self.ent_direccion),
            (self.vars["carrera"],                self.lbl_error_carrera,         "La carrera no puede estar vacía",          self.ent_carrera),
            (self.vars["semestre"],               self.lbl_error_semestre,        "El semestre no puede estar vacío",         self.ent_semestre),
        ]

        es_valido = True

        for var, lbl_error, mensaje, entry in campos:
            if not var.get().strip():
                # Mostrar mensaje de error en rojo debajo del campo
                lbl_error.config(text=f"⚠ {mensaje}")
                # Resaltar el borde del entry en rojo
                entry.config(highlightbackground="#e74c3c", highlightcolor="#e74c3c", highlightthickness=1)
                es_valido = False
            else:
                # Limpiar error si ya fue corregido
                lbl_error.config(text="")
                entry.config(highlightthickness=0)

        return es_valido

    def _limpiar_errores(self) -> None:
        """Limpia todos los mensajes de error y resaltados."""
        errores = [
            (self.lbl_error_nombre,         self.ent_nombre),
            (self.lbl_error_identificacion, self.ent_identificacion),
            (self.lbl_error_correo,         self.ent_correo),
            (self.lbl_error_telefono,       self.ent_telefono),
            (self.lbl_error_direccion,      self.ent_direccion),
            (self.lbl_error_carrera,        self.ent_carrera),
            (self.lbl_error_semestre,       self.ent_semestre),
        ]
        for lbl_error, entry in errores:
            lbl_error.config(text="")
            entry.config(highlightthickness=0)

    def _limpiar_formulario(self) -> None:
        """Limpia todos los campos del formulario tras un registro exitoso."""
        for var in self.vars.values():
            if isinstance(var, tk.StringVar):
                var.set("")

        # Restaurar género a Masculino por defecto
        self.genero_var.set("M")

        # Restaurar el calendario a la fecha actual
        self.cal_fecha.set_date(datetime.date.today())

        # Restaurar imagen a la imagen por defecto
        self.ruta_image = "backend/image/perfil_defecto.png"
        self.lbl_foto.config(image=self.img.image_defect())

        # Limpiar todos los mensajes de error
        self._limpiar_errores()

    def _guardar(self) -> None:
        # Primero validar — si hay campos vacíos, no continuar
        if not self._validar_campos():
            return

        try:
            if not self.ruta_image:
                raise ValueError("No se ha seleccionado ninguna imagen.")

            estudiante = self.estudiante_controller.registrar_estudiante(
                nombre=self.vars["nombre"].get(),
                identificacion=self.vars["identificacion"].get(),
                genero_limpio=self.vars["genero"].get(),
                fecha_nacimiento_limpia=self.cal_fecha.get_date().strftime("%d/%m/%Y"),
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

        # Limpiar todo el formulario
        self._limpiar_formulario()

        if self.on_guardado is not None:
            self.on_guardado()

    def tocar_label(self, event=None) -> None:
        ruta = self.img.subir_imagen()
        if not ruta:
            return
        self.ruta_image = ruta
        self.image = self.img.cargar_imagen(ruta)
        self.lbl_foto.config(image=self.image)