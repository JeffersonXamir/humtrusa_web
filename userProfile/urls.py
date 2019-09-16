from django.contrib.auth.decorators import login_required
from django.urls import path
from userProfile.views import RegistroUsuario, ListarUsuario, ActualizarView, EliminarView, PerfilUsuario

urlpatterns = [

    path('create/', login_required(RegistroUsuario.as_view()), name='crear_usuario'),
    path('profile/', login_required(PerfilUsuario.as_view()), name='perfil_usuario'),
    path('list/', login_required(ListarUsuario.as_view()), name='listar_usuario'),
    path('edit/<int:pk>/', login_required(ActualizarView.as_view()), name='actualizar_usuario'),
    path('delete/<int:pk>/', login_required(EliminarView.as_view()), name='eliminar_usuario'),

]