from __future__ import annotations

from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import font as tkfont

# Colores y tipografía
BG_COLOR      = "#1e3a5f"   # azul marino oscuro
PANEL_COLOR   = "#f0f4f8"   # gris muy claro
ACCENT_COLOR  = "#2e86de"   # azul medio
BTN_HOVER     = "#1b6ca8"
TEXT_DARK     = "#1e3a5f"
TEXT_LIGHT    = "#ffffff"

# ── Ventana principal ─────────────────────────────────────────────────────────
class StyleMainGUI(ABC):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema de Gestión de Estudiantes")
        self.root.resizable(False, False)

        self.root.configure(bg=BG_COLOR)

        titulo_font  = tkfont.Font(family="Helvetica", size=18, weight="bold")
        subtitulo_font = tkfont.Font(family="Helvetica", size=11)
        btn_font     = tkfont.Font(family="Helvetica", size=11, weight="bold")
        entry_font   = tkfont.Font(family="Helvetica", size=11)

        # ── Contenedor central ────────────────────────────────────────────────────────

        frame = tk.Frame(self.root, bg=PANEL_COLOR, bd=0, relief="flat",
                        padx=40, pady=35)
        frame.grid(row=0, column=0, padx=30, pady=30, sticky="nsew")

        # Fila 0 — Título
        lbl_titulo = tk.Label(
            frame,
            text="🎓  Sistema de Gestión de Estudiantes",
            font=titulo_font,
            bg=PANEL_COLOR,
            fg=TEXT_DARK,
        )
        lbl_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 6))

        # Fila 1 — Sub-título / descripción
        lbl_sub = tk.Label(
            frame,
            text="Seleccione una opción o busque un estudiante",
            font=subtitulo_font,
            bg=PANEL_COLOR,
            fg="#5a6a7a",
        )
        lbl_sub.grid(row=1, column=0, columnspan=2, pady=(0, 25))

        # Separador visual
        sep = tk.Frame(frame, bg=ACCENT_COLOR, height=2)
        sep.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, 25))

        # Fila 3 — Botón Registro de Estudiantes
        btn_estudiantes = tk.Button(
            frame,
            text="📋  Registro de Estudiantes",
            font=btn_font,
            bg=ACCENT_COLOR,
            fg=TEXT_LIGHT,
            activebackground=BTN_HOVER,
            activeforeground=TEXT_LIGHT,
            bd=0,
            padx=20,
            pady=12,
            cursor="hand2",
            command=self.abrir_registro_de_estudiantes,
        )
        btn_estudiantes.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(0, 12))

        # Fila 4 — Botón Registro de Control de Salud
        btn_salud = tk.Button(
            frame,
            text="🏥  Registro de Control de Salud",
            font=btn_font,
            bg=ACCENT_COLOR,
            fg=TEXT_LIGHT,
            activebackground=BTN_HOVER,
            activeforeground=TEXT_LIGHT,
            bd=0,
            padx=20,
            pady=12,
            cursor="hand2",
            command=self.abrir_registro_de_control_de_salud,
        )
        btn_salud.grid(row=4, column=0, columnspan=2, sticky="ew", pady=(0, 25))

        # Separador visual
        sep2 = tk.Frame(frame, bg=ACCENT_COLOR, height=2)
        sep2.grid(row=5, column=0, columnspan=2, sticky="ew", pady=(0, 18))

        # Fila 6 — Etiqueta del buscador
        lbl_buscar = tk.Label(
            frame,
            text="🔍  Buscador de Estudiante",
            font=btn_font,
            bg=PANEL_COLOR,
            fg=TEXT_DARK,
        )
        lbl_buscar.grid(row=6, column=0, columnspan=2, sticky="w", pady=(0, 6))

        # Fila 7 — Entry + Botón Buscar (en dos columnas)
        self.entry_buscador = tk.Entry(
            frame,
            font=entry_font,
            bd=2,
            relief="groove",
            fg=TEXT_DARK,
            insertbackground=TEXT_DARK,
        )
        self.entry_buscador.insert(0, "Nombre o ID del estudiante...")
        self.entry_buscador.config(fg="#aaaaaa")


        self.entry_buscador.bind("<FocusIn>", self.on_entry_focus_in)
        self.entry_buscador.bind("<FocusOut>", self.on_entry_focus_out)
        self.entry_buscador.bind("<Return>", lambda e: self.abrir_busqueda_estudiante())

        self.entry_buscador.grid(row=7, column=0, sticky="ew", ipady=8, padx=(0, 8))

        btn_buscar = tk.Button(
            frame,
            text="Buscar",
            font=btn_font,
            bg=ACCENT_COLOR,
            fg=TEXT_LIGHT,
            activebackground=BTN_HOVER,
            activeforeground=TEXT_LIGHT,
            bd=0,
            padx=16,
            pady=8,
            cursor="hand2",
            command=self.abrir_busqueda_estudiante,
        )
        btn_buscar.grid(row=7, column=1, sticky="ew")

        # Configurar pesos de columna para que el entry se expanda
        frame.columnconfigure(0, weight=3)
        frame.columnconfigure(1, weight=1)

    def on_entry_focus_in(self, event):
        if self.entry_buscador.get() == "Nombre o ID del estudiante...":
            self.entry_buscador.delete(0, tk.END)
            self.entry_buscador.config(fg=TEXT_DARK)

    def on_entry_focus_out(self, event):
        if not self.entry_buscador.get():
            self.entry_buscador.insert(0, "Nombre o ID del estudiante...")
            self.entry_buscador.config(fg="#aaaaaa")

    # ── Callbacks para botones ───────────────────────────────────────────────────
    @abstractmethod
    def abrir_registro_de_estudiantes(self):
        # Este método se sobrescribirá en main_gui.py para abrir la ventana de registro de estudiantes
        pass

    @abstractmethod
    def abrir_registro_de_control_de_salud(self):
        # Este método se sobrescribirá en main_gui.py para abrir la ventana de registro de control de salud
        pass


    @abstractmethod
    def abrir_busqueda_estudiante(self):
        return self.entry_buscador.get()
