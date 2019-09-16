from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView
from compras.views import ListaCompras, realizar_compra, reportecompras, generar_reporte_lista_compras

urlpatterns = [

    path('realizar_compras/', login_required(realizar_compra), name='realizar_compras'),
    path('listar_compras/', login_required(ListaCompras.as_view()), name='listar_compras'),
    path('confirmacion_compras/', login_required(TemplateView.as_view(template_name="compras/confirmacion_compra.html")), name='confirmacion_compras'),
    path('reporte_compras/<int:pk>/', login_required(reportecompras), name='reporte_compras'),
    path('generar_reporte_lista_compras/', login_required(generar_reporte_lista_compras), name='generar_reporte_lista_compras'),

]
