from django.contrib import admin
from django.urls import path, include  # Importe a função include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('artista.urls')),  # Inclua as URLs do aplicativo artista
    # Adicione outras URLs conforme necessário
]
