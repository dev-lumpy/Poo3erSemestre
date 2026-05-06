import tkinter as tk
from .styles import AppStyle

class BaseVentana(tk.Tk): # O Toplevel si son secundarias
    def __init__(self, titulo):
        super().__init__()
        self.title(titulo)
        self.configure(bg=AppStyle.COLORS["bg"])
        self.resizable(False, False)

        # Contenedor central automático
        self.main_frame = tk.Frame(self)
        AppStyle.estilo_panel(self.main_frame)
        self.main_frame.grid(row=0, column=0, padx=30, pady=30, sticky="nsew")

    def crear_titulo(self, texto, icono="🎓"):
        lbl = tk.Label(
            self.main_frame, 
            text=f"{icono}  {texto}",
            font=AppStyle.FONTS["titulo"],
            bg=AppStyle.COLORS["panel"],
            fg=AppStyle.COLORS["text_dark"]
        )
        lbl.pack(pady=(0, 20))
        return lbl
