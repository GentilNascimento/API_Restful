#Módulo padrão do Python q fornece maneiras de usar
#funcionalidades do sistema operacional manipulando
#variáveis de ambiente.
import os

#Especificação padrão p app web assíncronos em python/djando.
from django.core.asgi import get_asgi_application

#Define a variável de ambiente e aponta p django onde 
#tá as confg do projeto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trilhabackendjr.settings')

#Cria a aplicação ASGI, p interagir com aplicação django.
application = get_asgi_application()
