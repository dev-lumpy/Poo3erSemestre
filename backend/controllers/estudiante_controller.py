from __future__ import annotations

from backend.daos.estudiante_dao import EstudianteDAO
from backend.models.estudiante import Estudiante


class ControlEstudiante:
    def __init__(self, estudiante_dao: EstudianteDAO | None = None) -> None:
        self.estudiante_dao = estudiante_dao or EstudianteDAO()

    def registrar_estudiante(
        self,
        nombre: str,
        identificacion: str,
        genero_limpio: str,
        fecha_nacimiento_limpia: str,
        correo_institucional_limpio: str,
        telefono_limpio: str,
        direccion_limpia: str,
        matricula_limpia: str,
        carrera_limpia: str,
        semestre_limpio: str,
        image: str
    ) -> Estudiante:
        nombre_limpio = nombre.strip()
        identificacion_limpia = identificacion.strip()

        if not nombre_limpio:
            raise ValueError("El nombre es obligatorio.")
        if not identificacion_limpia:
            raise ValueError("La identificacion es obligatoria.")

        estudiante = Estudiante(
            nombre=nombre_limpio,
            identificacion=identificacion_limpia,
            genero=genero_limpio,
            fecha_nacimiento=fecha_nacimiento_limpia,
            correo_institucional=correo_institucional_limpio,
            telefono=telefono_limpio,
            direccion=direccion_limpia,

            # Si es Estudiante, añade estos:
            matricula=matricula_limpia,
            carrera=carrera_limpia,
            semestre=semestre_limpio,

            # Algunos datos adicionales:
            peso=0.0,
            altura=0.0,
            image=image
        )
        self.estudiante_dao.guardar(estudiante)
        return estudiante

    def listar_estudiantes(self) -> list[Estudiante]:
        return self.estudiante_dao.listar()
    
    def buscar_estudiante(self, query: str) -> Estudiante | None:
        """Busca un estudiante por nombre o ID (identificación)."""
        query_lower = query.lower().strip()
        estudiantes = self.listar_estudiantes()
        
        # Primero intenta buscar por ID exacto
        for est in estudiantes:
            if est.identificacion.lower() == query_lower:
                return est
        
        # Luego intenta buscar por nombre (parcial)
        for est in estudiantes:
            if query_lower in est.nombre.lower():
                return est
        
        return None
