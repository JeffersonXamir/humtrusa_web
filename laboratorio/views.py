# Create your views here.
# -*- coding: utf-8 -*-
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, TemplateView, UpdateView, ListView, DetailView
from .models import Laboratorio
from .forms import LaboratorioForm


class ListaLaboratorio(ListView):
    context_object_name = 'laboratorios'
    model = Laboratorio
    template_name = 'laboratorios/lista_laboratorios.html'
    success_url = reverse_lazy('listar_laboratorios')


# Create your views here.
class DetalleView(DetailView):
    model = Laboratorio
    template_name = 'laboratorios/detalle_laboratorios.html'


class ActualizarView(UpdateView):
    form_class = LaboratorioForm
    template_name = 'laboratorios/crear_laboratorios.html'
    model = Laboratorio
    success_url = reverse_lazy('listar_laboratorios')


class EliminarView(DeleteView):
    model = Laboratorio
    template_name = 'laboratorios/eliminar_laboratorios.html'
    success_url = reverse_lazy('listar_laboratorios')


class CreateLaboratorio(CreateView):
    model = Laboratorio
    form_class = LaboratorioForm
    template_name = 'laboratorios/crear_laboratorios.html'
    success_url = reverse_lazy('listar_laboratorios')
