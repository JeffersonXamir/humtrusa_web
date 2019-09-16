from django.db.models import signals
from django.db import models
from django.conf import settings
from clientes.models import Cliente
from productos.models import Producto


class Factura(models.Model):
    serie = models.IntegerField()
    numero = models.CharField(max_length=6)
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    vendedor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        # no duplicate serie y numero juntos
        unique_together = (('serie', 'numero'),)

    def __str__(self):
        return U" %s- %s" % (self.serie, self.numero)


class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura, db_column='factura_id', related_name='factura', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, db_column='producto_id', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=40)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    cantidad = models.IntegerField()
    impuesto = models.DecimalField(max_digits=6, decimal_places=2)
    subtotal = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return u'%s' % self.descripcion

    def suma(self):
        return self.cantidad * self.producto.precio_venta


def update_stock(sender, instance, **kwargs):
    instance.producto.stock -= instance.cantidad
    instance.producto.save()


# register the signal
signals.post_save.connect(update_stock, sender=DetalleFactura, dispatch_uid="update_stock_count")
