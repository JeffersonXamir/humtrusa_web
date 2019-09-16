from django.contrib import admin

from compras.models import DetalleCompra, CabeceraCompra


class producto_compraInline(admin.TabularInline):
    model = DetalleCompra


class compraAdmin(admin.ModelAdmin):
    inlines = (producto_compraInline,)


admin.site.register(CabeceraCompra, compraAdmin)
