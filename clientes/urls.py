from django.contrib.auth.decorators import login_required
from django.urls import path
from clientes.views import ActualizarView, EliminarView, DetalleView, CrearCliente, ListarCliente

urlpatterns = [

    path('create/', login_required(CrearCliente.as_view()), name='crear_clientes'),
    path('list/', login_required(ListarCliente.as_view()), name='listar_clientes'),
    path('edit/<int:pk>/', login_required(ActualizarView.as_view()), name='actualizar_clientes'),
    path('delete/<int:pk>/', login_required(EliminarView.as_view()), name='eliminar_clientes'),
    path('detail/<int:pk>/', login_required(DetalleView.as_view()), name='detalle_clientes'),
]