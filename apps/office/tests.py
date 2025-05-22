from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Office


class BaseOfficeTestCase(TestCase):
    """Classe base para testes de escritórios"""
    def setUp(self):
        self.client = APIClient()
        
        self.office1 = Office.objects.create(
            name="Escritório 1",
            cnpj="12345678901234", 
            location="Localização do escritório 1",
            phone="1234567890",
            rooms=5
        )
        self.office2 = Office.objects.create(
            name="Escritório 2",
            cnpj="98765432100123", 
            location="Localização do escritório 2",
            phone="31234567890",
            rooms=3
        )
       
        self.list_url = reverse('office:crud-office-list')


class OfficeListTestCase(BaseOfficeTestCase):
    """Testes para operações de listagem de escritórios"""
    
    def test_get_all_offices(self):
        """Teste para verificar se conseguimos obter a lista de todos os escritórios"""
        response = self.client.get(self.list_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)
        self.assertEqual(len(response.data['results']), 2)


class OfficeCreateTestCase(BaseOfficeTestCase):
    """Testes para operações de criação de escritórios"""
    
    def test_create_office_with_cnpj(self):
        """Teste para verificar se conseguimos criar um novo escritório com CNPJ"""
        data = {
            "name": "Novo Escritório CNPJ",
            "cnpj": "11111111000111",
            "location": "Nova localização",
            "phone": "11987654321",
            "rooms": 10
        }
        
        response = self.client.post(self.list_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Office.objects.count(), 3)
        self.assertEqual(response.data['name'], "Novo Escritório CNPJ")
        self.assertEqual(response.data['rooms'], 10)
    
    def test_create_invalid_office_missing_required_fields(self):
        """Teste para verificar validação ao criar escritório sem campos obrigatórios"""
        data = {
            "location": "Localização sem nome e CNPJ"
        }
        
        response = self.client.post(self.list_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Office.objects.count(), 2)
    
    def test_create_office_duplicate_cnpj(self):
        """Teste para verificar validação de CNPJ duplicado"""
        data = {
            "name": "Escritório Duplicado",
            "cnpj": "12345678901234",  # CNPJ já usado pelo office1
            "location": "Nova localização",
            "phone": "11987654321",
            "rooms": 5
        }
        
        response = self.client.post(self.list_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Office.objects.count(), 2)


class OfficeDetailTestCase(BaseOfficeTestCase):
    """Testes para operações em escritórios específicos (detalhe, atualização, exclusão)"""
    
    def test_get_single_office(self):
        """Teste para verificar se conseguimos obter um único escritório"""
        detail_url = reverse('office:crud-office-detail', kwargs={'pk': self.office1.pk})
        response = self.client.get(detail_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.office1.name)
        self.assertEqual(response.data['cnpj'], self.office1.cnpj)
        self.assertEqual(response.data['location'], self.office1.location)
        self.assertEqual(response.data['rooms'], self.office1.rooms)
    
    def test_update_office(self):
        """Teste para verificar se conseguimos atualizar um escritório"""
        detail_url = reverse('office:crud-office-detail', kwargs={'pk': self.office1.pk})
        updated_data = {
            "name": "Escritório 1 Atualizado",
            "cnpj": "12345678901234",
            "location": "Nova localização",
            "phone": "1199999999",
            "rooms": 8
        }
        
        response = self.client.put(detail_url, updated_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.office1.refresh_from_db()
        self.assertEqual(self.office1.name, "Escritório 1 Atualizado")
        self.assertEqual(self.office1.phone, "1199999999")
        self.assertEqual(self.office1.rooms, 8)
    
    def test_delete_office(self):
        """Teste para verificar se conseguimos deletar um escritório"""
        detail_url = reverse('office:crud-office-detail', kwargs={'pk': self.office1.pk})
        response = self.client.delete(detail_url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Office.objects.count(), 1)
    
    def test_get_nonexistent_office(self):
        """Teste para verificar o comportamento ao tentar obter um escritório que não existe"""
        non_existent_id = 999
        detail_url = reverse('office:crud-office-detail', kwargs={'pk': non_existent_id})
        response = self.client.get(detail_url)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class OfficeFilterSearchTestCase(BaseOfficeTestCase):
    """Testes para funcionalidades de busca e filtros"""
    
    def test_search_office_by_name(self):
      """Teste para verificar a funcionalidade de busca por nome"""
      search_url = f"{self.list_url}?search=Escritório 1"
      response = self.client.get(search_url)
      
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      matching_offices = [office for office in response.data['results'] 
                        if 'Escritório 1' in office['name']]
      self.assertEqual(len(matching_offices), 1)
      self.assertEqual(response.data['results'][0]['name'], "Escritório 1")
    
    def test_search_office_by_cnpj(self):
        """Teste para verificar a funcionalidade de busca por CNPJ"""
        search_url = f"{self.list_url}?search=12345678901234"
        response = self.client.get(search_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['cnpj'], "12345678901234")


class OfficeValidationTestCase(BaseOfficeTestCase):
    """Testes específicos de validação de escritórios"""
    
    def test_office_name_max_length(self):
        """Teste para verificar validação de tamanho máximo do nome (255 caracteres)"""
        data = {
            "name": "A" * 256,
            "cnpj": "11111111000111",
            "location": "Localização válida",
            "phone": "11987654321",
            "rooms": 5
        }
        
        response = self.client.post(self.list_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Office.objects.count(), 2)
    
    def test_office_cnpj_max_length(self):
        """Teste para verificar validação de tamanho máximo do CNPJ (18 caracteres)"""
        data = {
            "name": "Escritório Teste",
            "cnpj": "1" * 19,
            "location": "Localização válida",
            "phone": "11987654321",
            "rooms": 5
        }
        
        response = self.client.post(self.list_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Office.objects.count(), 2)