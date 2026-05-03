from __future__ import annotations

from dataclasses import dataclass
import logging

from backend.models.evaluable import IEvaluable
from backend.models.persona import Persona

# Configuramos un logger para este módulo específico
logger = logging.getLogger(__name__)

@dataclass
class Estudiante(Persona, IEvaluable):
    peso: float
    altura: float

    def obtener_tipo(self) -> str:
        return "Estudiante"

    def calcular_imc(self) -> float:
        """Calcula el IMC con manejo de errores para evitar el 'cabum'."""
        try:
            if self.altura <= 0 or self.peso <= 0:
                raise ValueError(f"Valores inválidos: Peso={self.peso}, Altura={self.altura}")
            
            return self.peso / (self.altura ** 2)
            
        except Exception as e:
            # Aquí te avisa exactamente qué salió mal en el cálculo
            logger.error(f"Error crítico calculando IMC para {self.nombre}: {e}")
            raise # Volvemos a lanzar el error para que la GUI pueda mostrar un mensaje

    def clasificar_nutricion(self) -> str:
        try:
            imc = self.calcular_imc()
            if imc < 18.5: return "Bajo peso"
            if imc < 25: return "Peso normal"
            if imc < 30: return "Sobrepeso"
            return "Obesidad"
        except Exception:
            return "Error en clasificación"

    def to_dict(self) -> dict[str, object]:
        return {
            "nombre": self.nombre,
            "identificacion": self.identificacion,
            "peso": self.peso,
            "altura": self.altura,
        }

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "Estudiante":
        """
        Punto crítico: Aquí es donde suele fallar si el JSON tiene basura.
        """
        try:
            return cls(
                nombre=str(data["nombre"]),
                identificacion=str(data["identificacion"]),
                peso=float(data.get("peso", 0)),
                altura=float(data.get("altura", 0)),
            )
        except KeyError as e:
            logger.error(f"¡CABUM! Falta un campo obligatorio en el JSON: {e}")
            raise
        except ValueError as e:
            logger.error(f"¡CABUM! El JSON tiene datos que no son números: {e}")
            raise
        except Exception as e:
            logger.error(f"Error inesperado al reconstruir Estudiante: {e}")
            raise
