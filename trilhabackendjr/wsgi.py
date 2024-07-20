#Módulo padrão do Python q fornece maneiras de usar
#funcionalidades do sistema operacional manipulando
#variáveis de ambiente.
import os

#Esta função cria uma aplicação WSGI para servir o
#projeto django. É uma espécie de caminho universal
#entre os servidores e app web.
from django.core.wsgi import get_wsgi_application

#Define a variável de ambiente e aponta p django onde 
#tá as confg do projeto.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trilhabackendjr.settings')

#Cria aplicação WSGI pra servir o projeto django, e
#encaminhar as solicitações HTTP ao projeto.
application = get_wsgi_application()
