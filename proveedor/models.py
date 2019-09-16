from django.db import models


class Proveedor(models.Model):
    nombre = models.CharField(max_length=20)
    ruc = models.CharField(unique=True, max_length=13)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=60)
    estado = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
