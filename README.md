# Sistema de Seguimiento de Salud Escolar

Aplicacion en Python con Programacion Orientada a Objetos y arquitectura de tres capas:

- Front-End: Tkinter
- Back-End: modelos, controladores y DAOs
- Persistencia: archivos JSON

## Estructura

- `main.py`: punto de entrada
- `frontend/`: ventanas de Tkinter
- `backend/models/`: `Persona`, `IEvaluable`, `Estudiante`
- `backend/controllers/`: logica de negocio
- `backend/daos/`: acceso a datos JSON
- `persistence/json_handler.py`: lectura y escritura JSON

## Ejecucion

```bash
python main.py
```

## Funcionalidad

- Registra nombre, identificacion, peso y altura
- Calcula IMC con la formula `peso / altura^2`
- Clasifica el estado nutricional
- Guarda y lee datos en `data/estudiantes.json`
