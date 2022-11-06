from django.db import models

# Create your models here.

class Equipo(models.Model):
    nombre = models.CharField("Nombre", max_length=200)
    ciudad = models.CharField("Ciudad", max_length=200)
    titulos = models.CharField("Títulos", max_length=200)

    def __str__(self):
        return self.nombre