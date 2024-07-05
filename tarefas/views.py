from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, permissions, status, serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Tarefa, User
from .serializers import TarefaSerializer, UserSerializer
from django.http import HttpResponse
from .permissions import IsOwner
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


#view pra registrar novo usuário
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
    
#serializer registra novo usuário
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
    

        
        
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def criar_tarefa(request):
    serializer = TarefaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(dono=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def atualizar_tarefa(request, pk):
    try:
        tarefa = Tarefa.objects.get(pk=pk, dono=request.user)
    except Tarefa.DoesNotExist:
        return Response({'error': 'Tarefa não encontrada ou não pertence ao usuário'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = TarefaSerializer(tarefa, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def excluir_tarefa(request, pk):
    try:
        tarefa = Tarefa.objects.get(pk=pk, dono=request.user)
    except Tarefa.DoesNotExist:
        return Response({'error': 'Tarefa não encontrada ou não pertence ao usuário'}, status=status.HTTP_404_NOT_FOUND)
    
    tarefa.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class TarefaListCreate(generics.ListCreateAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(dono=self.request.user)


class TarefaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def perform_update(self, serializer):
        serializer.save(dono=self.request.user)


def home(request):
    return HttpResponse("Página Inicial")
