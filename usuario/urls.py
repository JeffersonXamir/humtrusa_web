from django.contrib.auth.decorators import login_required
from django.urls import path
from usuario.views import *

urlpatterns = [
    path('registrar/', login_required(RegistroUsuario.as_view()), name='usuario_crear'),

]
