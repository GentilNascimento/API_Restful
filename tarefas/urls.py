# Importações responsável por gerar a documentação
# da API usando Swagger ou Redoc. Definir as rotas,
# e as views que manipulam as requisições/user/tarefas.
from trilhabackendjr.urls import schema_view
from django.urls import path
from .views import UserCreate, TarefaListCreate,TarefaRetrieveUpdateDestroy


urlpatterns = [
     path('user/', UserCreate.as_view(), name='user-create'),
     path('', schema_view.with_ui('swagger',
          cache_timeout=0), name='schema-swagger-ui'),
     path('redoc/', schema_view.with_ui('redoc',
          cache_timeout=0), name='schema-redoc'), 
     path('tarefas/', TarefaListCreate.as_view(), name='tarefa-list-create'),
     #recuperar, atualizar ou deletar uma tarefa específica.
     path('tarefas/<int:pk>/', TarefaRetrieveUpdateDestroy.as_view(),
          name='tarefa-retrieve-update-destroy'),
]
