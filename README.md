1. Contexto (Nível 1):
  Contexto: Sistema de Gerenciamento de Eventos Musicais

1. Stakeholders:
   - Cliente: Casa de eventos musicais
   - Administradores: Usuários responsáveis pelo gerenciamento do sistema
   - Artistas: Performers que participam dos eventos

2. Sistemas Externos:
   - Serviço de Mensagens: Sistema externo usado para enviar mensagens automáticas para os artistas.

3. Funcionalidades Principais:
   - Cadastro de Artistas: Permite aos administradores cadastrar novos artistas com informações detalhadas.
   - Agendamento de Eventos: Permite aos administradores associar artistas a datas específicas para eventos.
   - Envio Automático de Mensagens: No dia do evento, o sistema envia mensagens automáticas para os artistas para lembrá-los do compromisso.
   - Gerenciamento de Artistas: Capacidade de visualizar, editar e excluir informações dos artistas cadastrados.

4. Ambiente Externo:
   - Conexão com Serviço de Mensagens: O sistema deve estar configurado para se comunicar com o serviço de mensagens para enviar SMS automáticos.
Contexto: Sistema de Gerenciamento de Eventos Musicais

1. Stakeholders:
   - Cliente:  Casting Artístico DH PRODUÇÕES
   - Administradores: Usuários responsáveis pelo gerenciamento do sistema
   - Artistas: Performers que participam dos eventos

2. Sistemas Externos:
   - Serviço de Mensagens: Sistema externo usado para enviar mensagens automáticas para os artistas.

3. Funcionalidades Principais:
   - Cadastro de Artistas: Permite aos administradores cadastrar novos artistas com informações detalhadas.
   - Agendamento de Eventos: Permite aos administradores associar artistas a datas específicas para eventos.
   - Envio Automático de Mensagens: No dia do evento, o sistema envia mensagens automáticas para os artistas para lembrá-los do compromisso.
   - Gerenciamento de Artistas: Capacidade de visualizar, editar e excluir informações dos artistas cadastrados.

4. Ambiente Externo:
   - Conexão com Serviço de Mensagens: O sistema deve estar configurado para se comunicar com o serviço de mensagens para enviar SMS automáticos.

2. Contêineres (Nível 2):
 Nível 2: Contêineres

Interface de Usuário (UI):
- Responsável por fornecer uma interface amigável para os usuários interagirem com o sistema.
- Inclui páginas da web, formulários, estilos visuais, etc.
- Comunica-se com a aplicação web para enviar solicitações e receber respostas.

Aplicação Web (Web Application):
- Implementa a lógica de negócios do sistema usando o framework Django.
- Inclui views, models, forms, middleware, etc.
- Comunica-se com o banco de dados para recuperar e armazenar dados.

Banco de Dados (Database):
- Armazena todos os dados do sistema, incluindo informações de artistas, eventos, usuários, etc.
- Utilizaremos o banco de dados SQLite padrão fornecido pelo Django para este exemplo.

3. Componentes (Nível 3):
Nível 3: Componentes

Interface de Usuário (UI):
- Páginas da Web:
  - Página de Cadastro de Artista
  - Página de Listagem de Artistas
  - Página de Detalhes do Artista
  - ...
- Formulários:
  - Formulário de Cadastro de Artista
  - ...
- Estilos Visuais:
  - Estilos CSS para todas as páginas
  - ...

Aplicação Web (Web Application):
- Views:
  - View para exibir o formulário de cadastro de artistas
  - View para processar o formulário de cadastro de artistas
  - View para exibir a lista de artistas cadastrados
  - View para exibir os detalhes de um artista específico
  - ...
- Models:
  - Modelo de Artista (com campos como nome, gênero, descrição, etc.)
  - ...
- Forms:
  - Formulário de Cadastro de Artista (com campos correspondentes ao modelo de artista)
  - ...
- Middleware:
  - Middleware de autenticação de usuário
  - Middleware para tratamento de erros
  - ...

Banco de Dados (Database):
- Tabelas:
  - Tabela de Artistas (com colunas para nome, gênero, descrição, etc.)
  - ...
- Campos:
  - Campo "Nome" na tabela de artistas
  - Campo "Gênero" na tabela de artistas
  - ...
- Consultas:
  - Consulta para recuperar todos os artistas
  - Consulta para recuperar um artista específico por ID
  - ...

4. Código (Nível 4):
Nível 4: Código

Views (Visualizações):
- views.py:
  - def cadastrar_artista(request): # View para exibir e processar o formulário de cadastro de artistas
  - def listar_artistas(request): # View para exibir a lista de artistas cadastrados
  - def detalhar_artista(request, artista_id): # View para exibir os detalhes de um artista específico
  - ...

Models (Modelos):
- models.py:
  class Artista(models.Model):
    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    descricao = models.TextField()
    ...

Forms (Formulários):
- forms.py:
  class FormularioCadastroArtista(forms.ModelForm):
    class Meta:
      model = Artista
      fields = ['nome', 'genero', 'descricao']
    ...

Templates (Modelos de Visualização):
- templates/:
  - cadastro_artista.html # Template para o formulário de cadastro de artistas
  - listar_artistas.html # Template para exibir a lista de artistas cadastrados
  - detalhes_artista.html # Template para exibir os detalhes de um artista específico
  - ...

Urls (URLs):
- urls.py:
  from django.urls import path
  from . import views

  urlpatterns = [
    path('cadastrar-artista/', views.cadastrar_artista, name='cadastrar_artista'),
    path('listar-artistas/', views.listar_artistas, name='listar_artistas'),
    path('detalhes-artista/<int:artista_id>/', views.detalhar_artista, name='detalhar_artista'),
    ...
  ]

 -----------------------------------------------------------------------------------------------------------------



PS C:\Users\genti\OneDrive\Documentos\dh_producoes> .\dh\Scripts\activate
>>
(dh) PS C:\Users\genti\OneDrive\Documentos\dh_producoes> cd gestao_dh
(dh) PS C:\Users\genti\OneDrive\Documentos\dh_producoes\gestao_dh> cd artista
