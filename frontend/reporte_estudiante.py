
from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from typing import cast, Any
import logging
from PIL import Image, ImageTk
from pathlib import Path

logger = logging.getLogger(__name__)


class ReporteEstudiante(tk.Toplevel):
    def __init__(self, parent: tk.Misc, estudiante) -> None:
        super().__init__(parent)
        self.title(f"Perfil de {estudiante.nombre}")
        self.geometry("600x750")
        self.estudiante = estudiante
        
        self.transient(cast(Any, parent))
        self.grab_set()
        
        self._crear_widgets()
    
    def _crear_widgets(self) -> None:
        """Crea la interfaz elegante con toda la información del estudiante."""
        logger.debug(f"Creando perfil para {self.estudiante.nombre}")
        
        # Contenedor principal con scroll
        main_frame = ttk.Frame(self)
        main_frame.pack(fill="both", expand=True, padx=0, pady=0)
        
        # ===== HEADER CON IMAGEN Y NOMBRE =====
        header_frame = ttk.Frame(main_frame, relief="flat")
        header_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        # Foto de perfil
        try:
            img_path = self.estudiante.image
            if Path(img_path).exists():
                img = Image.open(img_path)
                img.thumbnail((120, 120))
                self.photo = ImageTk.PhotoImage(img)
                img_label = tk.Label(header_frame, image=self.photo, bg="#f0f0f0", relief="solid", bd=2)
            else:
                img_label = tk.Label(header_frame, text="📷", font=("Arial", 48), bg="#f0f0f0", width=8, height=3)
            img_label.pack(pady=(0, 15))
        except Exception as e:
            logger.warning(f"No se pudo cargar imagen: {e}")
            img_label = tk.Label(header_frame, text="📷", font=("Arial", 48), bg="#f0f0f0", width=8, height=3)
            img_label.pack(pady=(0, 15))
        
        # Nombre
        nombre_label = tk.Label(header_frame, text=self.estudiante.nombre, font=("Segoe UI", 18, "bold"))
        nombre_label.pack()
        
        # Identificación
        id_label = tk.Label(header_frame, text=self.estudiante.identificacion, font=("Segoe UI", 10), fg="#666")
        id_label.pack()
        
        # Separador
        ttk.Separator(main_frame, orient="horizontal").pack(fill="x", padx=20, pady=10)
        
        # ===== INFORMACIÓN PERSONAL =====
        self._crear_seccion(main_frame, "👤 INFORMACIÓN PERSONAL", [
            ("Nombre", self.estudiante.nombre),
            ("Identificación", self.estudiante.identificacion),
            ("Género", self.estudiante.genero or "No especificado"),
            ("Fecha de Nacimiento", self.estudiante.fecha_nacimiento),
        ])
        
        # ===== INFORMACIÓN DE CONTACTO =====
        self._crear_seccion(main_frame, "📞 CONTACTO", [
            ("Correo Institucional", self.estudiante.correo_institucional),
            ("Teléfono", self.estudiante.telefono),
            ("Dirección", self.estudiante.direccion),
        ])
        
        # ===== INFORMACIÓN ACADÉMICA =====
        self._crear_seccion(main_frame, "🎓 INFORMACIÓN ACADÉMICA", [
            ("Carrera", self.estudiante.carrera),
            ("Semestre", self.estudiante.semestre),
            ("Matrícula", self.estudiante.matricula or "No especificada"),
        ])
        
        # ===== INFORMACIÓN DE SALUD =====
        try:
            imc = self.estudiante.calcular_imc()
            clasificacion = self.estudiante.clasificar_nutricion()
            imc_color = self._obtener_color_imc(clasificacion)
        except Exception:
            imc = "N/A"
            clasificacion = "No calculable"
            imc_color = "#888"
        
        self._crear_seccion(main_frame, "⚕️ INFORMACIÓN DE SALUD", [
            ("Peso", f"{self.estudiante.peso} kg"),
            ("Altura", f"{self.estudiante.altura} m"),
            ("IMC", f"{imc:.2f}" if isinstance(imc, float) else imc),
            ("Clasificación", clasificacion),
        ], imc_color if clasificacion != "No calculable" else None)
    
    def _crear_seccion(self, parent, titulo, datos, color_especial=None):
        """Crea una sección con título y pares clave-valor."""
        seccion_frame = ttk.LabelFrame(parent, text=titulo, padding=15)
        seccion_frame.pack(fill="x", padx=20, pady=10)
        
        for clave, valor in datos:
            row_frame = ttk.Frame(seccion_frame)
            row_frame.pack(fill="x", pady=5)
            
            # Etiqueta
            label_key = tk.Label(row_frame, text=f"{clave}:", font=("Segoe UI", 10, "bold"), width=20, anchor="w")
            label_key.pack(side="left")
            
            # Valor
            valor_text = str(valor) if valor else "No especificado"
            label_value = tk.Label(row_frame, text=valor_text, font=("Segoe UI", 10), fg="#333")
            label_value.pack(side="left", fill="x", expand=True)
    
    def _obtener_color_imc(self, clasificacion):
        """Retorna un color basado en la clasificación nutricional."""
        colores = {
            "Bajo peso": "#3498db",      # Azul
            "Peso normal": "#2ecc71",    # Verde
            "Sobrepeso": "#f39c12",      # Naranja
            "Obesidad": "#e74c3c",       # Rojo
        }
        return colores.get(clasificacion, "#888")
