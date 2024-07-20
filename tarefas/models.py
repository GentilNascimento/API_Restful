#Este código define o modelo Tarefa para gerenciar tarefas,
#dentro de um sistema Django. Cada tarefa possui um título, 
#descrição, data de criação, estado de conclusão e é associada 
#a um usuário específico.  

#módulo que importa modelos que fornece classes 
#pra definir db, e usuários.
from django.db import models
from django.contrib.auth.models import User

#define o modelo como tarefa, e será usado
#pra criar tabela no db.
class Tarefa(models.Model):
    titulo = models.CharField(max_length=100) 
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    concluida = models.BooleanField(default=False)
    #define key estrangeira de user, associa cada tarefa ao seu user,
    #definindo q quando o user for deletado; as tarefas tamém serão.
    dono = models.ForeignKey(User, related_name='tarefas', on_delete=models.CASCADE)

    #define o método e o retorno da tarefa em string.
    def __str__(self):
        return self.titulo
