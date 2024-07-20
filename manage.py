#(os)-Módulo padrão do Python q fornece maneiras de usar
#funcionalidades do sistema operacional manipulando
#variáveis de ambiente.
#(sys)-Módulo que fornece funções e variáveis que podem 
#ser usadas p manipular partes do ambiente de execução.
import os
import sys


#A variável/ambiente, informa ao Django o arquivo de configurações,
#q deve ser usado para o projeto,(trilhabackendjr).
#"import execute", do django.core, pra analisar o comando
#e executar a tarefa.
#"except", se falhar por um erro de importação; informa
#que o django não pode ser importado.
#"sys.argv", executa o script passado na linha de comando.
#"if_name", verifica se o script foi executado direto e não
#importado igual módulo, se assim for chama main(). 
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trilhabackendjr.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
