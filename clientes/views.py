#from braces.views import GroupRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from clientes.forms import ClienteForm
from clientes.models import Cliente


class ListarCliente(ListView):
    context_object_name = 'clientes'
    model = Cliente
    template_name = 'clientes/listar_clientes.html'
    #group_required = ['trabajadores']


class DetalleView(DetailView):
    model = Cliente
    template_name = 'clientes/detalle_clientes.html'


class ActualizarView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/create_update_clientes.html'
    success_url = reverse_lazy('listar_clientes')


class EliminarView(DeleteView):
    model = Cliente
    template_name = 'clientes/eliminar_clientes.html'
    #group_required = ['administrador']
    success_url = reverse_lazy('listar_clientes')


class CrearCliente(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/create_update_clientes.html'
    success_url = reverse_lazy('listar_clientes')
