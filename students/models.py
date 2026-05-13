from django.db import models

# Modelo que representa a un estudiante
class Student(models.Model):
    # Identificador único del estudiante (código institucional)
    code = models.CharField(max_length=20, unique=True)

    # Datos personales básicos
    first_name = models.CharField(max_length=100)  # Nombre(s)
    last_name = models.CharField(max_length=100)   # Apellido(s)
    career = models.CharField(max_length=100)      # Carrera que estudia
    semester = models.IntegerField()               # Semestre actual (1 al 12 generalmente)

    # Fecha de nacimiento (opcional)
    birth_date = models.DateField(null=True, blank=True)

    # Género con opciones predefinidas
    gender = models.CharField(
        max_length=10,
        choices=[
            ("M", "Masculino"),
            ("F", "Femenino"),
            ("O", "Otro"),
        ],
        null=True,
        blank=True
    )

    # Correo institucional (debe ser único)
    institutional_email = models.EmailField(unique=True, null=True, blank=True)

    # Número de teléfono de contacto
    phone = models.CharField(max_length=20, null=True, blank=True)

    # Dirección de residencia
    address = models.TextField(null=True, blank=True)

    # Foto de perfil (se guarda en media/students/photos/)
    profile_photo = models.ImageField(
        upload_to="students/photos/",
        null=True,
        blank=True
    )

    # Representación legible del objeto en el admin y shell
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Modelo que almacena información médica del estudiante
class HealthRecord(models.Model):
    # Relación uno a uno con Student (cada estudiante tiene un solo registro)
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE  # Si el estudiante se elimina, también su registro médico
    )

    # Datos médicos principales
    blood_type = models.CharField(max_length=5)          # Tipo de sangre (ej: A+, O-, etc.)
    allergies = models.TextField(blank=True)             # Alergias conocidas
    chronic_diseases = models.TextField(blank=True)      # Enfermedades crónicas
    emergency_contact = models.CharField(max_length=100) # Nombre de contacto de emergencia

    # Datos físicos opcionales
    weight = models.FloatField(null=True, blank=True)    # Peso en kg
    height = models.FloatField(null=True, blank=True)    # Altura en metros

    # Fecha de última actualización del registro (se actualiza automáticamente)
    last_updated = models.DateTimeField(auto_now=True)

    # Observaciones adicionales sobre salud
    observations = models.TextField(blank=True)

    # Representación legible del objeto
    def __str__(self):
        return f"Registro médico de {self.student}"