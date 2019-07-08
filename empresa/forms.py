from django import forms
from empresa.models import *


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
            'nombre',
            'direccion',
            'telefono',
            'ruc',
        ]
        labels = {
            'nombre': 'Nombre',
            'direccion': 'Direccion',
            'telefono': 'Telefono',
            'ruc': 'Ruc',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'ruc': forms.TextInput(attrs={'class': 'form-control'}),
        }
