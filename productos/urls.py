from django.contrib.auth.decorators import login_required
from django.urls import path

from productos.views import CreateProductos, DetalleView, ActualizarView, CreatePresentacion, EliminarView, \
    ListaProductos, generar_reporte_productos

urlpatterns = [

    path('', login_required(ListaProductos.as_view()), name='listar_productos'),
    path('agregar/', login_required(CreateProductos.as_view()), name='crear_productos'),
    path('detalle/<int:pk>/', login_required(DetalleView.as_view()), name='detalle_productos'),
    path('actualizar/<int:pk>/', login_required(ActualizarView.as_view()), name='actualizar_productos'),
    path('eliminar/<int:pk>/', login_required(EliminarView.as_view()), name='eliminar_productos'),
    # exportar a excel
    # path('expatenciones/', CargaAtenciones_ant,name='xds'),
    path('reporte/', login_required(generar_reporte_productos), name='reporte_productos'),
    # presentacion
    path('presentacion', CreatePresentacion.as_view(), name='crear_presentacion'),

]
