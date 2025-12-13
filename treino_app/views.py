from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import FichaTreino, ItemFicha
from .forms import FichaTreinoForm, ItemFichaForm


@login_required
def fichas_list(request):
    fichas = FichaTreino.objects.filter(
        usuario=request.user
    ).prefetch_related('itens__exercicio')
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


@login_required
def adicionar_item_ficha(request, ficha_id):
    ficha = get_object_or_404(FichaTreino, id=ficha_id, usuario=request.user)

    if request.method == 'POST':
        form = ItemFichaForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.ficha = ficha
            item.save()
            return redirect('fichas_list')
    else:
        form = ItemFichaForm()

    return render(request, 'treino/adicionar_item_ficha.html', {
        'ficha': ficha,
        'form': form,
    })


@login_required
def editar_item_ficha(request, item_id):
    item = get_object_or_404(
        ItemFicha,
        id=item_id,
        ficha__usuario=request.user
    )
    ficha = item.ficha

    if request.method == 'POST':
        form = ItemFichaForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('fichas_list')
    else:
        form = ItemFichaForm(instance=item)

    return render(request, 'treino/editar_item_ficha.html', {
        'ficha': ficha,
        'form': form,
        'item': item,
    })


@login_required
def excluir_item_ficha(request, item_id):
    item = get_object_or_404(
        ItemFicha,
        id=item_id,
        ficha__usuario=request.user
    )
    if request.method == 'POST':
        item.delete()
        return redirect('fichas_list')

    return render(request, 'treino/excluir_item_ficha.html', {
        'item': item,
        'ficha': item.ficha,
    })

