from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypedDict

class EstudianteData(TypedDict):
    nombre: str
    identificacion: str
    genero: str
    fecha_nacimiento: str
    correo_institucional: str
    telefono: str
    direccion: str
    peso: float
    altura: float

@dataclass
class Persona(ABC):
    nombre: str
    identificacion: str   # CI o DNI
    genero: str           # "M", "F", "Otro"
    fecha_nacimiento: str # "DD/MM/AAAA"

    # --- Datos de contacto universitarios ---
    correo_institucional: str
    telefono: str
    direccion: str

    @abstractmethod
    def obtener_tipo(self) -> str:
        """Devuelve si es 'Estudiante', 'Docente' o 'Administrativo'."""
        pass

    def calcular_edad(self, anio_actual: int = 2026) -> int:
        """Un pequeño extra útil para reportes de salud."""
        anio_nac = int(self.fecha_nacimiento.split("/")[-1])
        return anio_actual - anio_nac
 
