from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class JsonHandler:
    def __init__(self, file_path: str | Path) -> None:
        self.file_path = Path(file_path)

    def leer(self) -> list[dict[str, Any]]:
        if not self.file_path.exists():
            return []

        with self.file_path.open("r", encoding="utf-8") as archivo:
            contenido = json.load(archivo)

        if isinstance(contenido, list):
            return contenido
        if isinstance(contenido, dict) and "estudiantes" in contenido:
            registros = contenido["estudiantes"]
            if isinstance(registros, list):
                return registros
        return []

    def escribir(self, datos: list[dict[str, Any]]) -> None:
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        with self.file_path.open("w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)
