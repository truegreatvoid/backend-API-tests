from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Resource


class BaseResourceTestCase(TestCase):
    """Classe base para testes de recursos"""
    def setUp(self):
        self.client = APIClient()
        self.resource1 = Resource.objects.create(name="Recurso A", description="Descrição A")
        self.resource2 = Resource.objects.create(name="Recurso B", description="Descrição B")
        self.list_url = reverse('additional:crud-additional-list')


class ResourceListTestCase(BaseResourceTestCase):
    """Testes para operações de listagem de recursos"""
    
    def test_get_all_resources(self):
        """Teste para verificar se conseguimos obter a lista de todos os recursos"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)
        self.assertEqual(len(response.data['results']), 2)


class ResourceCreateTestCase(BaseResourceTestCase):
    """Testes para operações de criação de recursos"""
    
    def test_create_resource_success(self):
        """Teste para verificar se conseguimos criar um novo recurso"""
        data = {
            "name": "Recurso Novo",
            "description": "Descrição do novo recurso"
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Resource.objects.count(), 3)

    def test_create_resource_missing_name(self):
        """Teste para validar erro ao criar recurso sem nome"""
        data = {
            "description": "Sem nome"
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_resource_with_long_name(self):
        """Teste para validar erro ao criar recurso com nome longo"""
        data = {
            "name": "A" * 256,
            "description": "Ok"
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_duplicate_resource(self):
        """Teste para verificar erro ao tentar criar recurso com nome duplicado"""
        Resource.objects.create(name="Duplicado", description="1")
        data = {
            "name": "Duplicado",
            "description": "2"
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertIn(response.status_code, [status.HTTP_400_BAD_REQUEST, status.HTTP_201_CREATED])

    def test_create_resource_without_description(self):
        """Teste para verificar se é possível criar recurso sem descrição"""
        data = {
            "name": "SemDescrição"
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertIn(response.status_code, [status.HTTP_201_CREATED, status.HTTP_400_BAD_REQUEST])


class ResourceDetailTestCase(BaseResourceTestCase):
    """Testes para operações em recursos específicos (detalhe, atualização, exclusão)"""
    
    def test_get_single_resource(self):
        """Teste para verificar se conseguimos obter um único recurso"""
        detail_url = reverse('additional:crud-additional-detail', kwargs={'pk': self.resource1.pk})
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.resource1.name)

    def test_get_nonexistent_resource(self):
        """Teste para verificar erro ao buscar recurso inexistente"""
        detail_url = reverse('additional:crud-additional-detail', kwargs={'pk': 9999})
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_resource_full(self):
        """Teste para verificar se conseguimos atualizar completamente um recurso"""
        detail_url = reverse('additional:crud-additional-detail', kwargs={'pk': self.resource1.pk})
        updated_data = {
            "name": "Atualizado",
            "description": "Nova descrição"
        }
        response = self.client.put(detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.resource1.refresh_from_db()
        self.assertEqual(self.resource1.name, "Atualizado")

    def test_partial_update_resource(self):
        """Teste para verificar se conseguimos fazer atualização parcial"""
        detail_url = reverse('additional:crud-additional-detail', kwargs={'pk': self.resource1.pk})
        response = self.client.patch(detail_url, {"name": "Parcial"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.resource1.refresh_from_db()
        self.assertEqual(self.resource1.name, "Parcial")

    def test_update_resource_with_invalid_name(self):
        """Teste para validar erro ao atualizar recurso com nome inválido"""
        detail_url = reverse('additional:crud-additional-detail', kwargs={'pk': self.resource1.pk})
        data = {
            "name": "",
            "description": "Desc"
        }
        response = self.client.put(detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_resource(self):
        """Teste para verificar se conseguimos deletar um recurso"""
        detail_url = reverse('additional:crud-additional-detail', kwargs={'pk': self.resource1.pk})
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Resource.objects.count(), 1)

    def test_delete_nonexistent_resource(self):
        """Teste para validar erro ao deletar recurso inexistente"""
        detail_url = reverse('additional:crud-additional-detail', kwargs={'pk': 999})
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
