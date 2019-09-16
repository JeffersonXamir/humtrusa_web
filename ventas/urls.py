from django.contrib.auth.decorators import login_required
from django.urls import path
from ventas.views import todo_listCreateView, TodoitemAjax

urlpatterns = [

   # path('', login_required(todo_listCreateView.as_view()), name='crear_ventas'),
    #path('author-ajax/', login_required(TodoitemAjax), name='listar_ventas'),

]

