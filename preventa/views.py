from django.http import HttpResponseRedirect
from preventa.forms import *
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView


class PreVentaCreate(CreateView):
    model = DetVenta, CabVenta
    template_name = 'preVenta/preVenta_form.html'
    form_class = DetVentaForm
    second_form_class = CabVentaForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(PreVentaCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            detalle = form.save(commit=False)
            detalle.idCabVenta = form2.save()
            detalle.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


class PreVentaUpdate(UpdateView):
    model = DetVenta
    second_model = CabVenta
    template_name = 'adopcion/solicitud_form.html'
    form_class = DetVentaForm
    second_form_class = CabVentaForm
    success_url = reverse_lazy('adopcion:solicitud_listar')

    def get_context_data(self, **kwargs):
        context = super(PreVentaUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        detalle = self.model.objects.get(id=pk)
        cabecera = self.second_model.objects.get(id=detalle.idCabVenta)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=cabecera)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_detalle = kwargs['pk']
        detalle = self.model.objects.get(id=id_detalle)
        cabecera = self.second_model.objects.get(id=detalle.idCabVenta)
        form = self.form_class(request.POST, instance=detalle)
        form2 = self.second_form_class(request.POST, instance=cabecera)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())


class PreVentaDelete(DeleteView):
    model = DetVenta
    template_name = 'adopcion/solicitud_delete.html'
    success_url = reverse_lazy('adopcion:solicitud_listar')
