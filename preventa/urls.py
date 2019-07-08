from django.contrib.auth.decorators import login_required
from django.urls import path
from preventa.views import PreVentaCreate

urlpatterns = [
    path('create/', login_required(PreVentaCreate.as_view()), name='venta_crear'),
]
