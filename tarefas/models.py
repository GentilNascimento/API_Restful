from django.db import models
from django.contrib.auth.models import User


class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    concluida = models.BooleanField(default=False)
    dono = models.ForeignKey(User, related_name='tarefas', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
