from __future__ import annotations

from abc import ABC, abstractmethod


class IEvaluable(ABC):
    # Interfaz: obliga a implementar los calculos de salud en las clases hijas.

    @abstractmethod
    def calcular_imc(self) -> float:
        """Calcula el indice de masa corporal."""

    @abstractmethod
    def clasificar_nutricion(self) -> str:
        """Clasifica el estado nutricional segun el IMC."""
