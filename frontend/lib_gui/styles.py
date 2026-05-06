import tkinter as tk

class AppStyle:
    # Paleta de colores
    COLORS = {
        "bg": "#1e3a5f",
        "panel": "#f0f4f8",
        "accent": "#2e86de",
        "hover": "#1b6ca8",
        "text_dark": "#1e3a5f",
        "text_light": "#ffffff",
        "placeholder": "#aaaaaa"
    }

    # Fuentes
    FONTS = {
        "titulo": ("Helvetica", 18, "bold"),
        "subtitulo": ("Helvetica", 11),
        "boton": ("Helvetica", 11, "bold"),
        "entrada": ("Helvetica", 11)
    }

    @staticmethod
    def estilo_boton(btn):
        btn.config(
            font=AppStyle.FONTS["boton"],
            bg=AppStyle.COLORS["accent"],
            fg=AppStyle.COLORS["text_light"],
            activebackground=AppStyle.COLORS["hover"],
            activeforeground=AppStyle.COLORS["text_light"],
            bd=0, padx=20, pady=12, cursor="hand2"
        )

    @staticmethod
    def estilo_panel(frame):
        frame.config(bg=AppStyle.COLORS["panel"], padx=40, pady=35)

    
    @staticmethod
    def estilo_entrada(entry):
        entry.config(
            font=AppStyle.FONTS["entrada"],
            bd=2,
            relief="groove",
            fg=AppStyle.COLORS["text_dark"],
            insertbackground=AppStyle.COLORS["text_dark"]
        )
