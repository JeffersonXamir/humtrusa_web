from django.db import models


class Cliente(models.Model):
    cedula = models.CharField(unique=True, max_length=13)
    nombre = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField(verbose_name='Telefono')

    def __str__(self):
        return self.nombre
