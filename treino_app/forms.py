from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import FichaTreino, ItemFicha, Exercicio, Profile


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


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]


class EditProfileExtraForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["nome_completo", "idade", "peso_kg", "altura_cm"]