from django.contrib import admin

from ventas.models import CabeceraVenta, DetalleVenta


class producto_ventaInline(admin.TabularInline):
    model = DetalleVenta


class Detalle_VentaAdmin(admin.ModelAdmin):
    inlines = (producto_ventaInline,)


admin.site.register(CabeceraVenta, Detalle_VentaAdmin)
