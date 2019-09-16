from django.contrib.auth.decorators import login_required
from django.urls import path
from proveedor.views import ActualizarView, DetalleView, ListarProveedor, CrearProveedor, EliminarView

urlpatterns = [

    path('create/', login_required(CrearProveedor.as_view()), name='crear_proveedor'),
    path('list/', login_required(ListarProveedor.as_view()), name='listar_proveedor'),
    path('edit/<int:pk>/', login_required(ActualizarView.as_view()), name='actualizar_proveedor'),
    path('delete/<int:pk>/', login_required(EliminarView.as_view()), name='eliminar_proveedor'),
    path('detail/<int:pk>/', login_required(DetalleView.as_view()), name='detalle_proveedor'),
]