from django.contrib.auth.decorators import login_required
from django.urls import path
from factura.views import ListaVentas, facturaCrear, buscarCliente, buscarProducto, consultarFactura, generar_pdf, \
    reporteventas

urlpatterns = [

    path('create/', login_required(facturaCrear), name='factura_ventas'),
    path('buscar_clientes/', login_required(buscarCliente)),
    path('buscar_productos/', login_required(buscarProducto)),
    #path('query/', login_required(consultarFactura), name='consultar_factura'),
    path('list/', login_required(ListaVentas.as_view()), name='listar_ventas'),
    path('generar_reporte_factura/', login_required(generar_pdf), name='generar_reporte_factura'),
    path('reporte_ventas/<int:pk>/', login_required(reporteventas), name='reporte_ventas'),

]
