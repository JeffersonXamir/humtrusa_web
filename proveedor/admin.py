from django.contrib import admin
from proveedor.models import Proveedor


@admin.register(Proveedor)
class DistribuidorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ruc')
    search_fields = ('codigo', 'nombre')