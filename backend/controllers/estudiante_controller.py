from __future__ import annotations

from backend.daos.estudiante_dao import EstudianteDAO
from backend.models.estudiante import Estudiante


class EstudianteController:
    def __init__(self, estudiante_dao: EstudianteDAO | None = None) -> None:
        self.estudiante_dao = estudiante_dao or EstudianteDAO()

    def registrar_estudiante(
        self,
        nombre: str,
        identificacion: str,
        peso: float,
        altura: float,
    ) -> Estudiante:
        nombre_limpio = nombre.strip()
        identificacion_limpia = identificacion.strip()

        if not nombre_limpio:
            raise ValueError("El nombre es obligatorio.")
        if not identificacion_limpia:
            raise ValueError("La identificacion es obligatoria.")
        if peso <= 0:
            raise ValueError("El peso debe ser mayor que cero.")
        if altura <= 0:
            raise ValueError("La altura debe ser mayor que cero.")

        estudiante = Estudiante(
            nombre=nombre_limpio,
            identificacion=identificacion_limpia,
            peso=peso,
            altura=altura,
        )
        self.estudiante_dao.guardar(estudiante)
        return estudiante

    def listar_estudiantes(self) -> list[Estudiante]:
        return self.estudiante_dao.listar()
