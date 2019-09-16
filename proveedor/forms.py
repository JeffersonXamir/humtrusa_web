from django import forms

from proveedor.models import Proveedor


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor

        fields = '__all__'

        widgets = {

            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'ruc': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),

        }

    def clean_cedula(self):
        ruc = self.cleaned_data['ruc']
        if len(ruc) < 13 or len(ruc) > 13:
            raise forms.ValidationError("debe ser de 13 Digitos para RUC")
        return ruc

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if not nombre.isalpha():
            raise forms.ValidationError('No puede contener números')
        return nombre
