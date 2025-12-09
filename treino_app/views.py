from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import FichaTreino
from .forms import FichaTreinoForm

def fichas_list(request):
    if request.user.is_authenticated:
        fichas = FichaTreino.objects.filter(usuario=request.user).prefetch_related('itens__exercicio')
    else:
        fichas = []
    return render(request, 'treino/fichas_list.html', {'fichas': fichas})

@login_required
def criar_ficha(request):
    if request.method == 'POST':
        form = FichaTreinoForm(request.POST)
        if form.is_valid():
            ficha = form.save(commit=False)
            ficha.usuario = request.user
            ficha.save()
            return redirect('fichas_list')
    else:
        form = FichaTreinoForm()
    return render(request, 'treino/criar_ficha.html', {'form': form})
