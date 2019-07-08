from django import forms
from preventa.models import *


class CabVentaForm(forms.ModelForm):
    class Meta:
        model = CabVenta
        fields = [
            'usuarioNombre',
            'fecha',
        ]
        labels = {
            'usuarioNombre': 'Nombre',
            'fecha': 'Fecha',
        }
        widgets = {
            'usuarioNombre': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }


class DetVentaForm(forms.ModelForm):
    class Meta:
        model = DetVenta
        fields = [
            'productoNombre',
            'cantidad',
            'precio',
            'iva',
            'descuento',
        ]
        labels = {
            'productoNombre': 'Producto',
            'cantidad': 'Cantidad',
            'precio': 'precio',
            'iva': 'Iva',
            'descuento': 'Descuento',
        }
        widgets = {
            'productoNombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'iva': forms.NumberInput(attrs={'class': 'form-control'}),
            'descuento': forms.NumberInput(attrs={'class': 'form-control'}),
        }
