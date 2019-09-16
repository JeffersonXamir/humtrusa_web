from django.shortcuts import render, redirect
from django.views.generic import *
from empresa.forms import *
from empresa.models import *
from django.urls import reverse_lazy

"""
def index(request):
    return HttpResponse("Hello, world. index.")
"""


def index(request):
    return render(request, 'users/home.html')


def empresa_crear(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            q = form.save()
        print(q.id)
        return redirect('index')
    else:
        form = EmpresaForm()

    return render(request, 'empresa/empresa_form.html', {'form': form})


def empresa_listar(request):
    empresa = Empresa.objects.all().order_by('id')
    contexto = {'empresas': empresa}
    return render(request, 'empresa/empresa_list.html', contexto)


def empresa_editar(request, id_empresa):
    empresa = Empresa.objects.get(id=id_empresa)
    if request.method == 'GET':
        form = EmpresaForm(instance=empresa)
    else:
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
        return redirect('empresa_listar')
    return render(request, 'empresa/empresa_form.html', {'form': form})


def empresa_eliminar(request, id_empresa):
    empresa = Empresa.objects.get(id=id_empresa)
    if request.method == 'POST':
        empresa.delete()
        return redirect('empresa_listar')
    contexto = {'empresa': empresa}
    return render(request, 'empresa/empresa_delete.html', contexto)


"""

crud tipo clases
"""


class EmpresaCreate(CreateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'empresa/empresa_form.html'
    success_url = reverse_lazy('empresa_listar')
