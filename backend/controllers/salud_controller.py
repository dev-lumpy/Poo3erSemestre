from __future__ import annotations

from backend.daos.salud_dao import SaludDAO
from backend.models.estudiante import Estudiante


class SaludController:
    def __init__(self, salud_dao: SaludDAO | None = None) -> None:
        self.salud_dao = salud_dao or SaludDAO()

    def obtener_resumen(self, estudiante: Estudiante) -> dict[str, object]:
        return self.salud_dao.construir_resumen(estudiante)

    def obtener_resumenes(self, estudiantes: list[Estudiante]) -> list[dict[str, object]]:
        return [self.obtener_resumen(estudiante) for estudiante in estudiantes]
