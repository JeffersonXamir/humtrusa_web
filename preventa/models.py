from django.db import models


class CabVenta(models.Model):
    usuarioNombre = models.CharField(max_length=75)
    fecha = models.DateField()
    estado = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuarioNombre


class DetVenta(models.Model):
    idCabVenta = models.ForeignKey(CabVenta, null=False, blank=False, on_delete=models.CASCADE)
    productoNombre = models.CharField(max_length=75)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    iva = models.DecimalField(max_digits=5, decimal_places=2)
    descuento = models.DecimalField(max_digits=5, decimal_places=2)
    estado = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        cadena = " factura #:{0} del clientes : {1}"

        return cadena.format(self.idCabVenta.id, self.idCabVenta.usuarioNombre)
