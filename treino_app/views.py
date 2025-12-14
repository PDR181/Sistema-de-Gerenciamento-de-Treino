from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import FichaTreino, ItemFicha
from .forms import FichaTreinoForm, ItemFichaForm, SignUpForm

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # cria o usuário já com senha criptografada [web:408][web:411]
            login(request, user)  # faz login automático após o cadastro [web:97]
            return redirect("fichas_list")  # ajuste para o nome da sua url inicial
    else:
        form = SignUpForm()

    return render(request, "treino/signup.html", {"form": form})


@login_required
def fichas_list(request):
    fichas = FichaTreino.objects.filter(
        usuario=request.user
    ).prefetch_related('itens__exercicio')
    return render(request, 'treino/fichas_list.html', {'fichas': fichas})


@login_required
def ficha_detalhe(request, ficha_id):
    ficha = get_object_or_404(
        FichaTreino,
        id=ficha_id,
        usuario=request.user
    )
    itens = ItemFicha.objects.filter(ficha=ficha).select_related('exercicio')

    context = {
        'ficha': ficha,
        'itens': itens,
    }
    return render(request, 'treino/ficha_detalhe.html', context)


@login_required
def criar_ficha(request):
    if request.method == 'POST':
        form = FichaTreinoForm(request.POST)
        if form.is_valid():
            ficha = form.save(commit=False)
            ficha.usuario = request.user
            ficha.save()
            # depois de criar, pode ir direto para os detalhes da ficha nova
            return redirect('ficha_detalhe', ficha_id=ficha.id)
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
            # volta para os detalhes da ficha
            return redirect('ficha_detalhe', ficha_id=ficha.id)
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
            # volta para os detalhes da ficha do item editado
            return redirect('ficha_detalhe', ficha_id=ficha.id)
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
    ficha_id = item.ficha.id

    if request.method == 'POST':
        item.delete()
        # volta para os detalhes da ficha de onde o item foi excluído
        return redirect('ficha_detalhe', ficha_id=ficha_id)

    return render(request, 'treino/excluir_item_ficha.html', {
        'item': item,
        'ficha': item.ficha,
    })
