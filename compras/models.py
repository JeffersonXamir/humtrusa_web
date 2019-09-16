from django.db.models import signals
from django.db import models
from django.conf import settings
from proveedor.models import Proveedor
from laboratorio.models import Laboratorio
from productos.models import Producto


class TimeStampModel(models.Model):
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class CabeceraCompra(TimeStampModel):
    trabajador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=10, unique=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.codigo


class DetalleCompra(models.Model):
    list = models.ForeignKey(CabeceraCompra, related_name='cabecera', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def suma(self):
        return self.cantidad * self.producto.precio_compra

    def __str__(self):
        return str(self.producto)


def update_stock(sender, instance, **kwargs):
    instance.producto.stock += instance.cantidad
    instance.producto.save()


# register the signal
signals.post_save.connect(update_stock, sender=DetalleCompra, dispatch_uid="update_stock_count")
