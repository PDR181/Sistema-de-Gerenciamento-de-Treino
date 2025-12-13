from django import forms
from .models import FichaTreino, ItemFicha, Exercicio

class FichaTreinoForm(forms.ModelForm):
    class Meta:
        model = FichaTreino
        fields = ['nome']

class ItemFichaForm(forms.ModelForm):
    class Meta:
        model = ItemFicha
        fields = ['exercicio', 'series', 'repeticoes', 'peso']
