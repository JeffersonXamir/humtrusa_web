from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from userProfile.models import UserProfile


class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class PerfilForm(forms.ModelForm):
    class Meta:
        model = UserProfile

        fields = '__all__'
