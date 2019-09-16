from django.contrib.auth.decorators import login_required
from django.urls import path
from empresa import views
from empresa.views import EmpresaCreate

urlpatterns = [
    #path('', views.index, name='index'),
    path('create/', login_required(EmpresaCreate.as_view()), name='empresa_crear'),
    path('list/', login_required(views.empresa_listar), name='empresa_listar'),
    path('edit/<int:id_empresa>/', login_required(views.empresa_editar), name='empresa_editar'),
    path('delete/<int:id_empresa>/', login_required(views.empresa_eliminar), name='empresa_eliminar'),
]
