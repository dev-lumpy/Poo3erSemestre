from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Persona(ABC):
    # Abstraccion: esta clase define los datos comunes de cualquier persona.
    nombre: str
    identificacion: str

    @abstractmethod
    def obtener_tipo(self) -> str:
        """Devuelve el tipo concreto de persona."""
