#Este arquivo define os serializadores para os modelos User e Tarefa,
#usando Django REST Framework. Os serializadores são usados 
#para converter instâncias de modelos Django em representações 
#JSON e vice-versa.

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Tarefa


#define o serializer pro modelo user, convertendo
#as instâncias em JSON ou vice-versa.
class UserSerializer(serializers.ModelSerializer):
    
    #chama a classe 'Metadados' pra definir o modelo 'user',
    #'fields'especifica quais campos, 'extra_kwargs'argumentos
    #apenas de escrita e não exibe junto c/json(output).
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    #método pra criar um novo user, recebe a instância do
    #serializer e os dados validados.  'create_user'cria a
    #nova instância do user, Hashiza a senha e salva no db. 
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

#define o serializer pro modelo tarefa, convertendo
#as instâncias em JSON ou vice-versa.
class TarefaSerializer(serializers.ModelSerializer):
    
    #chama a classe 'Metadados' pra definir o modelo 'tarefa',
    #'fields'especifica quais campos, e define o campo
    #dono somente leitura.
    class Meta:
        model = Tarefa
        fields = ['id', 'titulo', 'descricao',
                  'data_criacao', 'concluida', 'dono']
        read_only_fields = ['dono']
