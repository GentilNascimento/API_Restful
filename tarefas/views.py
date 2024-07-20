#Importamos diversas funcionalidades do Django e do Django REST Framework,
#necessárias para a criação das views e manipulação das requisições.
#Tarefa e User, modelos importados de models.py.
#TarefaSerializer e UserSerializer, importados do serializers.py e o
#IsOwner, permissão personalizada q verifica se user logado é dono
#da tarefa. Swagger_auto_schema, ustilizado p documentar operações
#da API swagger.

from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Tarefa 
from .serializers import TarefaSerializer, UserSerializer
from django.http import HttpResponse
from .permissions import IsOwner
from drf_yasg.utils import swagger_auto_schema
 


#view pra registrar novo usuário.
#'queryset', define o conjunto de dados inicial contendo todos usuários.
#'serializer_class', converte os dados do usuário nos formatos
#usados pela API e db. 
#'permission_classes'(AllowAny), diz q qualquer pessoa pode criar
#novo usuário.
#'Post'é personalizado p criar novo user, decorado pelo 
#'swagger_auto_schema' c/ documentação automática. Requisita 
#'args/kwargs'argumentos, inclusive adicionais ou nomeados
#q possam ser passados posterior.
#'super', chama usercreate c/request junto c/os argumentos
#adicionais/nomeados p class usercreate.
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
    @swagger_auto_schema(
        operation_description="register_novo_usuario",
        tags=["Users"]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
 
#Requisitando 'post' p criar tarefa,'IsAuthenticated' diz q 
#precisa está autenticado pra acessar a view.'Serializer', 
#instancia TarefaSerializer c/dados da requisição, verifica 
#se dados são válidos, salva a nova tarefa e user como dono,
#'Response data',retorna status 201 criado, e 'Response erros'
#retorna status 400 como erro.    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def criar_tarefa(request):
    serializer = TarefaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(dono=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Requisitando 'put' p atualizar tarefa,'IsAuthenticated',diz q usuário 
#precisa está autenticado pra acessar a view.'Try...except', tenta
#a tarefa pelo pk/dono, se não retorna erro 404. 'TarefaSerializer',
#mostra tarefa c dados, verifica se são válidos, se sim, salva.
#'Response.data', retorna os dados atualz e 'Response.errors', os erros
#com status 400.

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def atualizar_tarefa(request, pk):
    try:
        tarefa = Tarefa.objects.get(pk=pk, dono=request.user)
    except Tarefa.DoesNotExist:
        return Response({'error': 'Tarefa não encontrada ou não pertence ao usuário'}, 
                        status=status.HTTP_404_NOT_FOUND)
    
    serializer = TarefaSerializer(tarefa, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Requisitando delete, 'IsAuthenticated', só users autenticado acessam
#essa view.'Try...except', tenta a tarefa pelo pk/dono, se não, retorna
#erro 404, se achar; exclui e retorna satatus (204-sem conteúdo)
#excluído com sucesso.
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def excluir_tarefa(request, pk):
    try:
        tarefa = Tarefa.objects.get(pk=pk, dono=request.user)
    except Tarefa.DoesNotExist:
        return Response({'error': 'Tarefa não encontrada ou não pertence ao usuário'}, 
                        status=status.HTTP_404_NOT_FOUND)
    
    tarefa.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
 
#view pra listar todas tarefas e criar novas.
#'queryset',define o conjunto de dados inicial contendo todas tarefas.
#'serializer_class', converte os dados da tarefa nos formatos
#usados pela API e db. 
#'permission_classes'(IsAuthenticated), diz q apenas user 
#autenticado/dono pode acessar a view. 
#'perform_create', Sobrescreve o método, ou seja; permite lógica
#personalizada ao criar outro objeto antes de salvar no db, e que o dono da tarefa seja o user autenticado da requisição. 
class TarefaListCreate(generics.ListCreateAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(dono=self.request.user)

#view pra recuperar, atualizar e excluir tarefa.
#'queryset',define o conjunto de dados inicial contendo todas tarefas.
#'serializer_class', converte os dados da tarefa nos formatos
#usados pela API e db. 
#'permission_classes'(IsAuthenticated/IsOwner), diz q apenas user 
#autenticado/dono pode acessar a view. 
#'perform_update',Sobrescreve o método, ou seja; permite lógica
#personalizada ao criar outro objeto, antes de salvar no db, e que o dono da tarefa seja o user autenticado da requisição.
class TarefaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def perform_update(self, serializer):
        serializer.save(dono=self.request.user)


#def home(request):
#    return HttpResponse("Página Inicial")
