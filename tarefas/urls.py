from django.urls import path
from .views import TarefaListCreate, TarefaRetrieveUpdateDestroy, home

urlpatterns = [
    path('', home, name='home'),  # Rota página inicial
    path('tarefas/', TarefaListCreate.as_view(), name='tarefa-list-create'),
    path('tarefas/<int:pk>/', TarefaRetrieveUpdateDestroy.as_view(),
         name='tarefa-retrieve-update-destroy'),
]
