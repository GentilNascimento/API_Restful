from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tarefas.urls')),  # incluir URLS aplicação'tarefas'
    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),  # URL obter token JWT
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),  # URL renova token JWT
    path('', include('tarefas.urls')),  # URLS de 'tarefas' para URL raiz
]
