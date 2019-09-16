# -*- coding:utf-8 -*-
from django.forms import ModelForm, inlineformset_factory
from .models import *


class todo_listForm(ModelForm):
    class Meta:
        model = CabeceraVenta

        fields = '__all__'


todo_itemSet = inlineformset_factory(CabeceraVenta, DetalleVenta, form=todo_listForm, extra=3)
