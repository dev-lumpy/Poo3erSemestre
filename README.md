
# Sistema de Seguimiento de Salud Escolar

Aplicación en Python con Programación Orientada a Objetos y arquitectura de tres capas:

- **Front-End:** Tkinter (interfaz gráfica)
- **Back-End:** Modelos, controladores y DAOs
- **Persistencia:** Archivos JSON

---

## Instalación y Ejecución

1. **Requisitos previos:**
	- Python 3.8 o superior
	- [Tkinter](https://docs.python.org/3/library/tkinter.html) (incluido en la mayoría de instalaciones de Python)

2. **Instalar dependencias:**
	Si tienes un archivo `requirements.txt`, ejecuta:
	```bash
	pip install -r requirements.txt
	```
	Si no hay dependencias externas, puedes continuar directamente.

3. **Ejecutar la aplicación:**
	Desde la raíz del proyecto, ejecuta:
	```bash
	python main.py
	```

---

## ¿Cómo usar el programa?

1. **Pantalla principal:**
	- Verás botones para registrar estudiantes, registrar control de salud y buscar estudiantes.

2. **Registrar estudiante:**
	- Haz clic en "Registro de Estudiantes" para agregar un nuevo estudiante con nombre, identificación, peso y altura.

3. **Registrar control de salud:**
	- Haz clic en "Registro de Control de Salud" para ingresar datos de salud (en desarrollo).

4. **Buscar estudiante:**
	- Usa el buscador para encontrar estudiantes por nombre o ID.

5. **Ver reportes:**
	- Accede a los reportes de estudiantes registrados y su estado nutricional.

---

## Estructura del Proyecto

- `main.py`: Punto de entrada
- `frontend/`: Ventanas de Tkinter
- `backend/models/`: Modelos como `Persona`, `IEvaluable`, `Estudiante`
- `backend/controllers/`: Lógica de negocio
- `backend/daos/`: Acceso a datos JSON
- `persistence/json_handler.py`: Lectura y escritura de archivos JSON
- `data/estudiantes.json`: Base de datos de estudiantes

---

## Funcionalidad

- Registrar nombre, identificación, peso y altura
- Calcular IMC con la fórmula `peso / altura^2`
- Clasificar el estado nutricional
- Guardar y leer datos en `data/estudiantes.json`

---

## Soporte

Si tienes problemas para ejecutar el programa:
- Verifica que tienes Python instalado: `python --version`
- Si falta Tkinter, instálalo según tu sistema operativo ([ver guía](https://tkdocs.com/tutorial/install.html))
- Si tienes dudas, revisa el código o consulta con el desarrollador.
