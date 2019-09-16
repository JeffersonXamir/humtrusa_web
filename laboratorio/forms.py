# encoding:utf-8
from django import forms
from .models import Laboratorio


class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio

        fields = '__all__'
