from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Artista
from .forms import ArtistaForm
from .models import Evento
from .forms import EventoForm


def home(request):
    # Adicione qualquer lógica necessária aqui
    return render(request, 'artista/home.html')


def cadastrar_artista(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Artista cadastrado com sucesso!')
            form = ArtistaForm()
            # Redirecionar o usuário para outra página, se necessário
    else:
        form = ArtistaForm()
    return render(request, 'artista/cadastrar_artista.html', {'form': form})


def listar_artista(request):
    artistas = Artista.objects.all()
    if not artistas:
        return render(request, 'artista/sem_artista.html')
    else:
        return render(request, 'artista/listar_artista.html', {'artistas': artistas})


def sem_artista(request):
    return render(request, 'artista/sem_artista.html')


def editar_artista(request, artista_id):
    artista = get_object_or_404(Artista, pk=artista_id)
    if request.method == 'POST':
        form = ArtistaForm(request.POST, instance=artista)
        if form.is_valid():
            form.save()
            messages.success(request, 'Artista editado com sucesso!')
            return redirect('listar_artista')
        else:
            messages.error(request, 'Corrija os erros no formulário.')
    else:
        form = ArtistaForm(instance=artista)
    return render(request, 'editar_artista.html', {'form': form, 'artista': artista})


def excluir_artista(request, artista_id):
    artista = get_object_or_404(Artista, pk=artista_id)
    if request.method == 'POST':
        artista.delete()
        messages.success(request, 'Artista excluído com sucesso!')
        return redirect('listar_artista')
    return render(request, 'artista/excluir_artista_confirmacao.html', {'artista': artista})


def confirmar_excluir_artista(request, artista_id):
    # Recuperar o objeto do artista a ser excluído
    artista = get_object_or_404(Artista, pk=artista_id)
    # Renderizar o template com o contexto adequado
    return render(request, 'artista/excluir_artista_confirmacao.html', {'artista': artista})


def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'artista/listar_eventos.html', {'eventos': eventos})


def criar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save()
            print("Evento salvo com sucesso:", evento)
            return redirect('artista/listar_eventos')
        else:
            print("Erros no formulário:", form.errors)
    else:
        form = EventoForm()
    return render(request, 'artista/criar_evento.html', {'form': form})
