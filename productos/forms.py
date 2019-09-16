from .models import *
from django import forms


class CrearProductosForm(forms.ModelForm):
    class Meta:
        model = Producto

        fields = '__all__'

        widgets = {
            'lote': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'componente': forms.TextInput(attrs={'class': 'form-control'}),
            'concentracion': forms.TextInput(attrs={'class': 'form-control'}),
            'sanitario': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': '6'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio_compra': forms.NumberInput(attrs={'class': 'form-control', 'id': 'precio_compra'}),
            'precio_venta': forms.NumberInput(attrs={'class': 'form-control', 'id': 'precio_venta'}),
            'presentacion': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'fecha_expiracion': forms.DateInput(
                attrs={'class': 'form-control', 'id': 'Date', 'data-date-format': 'dd/mm/yyyy'}),
            'fecha_produccion': forms.DateInput(
                attrs={'class': 'form-control', 'id': 'Date1', 'data-date-format': 'dd/mm/yyyy'}),
            'iva': forms.NumberInput(attrs={'class': 'form-control', 'id': 'iva'}),
        }


class CrearPresentacionForm(forms.ModelForm):
    class Meta:
        model = Presentacion
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
