from django.db import models


class Laboratorio(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=40)
    sanitario = models.CharField(max_length=50)
    autorizacion = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
