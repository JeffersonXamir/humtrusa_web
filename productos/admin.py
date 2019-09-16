from django.contrib import admin

from productos.models import Presentacion, Producto


@admin.register(Presentacion)
class PresentacionAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
    'lote', 'presentacion', 'nombre', 'descripcion', 'fecha_expiracion', 'fecha_produccion', 'tipo', 'precio_compra',
    'precio_venta', 'stock')
    search_fields = ('nombre', 'descripcion')
