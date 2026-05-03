from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

logging.basicConfig(level=logging.INFO)

class JsonHandler:
    def __init__(self, file_path: str | Path) -> None:
        self.file_path = Path(file_path)
        # Aseguramos que la carpeta existe desde el inicio
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    def leer(self) -> list[dict[str, Any]]:
        """Lee el archivo JSON y garantiza que siempre devuelva una lista."""
        if not self.file_path.exists():
            return []
        
        try:
            with self.file_path.open("r", encoding="utf-8") as archivo:
                contenido = json.load(archivo)
            
            # Compatibilidad: Maneja si es lista directa o el formato antiguo con llave "estudiantes"
            if isinstance(contenido, list):
                return contenido
            if isinstance(contenido, dict):
                # Busca cualquier llave que contenga una lista (estudiantes, controles, etc.)
                for llave in contenido:
                    if isinstance(contenido[llave], list):
                        return contenido[llave]
            
            return []
        except (json.JSONDecodeError, ValueError):
            logging.error(f"Error al decodificar {self.file_path}. El archivo está corrupto o vacío.")
            return []

    def escribir(self, datos: list[dict[str, Any]]) -> None:
        """Escribe los datos de forma segura."""
        try:
            # Escribir en un archivo temporal primero evita que se borren datos si el PC se apaga
            temp_path = self.file_path.with_suffix(".tmp")
            with temp_path.open("w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, ensure_ascii=False, indent=4)
            
            # Reemplazo atómico: sobreescribe el original solo si la escritura fue exitosa
            temp_path.replace(self.file_path)
        except Exception as e:
            logging.error(f"No se pudo guardar en {self.file_path}: {e}")

    def agregar_registro(self, nuevo_registro: dict[str, Any]) -> None:
        """Método de conveniencia para no tener que leer y escribir manualmente fuera."""
        registros = self.leer()
        registros.append(nuevo_registro)
        self.escribir(registros)