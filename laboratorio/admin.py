from django.contrib import admin

from laboratorio.models import Laboratorio


@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'sanitario', 'autorizacion')
