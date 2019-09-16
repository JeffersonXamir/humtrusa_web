from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from proveedor.forms import ProveedorForm
from proveedor.models import Proveedor


class ListarProveedor(ListView):
    context_object_name = 'proveedor'
    model = Proveedor
    template_name = 'proveedor/listar_proveedor.html'



class DetalleView(DetailView):
    model = Proveedor
    template_name = 'proveedor/detalle_proveedor.html'


class ActualizarView(UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'proveedor/create_update_proveedor.html'
    success_url = reverse_lazy('listar_proveedor')


class EliminarView(DeleteView):
    model = Proveedor
    template_name = 'proveedor/eliminar_proveedor.html'

    success_url = reverse_lazy('listar_proveedor')


class CrearProveedor(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'proveedor/create_update_proveedor.html'
    success_url = reverse_lazy('listar_proveedor')
