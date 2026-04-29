import tkinter as tk
from tkinter import font as tkfont


# ── Callbacks ────────────────────────────────────────────────────────────────

def on_registro_estudiantes():
    print("Botón presionado: Registro de Estudiantes")


def on_registro_salud():
    print("Botón presionado: Registro de Control de Salud")


def on_buscar_estudiante():
    texto = entry_buscador.get().strip()
    if texto:
        print(f"Buscando estudiante: {texto}")
    else:
        print("Buscador: ingrese un nombre o ID para buscar")


# ── Ventana principal ─────────────────────────────────────────────────────────

root = tk.Tk()
root.title("Sistema de Gestión de Estudiantes")
root.resizable(False, False)

# Colores y tipografía
BG_COLOR      = "#1e3a5f"   # azul marino oscuro
PANEL_COLOR   = "#f0f4f8"   # gris muy claro
ACCENT_COLOR  = "#2e86de"   # azul medio
BTN_HOVER     = "#1b6ca8"
TEXT_DARK     = "#1e3a5f"
TEXT_LIGHT    = "#ffffff"

root.configure(bg=BG_COLOR)

titulo_font  = tkfont.Font(family="Helvetica", size=18, weight="bold")
subtitulo_font = tkfont.Font(family="Helvetica", size=11)
btn_font     = tkfont.Font(family="Helvetica", size=11, weight="bold")
entry_font   = tkfont.Font(family="Helvetica", size=11)

# ── Contenedor central ────────────────────────────────────────────────────────

frame = tk.Frame(root, bg=PANEL_COLOR, bd=0, relief="flat",
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
    command=on_registro_estudiantes,
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
    command=on_registro_salud,
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
entry_buscador = tk.Entry(
    frame,
    font=entry_font,
    bd=2,
    relief="groove",
    fg=TEXT_DARK,
    insertbackground=TEXT_DARK,
)
entry_buscador.insert(0, "Nombre o ID del estudiante...")
entry_buscador.config(fg="#aaaaaa")

def on_entry_focus_in(event):
    if entry_buscador.get() == "Nombre o ID del estudiante...":
        entry_buscador.delete(0, tk.END)
        entry_buscador.config(fg=TEXT_DARK)

def on_entry_focus_out(event):
    if not entry_buscador.get():
        entry_buscador.insert(0, "Nombre o ID del estudiante...")
        entry_buscador.config(fg="#aaaaaa")

entry_buscador.bind("<FocusIn>", on_entry_focus_in)
entry_buscador.bind("<FocusOut>", on_entry_focus_out)
entry_buscador.bind("<Return>", lambda e: on_buscar_estudiante())

entry_buscador.grid(row=7, column=0, sticky="ew", ipady=8, padx=(0, 8))

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
    command=on_buscar_estudiante,
)
btn_buscar.grid(row=7, column=1, sticky="ew")

# Configurar pesos de columna para que el entry se expanda
frame.columnconfigure(0, weight=3)
frame.columnconfigure(1, weight=1)

# ── Arrancar ──────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    root.mainloop()
