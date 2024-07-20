#Este arquivo configura as rotas principais do projeto Django,
#como:'admin',registra model no painel administrativo.
#'include', define,inclui, padrões de urls do django.
#'HttpResponseRedirect', redireciona um HTTP p url diferente.
#'simplejwt', importa e fornece funções (JOSON WEb Token)
#'get_schema_view',visuali esquema do swagger/OpenApi.
#'tarefas.views',cria user com personalidade.
#'openapi',módulo usado p configurar inf do OpneApi/swagger.
#'permissions',fornecer permissão p controle de acesso.
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView
)
from drf_yasg.views import get_schema_view
from tarefas.views import UserCreate
from drf_yasg import openapi
from rest_framework import permissions

#Esquema de informação p configuração do swagger/OpenAPI,
#'public-True', define como público, e q qualquer um
#pode pode acessar API.
schema_view = get_schema_view(
    openapi.Info(
        title="Tarefas API",
        default_version='v1',
        description="Documentação da API de Tarefas",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="gentilrn.65@hotmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

#Redirecionamento p URL/api.
def redirect_to_swagger(request):
    return HttpResponseRedirect('/api/')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', UserCreate.as_view(), name='user-create'),
    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),  
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),  
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/', include('tarefas.urls')),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    path('', redirect_to_swagger),
]
