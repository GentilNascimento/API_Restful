from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.urls import reverse
from tarefas.models import Tarefa


#testando db
class TarefaTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        # obter tokin JWT
        url = reverse('token_obtain_pair')
        response = self.client.post(
            url, {'username': 'testuser', 'password': 'testpass'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token = response.data['access']

    def test_create_tarefa(self):
        url = reverse('tarefa-list-create')
        data = {'titulo': 'Test Tarefa', 'descricao': 'Test Descricao'}

        # Adicionar token de autenticação no cabeçalho.
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tarefa.objects.count(), 1)
        self.assertEqual(Tarefa.objects.get().titulo, 'Test Tarefa')

    #testando listagem de tarefas
    def test_list_tarefas(self):
        Tarefa.objects.create(titulo='Test Tarefa', descricao='Test Descricao', dono=self.user)
        
        #fazendo uma requisição GET p/listar as tarefas
        url = reverse('tarefa-list-create')
        response = self.client.get(url, format='json')

        #verificando se a resposta tá correta
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['titulo'], 'Test Tarefa')

    #testando atualização da tarefa
    def test_update_tarefa(self):
        tarefa = Tarefa.objects.create(titulo='Test Tarefa', descricao='Test Descricao', dono=self.user)
        
        #fazer uma requisição PUT p/atualizar tarefa.
        url = reverse('tarefa-retrieve-update-destroy', args=[tarefa.id])
        data = {'titulo': 'Updated Tarefa', 'descricao': 'Updated Descricao'}
        self.client.credentials(HTTP_AUTHORIZATTION='Bearer ' + self.token)
        response = self.client.put(url, data, format='json')
        
        #verificando se resposta correta
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Tarefa.objects.get().titulo, 'Updated Tarefa')
        
    #testando exclusão da tarefa
    def test_delete_tarefa(self):
        tarefa = Tarefa.objects.create(titulo='Test Tarefa', descricao='Test Descricao', dono=self.user)
        
        #fazendo requisição'delete' p/excluir tarefa
        url = reverse('tarefa-retrieve-update-destroy', args=[tarefa.id])
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.delete(url, format='json')
        
        #verificando se resposta tá correta
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT) 
        self.assertEqual(Tarefa.objects.count(), 0)
        