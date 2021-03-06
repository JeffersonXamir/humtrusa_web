# -*- coding: utf-8 -*-
from _threading_local import local

from django.template import RequestContext as ctx
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext  # For CSRF
from django.forms.formsets import formset_factory, BaseFormSet
from django.http import HttpResponse, HttpResponseRedirect

# reporte pdf
from django.http import HttpResponseRedirect
from datetime import *
from xhtml2pdf import pisa
from django import http
from django.template.context_processors import csrf
from django.template.loader import get_template
from django.template import Context
from io import BytesIO
import cgi
from .forms import TodoListForm, TodoItemForm, RangoForm
from .models import CabeceraCompra
from django.views.generic import ListView, TemplateView


def realizar_compra(request):
    # This class is used to make empty formset forms required
    # See http://stackoverflow.com/questions/2406537/django-formsets-make-first-required/4951032#4951032
    class RequiredFormSet(BaseFormSet):
        def __init__(self, *args, **kwargs):
            super(RequiredFormSet, self).__init__(*args, **kwargs)
            for form in self.forms:
                form.empty_permitted = False

    TodoItemFormSet = formset_factory(TodoItemForm, max_num=100, formset=RequiredFormSet)

    if request.method == 'POST':  # If the form has been submitted...
        todo_list_form = TodoListForm(request.POST)  # A form bound to the POST data
        # Create a formset from the submitted data
        todo_item_formset = TodoItemFormSet(request.POST, request.FILES)
        if todo_list_form.is_valid() and todo_item_formset.is_valid():
            trabajador = request.user
            nuevo_evento = todo_list_form.save(commit=False)
            nuevo_evento.trabajador = trabajador
            nuevo_evento.save()
            todo_list = todo_list_form.save()

            for form in todo_item_formset.forms:
                todo_item = form.save(commit=False)
                todo_item.list = todo_list
                todo_item.save()

            return redirect('confirmacion_compras')  # Redirect to a 'success' page
    else:
        todo_list_form = TodoListForm()
        todo_item_formset = TodoItemFormSet()

    # For CSRF protection
    # See http://docs.djangoproject.com/en/dev/ref/contrib/csrf/
    c = {'todo_list_form': todo_list_form,
         'todo_item_formset': todo_item_formset,
         }
    c.update(csrf(request))
    return render(request, 'compras/realizar_compra.html', c)


class ListaCompras(ListView):
    template_name = 'compras/lista_compras.html'
    model = CabeceraCompra

    def get_context_data(self, **kwargs):
        context = super(ListaCompras, self).get_context_data(**kwargs)
        context['events'] = CabeceraCompra.objects.filter(trabajador=self.request.user)
        context['compras'] = context['events']
        return context


def reportecompras(request, pk):
    compra = CabeceraCompra.objects.get(pk=pk)
    productos = compra.cabecera.all()

    total = 0
    for expe in productos:
        total = (expe.cantidad * expe.producto.precio_compra) + total

    return render(request, 'compras/reportecompras.html', locals())


def write_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)

    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return http.HttpResponse(result.getvalue(), content_type="application/pdf")
    return http.HttpResponse('Ocurrio un error al genera el reporte %s' % cgi.escape(html))


def generar_reporte_lista_compras(request):
    if request.method == "POST":
        formbusqueda = RangoForm(request.POST)
        if formbusqueda.is_valid():
            fecha_in = formbusqueda.cleaned_data['fecha_i']
            fecha_fi = formbusqueda.cleaned_data['fecha_f']
            rango = CabeceraCompra.objects.filter(fecha__gte=(fecha_in), fecha__lte=(fecha_fi)).order_by('trabajador')
            return write_pdf('compras/reporte_detalle_lista_compras.html', {'pagesize': 'legal', 'rango': rango})
            # return render_to_response ('empleados/test.html',{'rango':rango},context_instance=RequestContext(request))
        else:
            error = "Hay un error en las fechas proporcionadas"
            return render(request, 'compras/rango_fecha_reporte_lista_compra.html', {'error': error})

    return render(request, 'compras/rango_fecha_reporte_lista_compra.html', {'rangoform': RangoForm()})
