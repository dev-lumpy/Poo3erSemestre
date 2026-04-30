from __future__ import annotations

from backend.models.estudiante import Estudiante


class SaludDAO:
    def construir_resumen(self, estudiante: Estudiante) -> dict[str, object]:
        return {
            "nombre": estudiante.nombre,
            "identificacion": estudiante.identificacion,
            "peso": estudiante.peso,
            "altura": estudiante.altura,
            "imc": round(estudiante.calcular_imc(), 2),
            "clasificacion": estudiante.clasificar_nutricion(),
        }
