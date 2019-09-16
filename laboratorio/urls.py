from django.contrib.auth.decorators import login_required
from django.urls import path
from laboratorio.views import CreateLaboratorio, ListaLaboratorio, DetalleView, ActualizarView, EliminarView

urlpatterns = [

    path('create/', login_required(CreateLaboratorio.as_view()), name='crear_laboratorios'),
    path('list/', login_required(ListaLaboratorio.as_view()), name='listar_laboratorios'),
    path('edit/<int:pk>/', login_required(ActualizarView.as_view()), name='actualizar_laboratorios'),
    path('delete/<int:pk>/', login_required(EliminarView.as_view()), name='eliminar_laboratorios'),
    path('detail/<int:pk>/', login_required(DetalleView.as_view()), name='detalle_laboratorios'),

]
