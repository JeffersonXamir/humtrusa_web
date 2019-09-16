from django.db import models

import datetime

TAX_VALUE = 0.12


class Presentacion(models.Model):
    # codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    TIPO = (
        ('industrial', 'Industrial'),
        ('comercial', 'Comercial'),
    )
    lote = models.CharField(max_length=10, unique=True, default=0)
    presentacion = models.ForeignKey(Presentacion, on_delete=models.CASCADE)
    tipo = models.CharField(choices=TIPO, max_length=30)
    nombre = models.CharField(max_length=200, unique=True)
    componente = models.CharField(max_length=200)
    concentracion = models.CharField(max_length=50)
    sanitario = models.CharField(max_length=200)
    fecha_expiracion = models.DateField()
    fecha_produccion = models.DateField()
    descripcion = models.TextField(max_length=400)
    precio_compra = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    precio_venta = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    stock = models.PositiveSmallIntegerField()
    iva = models.DecimalField(max_digits=6, decimal_places=3, default=0.000)
    estado = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    def preciototal(self):
        precio_total = self.precio_compra * self.stock
        return precio_total

    def estadoproducto(self):
        hoy = datetime.date.today()
        dias = (self.fecha_expiracion - hoy).days
        return dias

    def incrementarlote(self, *args, **kwargs):
        if self.lote == 0:
            self.lote += 1
            self.store.save()
        super(Producto, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.precio_venta:
            self.iva = round(float(self.precio_venta) * TAX_VALUE, 3)
            super(Producto, self).save(*args, **kwargs)
        else:
            self.iva = 0
            super(Producto, self).save(*args, **kwargs)
