from __future__ import annotations

from pathlib import Path

from backend.models.estudiante import Estudiante
from persistence.json_handler import JsonHandler


class EstudianteDAO:
    def __init__(self, json_handler: JsonHandler | None = None) -> None:
        ruta = Path("data") / "estudiantes.json"
        self.json_handler = json_handler or JsonHandler(ruta)

    def listar(self) -> list[Estudiante]:
        return [Estudiante.from_dict(item) for item in self.json_handler.leer()]

    def guardar(self, estudiante: Estudiante) -> None:
        estudiantes = self.json_handler.leer()
        estudiantes = [
            item for item in estudiantes if str(item.get("identificacion")) != estudiante.identificacion
        ]
        estudiantes.append(estudiante.to_dict())
        self.json_handler.escribir(estudiantes)

    def buscar_por_identificacion(self, identificacion: str) -> Estudiante | None:
        for estudiante in self.listar():
            if estudiante.identificacion == identificacion:
                return estudiante
        return None
