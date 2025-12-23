from django.db import models
from django.utils import timezone

class Socio(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_inscripcion = models.DateField(default=timezone.localdate)

    def __str__(self):
        return f"{self.nombre} - {self.email}"


class Entrenador(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    entrenador = models.ForeignKey(
        Entrenador,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    horario = models.CharField(max_length=50)
    cupo = models.PositiveIntegerField(default=20)

    def __str__(self):
        return f"{self.nombre} ({self.horario})"
