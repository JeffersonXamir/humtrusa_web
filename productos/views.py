# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Producto, Presentacion
from .forms import CrearProductosForm, CrearPresentacionForm
from django.http import HttpResponse
import csv

# reporte pdf
from django.http import HttpResponseRedirect
from datetime import *
from xhtml2pdf import pisa
from django import http
from django.template.loader import get_template
from io import BytesIO
import cgi


class ListaProductos(ListView):
    context_object_name = 'productos'
    model = Producto
    template_name = 'productos/lista_productos.html'


class DetalleView(DetailView):
    model = Producto
    template_name = 'productos/detalle_productos.html'


class ActualizarView(UpdateView):
    form_class = CrearProductosForm
    template_name = 'productos/create_update_productos.html'
    model = Producto
    success_url = reverse_lazy('listar_productos')


class CreateProductos(CreateView):
    model = Producto
    form_class = CrearProductosForm
    template_name = 'productos/create_update_productos.html'
    success_url = reverse_lazy('listar_productos')


class EliminarView(DeleteView):
    model = Producto
    success_url = '/productos'
    template_name = 'productos/eliminar_productos.html'


def CargaAtenciones_ant(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="atenciones.csv"'
    registrants = Producto.objects.all()
    writer = csv.writer(response, delimiter="|")
    writer.writerow(
        ['id', 'codigo', 'categoria', 'tipo', 'nombre', 'componente', 'concentracion', 'sanitario', 'fecha_expiracion',
         'fecha_produccion', 'descripcion', 'precio_compra', 'precio_venta', 'stock'])
    for registrant in registrants:
        writer.writerow([registrant.id,
                         registrant.codigo,
                         registrant.categoria,
                         registrant.tipo,
                         registrant.nombre.encode('utf-8'),
                         registrant.componente.encode('utf-8'),
                         registrant.concentracion.encode('utf-8'),
                         registrant.sanitario,
                         registrant.fecha_expiracion,
                         registrant.fecha_produccion,
                         registrant.descripcion.encode('utf-8'),
                         registrant.precio_compra,
                         registrant.precio_venta,
                         registrant.stock
                         ])
    return response


def write_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)

    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return http.HttpResponse(result.getvalue(), content_type="application/pdf")
    return http.HttpResponse('Ocurrio un error al genera el reporte %s' % cgi.escape(html))


def generar_reporte_productos(request):
    productos = Producto.objects.all()

    total_precio_compra = 0
    for expe in productos:
        total_precio_compra = (expe.stock * expe.precio_compra) + total_precio_compra

    total_precio_venta = 0
    for expe in productos:
        total_precio_venta = (expe.stock * expe.precio_venta) + total_precio_venta

    ganancia = total_precio_venta - total_precio_compra

    return write_pdf('productos/reporte_detalle_productos.html', {'pagesize': 'legal',
                                                                  'productos': productos,
                                                                  'total_precio_compra': total_precio_compra,
                                                                  'total_precio_venta': total_precio_venta,
                                                                  'ganancia': ganancia})


# Presentación

class CreatePresentacion(CreateView):
    form_class = CrearPresentacionForm
    template_name = 'productos/create_update_presentacion.html'
    model = Presentacion
    success_url = reverse_lazy('crear_productos')
