from django import forms

from clientes.models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente

        fields = ['cedula', 'nombre', 'apellidos', 'direccion', 'telefono']

        labels = {
            'cedula': 'Cedula/Ruc',
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'direccion': 'Direccion',
            'telefono': 'Telefono',
        }

        widgets = {
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),

        }

    def clean_cedula(self):
        cedula = self.cleaned_data['cedula']
        if len(cedula) < 10 or len(cedula) > 13:
            raise forms.ValidationError("debe ser de 10 Digitos para cedula o 13 para RUC")
        return cedula

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if not nombre.isalpha():
            raise forms.ValidationError('No puede contener números')
        return nombre
