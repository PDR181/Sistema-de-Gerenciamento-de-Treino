from django import forms
from .models import FichaTreino

class FichaTreinoForm(forms.ModelForm):
    class Meta:
        model = FichaTreino
        fields = ['nome']  # usuário será preenchido na view
