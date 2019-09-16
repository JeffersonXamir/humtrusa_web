from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from userProfile.forms import RegistroForm, PerfilForm
from userProfile.models import UserProfile


class RegistroUsuario(CreateView):
    model = User
    template_name = 'registration/registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy('listar_usuario')


class ListarUsuario(ListView):
    context_object_name = 'usuario'
    model = User
    template_name = 'registration/user_list.html'


class ActualizarView(UpdateView):
    model = User
    form_class = RegistroForm
    template_name = 'registration/registrar.html'
    success_url = reverse_lazy('listar_usuario')


class EliminarView(DeleteView):
    model = User
    template_name = 'registration/user_delist.html'
    success_url = reverse_lazy('listar_usuario')


class PerfilUsuario(CreateView):
    model = UserProfile
    template_name = 'registration/profiles.html'
    form_class = PerfilForm
    success_url = reverse_lazy('listar_usuario')

