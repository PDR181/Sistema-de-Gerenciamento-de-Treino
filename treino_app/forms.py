from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import FichaTreino, ItemFicha, Exercicio


class FichaTreinoForm(forms.ModelForm):
    class Meta:
        model = FichaTreino
        fields = ['nome']


class ItemFichaForm(forms.ModelForm):
    class Meta:
        model = ItemFicha
        fields = ['exercicio', 'series', 'repeticoes', 'peso']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
