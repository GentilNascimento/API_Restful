from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Tarefa
from .serializers import TarefaSerializer
from django.http import HttpResponse


class TarefaListCreate(generics.ListCreateAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(dono=self.request.user)


class TarefaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(dono=self.request.user)


def home(request):
    return HttpResponse("Página Inicial")
