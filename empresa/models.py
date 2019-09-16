from django.db import models


class Empresa(models.Model):
    nombre = models.CharField(max_length=75)
    direccion = models.CharField(max_length=75)
    telefono = models.CharField(max_length=75)
    ruc = models.CharField(max_length=75)
    estado = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.nombre


class Usuario(models.Model):
    cedula = models.CharField(max_length=75)
    nombre = models.CharField(max_length=75)
    apellido = models.CharField(max_length=75)
    telefono = models.CharField(max_length=75)
    direccion = models.CharField(max_length=75)
    correo = models.CharField(max_length=75)
    password = models.CharField(max_length=75)
    tipoUsuario = models.CharField(max_length=75)
    estado = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        cadena = "{0} {1}"

        return cadena.format(self.nombre, self.apellido)


class Roles(models.Model):
    nombre = models.CharField(max_length=75)
    estado = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.nombre


class RelacionRolesUsuario(models.Model):
    idRoles = models.ForeignKey(Roles, null=False, blank=False, on_delete=models.CASCADE)
    idUsuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        cadena = "{0} : {1}"

        return cadena.format(self.idRoles.nombre, self.idUsuario.nombre)


class Producto(models.Model):
    nombre = models.CharField(max_length=75)
    #precioCompra = models.DecimalField(max_digits=5, decimal_places=2)
    precioVenta = models.DecimalField(max_digits=5, decimal_places=2)
    Cantidad = models.IntegerField()
    iva = models.BooleanField()
    estado = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        cadena = "{0}"

        return cadena.format(self.nombre)


class Iva(models.Model):
    iva = models.DecimalField(max_digits=5, decimal_places=2)
    estado = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)


class ClaseProducto(models.Model):
    nombre = models.CharField(max_length=75)
    estado = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.nombre


class TipoProducto(models.Model):
    nombre = models.CharField(max_length=75)
    estado = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.nombre


class MedidaProducto(models.Model):
    nombre = models.CharField(max_length=75)
    estado = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.nombre


class TipoPago(models.Model):
    nombre = models.CharField(max_length=75)
    estado = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.nombre


class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=75)
    estado = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class CabFactura(models.Model):
    idEmpresa = models.ForeignKey(Empresa, null=False, blank=False, on_delete=models.CASCADE)
    facturaNumero = models.CharField(max_length=75)
    idUsuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    fecha = models.DateField()
    idTipoPago = models.ForeignKey(TipoPago, null=False, blank=False, on_delete=models.CASCADE)
    idTipoDocumento = models.ForeignKey(TipoDocumento, null=False, blank=False, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.facturaNumero


class DetFactura(models.Model):
    idCabFactura = models.ForeignKey(CabFactura, null=False, blank=False, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, null=False, blank=False, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    iva = models.DecimalField(max_digits=5, decimal_places=2)
    descuento = models.DecimalField(max_digits=5, decimal_places=2)
    estado = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        cadena = " factura #:{0} del clientes : {1}"

        return cadena.format(self.idCabFactura.facturaNumero, self.idCabFactura.idUsuario)