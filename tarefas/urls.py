from rest_framework import permissions
from django.urls import path
from .views import UserCreate, TarefaListCreate, TarefaRetrieveUpdateDestroy
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Tarefas-API",
        default_version='v1',
        description="Documentação da API de Tarefas",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="gentilrn.65@hotmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('register/', UserCreate.as_view(), name='users-register-create'),
    path('', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    path('tarefas/', TarefaListCreate.as_view(), name='tarefa-list-create'),
    path('tarefas/<int:pk>/', TarefaRetrieveUpdateDestroy.as_view(),
         name='tarefa-retrieve-update-destroy'),
]
