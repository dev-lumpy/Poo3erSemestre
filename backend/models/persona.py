from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Persona(ABC):
    nombre: str
    identificacion: str  # Puede ser el CI
    genero: str          # Útil para estadísticas de salud
    fecha_nacimiento: str # Formato "DD/MM/AAAA"

    @abstractmethod
    def obtener_tipo(self) -> str:
        """Devuelve el tipo concreto de persona."""
