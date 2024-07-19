from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL para a página inicial
    path('cadastrar-artista/', views.cadastrar_artista, name='cadastrar_artista'), #URL para a pág. de cadastro de artista
    path('listar-artista/', views.listar_artista, name='listar_artista'), #URL para listar os artistas.
    path('editar-artista/<int:artista_id>/', views.editar_artista, name='editar_artista'),  #URL para editar o artista.
    path('excluir-artista/<int:artista_id>/', views.excluir_artista, name='excluir_artista'), #URL para excluir o artista.
    path('confirmar-excluir-artista/<int:artista_id>/', views.confirmar_excluir_artista, name='confirmar_excluir_artista'), 
    path('sem_artista/', views.sem_artista, name='sem_artista'),
    path('listar_eventos/', views.listar_eventos, name='listar_eventos'),
    path('criar_evento/', views.criar_evento, name='criar_evento'),
]
 