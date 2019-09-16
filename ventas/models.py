from django.db import models
from django.db.models import signals
from productos.models import Producto
from clientes.models import Cliente


class TimeStampModel(models.Model):
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class CabeceraVenta(TimeStampModel):
    ruc = models.CharField(max_length=10, unique=True)
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ruc


class DetalleVenta(models.Model):
    list_id = models.ForeignKey(CabeceraVenta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()


def update_stock(sender, instance, **kwargs):
    instance.producto.stock -= instance.cantidad
    instance.producto.save()


# register the signal
signals.post_save.connect(update_stock, sender=DetalleVenta, dispatch_uid="update_stock_count")
