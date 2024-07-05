from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from tarefas.views import UserCreate
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

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


def redirect_to_swagger(request):
    return HttpResponseRedirect('/api/')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),  # URL obter token JWT
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),  # URL renova token JWT
    path('api/register/', UserCreate.as_view(), name='user-register'),
    path('api/', include('tarefas.urls')),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', 
         cache_timeout=0), name='schema-redoc'),
    path('', redirect_to_swagger),
]
