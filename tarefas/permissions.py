#Este código define uma permissão personalizada para a API REST,
#usando Django REST Framework. O 'IsOwner' garante que apenas,
#o dono do objeto tenha acesso.

#módulo pra criar permissões personalizadas.
from rest_framework import permissions

#classe personalizada, que verifica se user tem permissão
#a classe, requisição, view, e é o dono do objeto atual,
#caso contrário, é negada.
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.dono == request.user

