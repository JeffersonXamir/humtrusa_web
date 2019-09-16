from django.contrib import admin
from clientes.models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'apellidos', 'direccion', 'telefono')
    search_fields = ('cedula', 'nombre')
