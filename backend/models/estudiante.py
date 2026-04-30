from __future__ import annotations

from dataclasses import dataclass

from backend.models.evaluable import IEvaluable
from backend.models.persona import Persona


@dataclass
class Estudiante(Persona, IEvaluable):
    # Herencia: Estudiante extiende Persona e implementa IEvaluable.
    peso: float
    altura: float

    def obtener_tipo(self) -> str:
        return "Estudiante"

    def calcular_imc(self) -> float:
        if self.altura <= 0:
            raise ValueError("La altura debe ser mayor que cero.")
        if self.peso <= 0:
            raise ValueError("El peso debe ser mayor que cero.")
        return self.peso / (self.altura ** 2)

    def clasificar_nutricion(self) -> str:
        imc = self.calcular_imc()
        if imc < 18.5:
            return "Bajo peso"
        if imc < 25:
            return "Peso normal"
        if imc < 30:
            return "Sobrepeso"
        return "Obesidad"

    def to_dict(self) -> dict[str, object]:
        return {
            "nombre": self.nombre,
            "identificacion": self.identificacion,
            "peso": self.peso,
            "altura": self.altura,
        }

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "Estudiante":
        return cls(
            nombre=str(data["nombre"]),
            identificacion=str(data["identificacion"]),
            peso=float(data["peso"]),
            altura=float(data["altura"]),
        )
