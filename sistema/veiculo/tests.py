from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from datetime import datetime
from veiculo.models import *
from veiculo.forms import *

class TestesModelVeiculo(TestCase):
    '''
    Classe de testes para o model Veículo
    '''
    def setUp(self):
        self.instancia = Veiculo(
            marca=1,
            modelo='Modelo Teste',
            ano=datetime.now().year,
            cor=2,
            combustivel=3
        )
    def test_veiculo_novo(self):
        self.assertTrue(self.instancia.veiculo_novo)
        self.instancia.ano = datetime.now().year - 5
        self.assertFalse(self.instancia.veiculo_novo)

    def test_anos_de_uso(self):
        self.instancia.ano = datetime.now().year - 10
        self.assertEqual(self.instancia.anos_de_uso(), 10)

class TestesViewListarVeiculos(TestCase):
    '''
    Classe de testes para a view ListarVeiculos
    '''
    def setUp(self):
        self.user = User.objects.create(username='teste', password='12345')
        self.client.force_login(self.user)
        self.url = reverse('listar-veiculos')
        Veiculo(marca=1, modelo='Modelo A', ano=2020, cor=1, combustivel=1).save()
        
    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['lista_veiculos']), 1)
 
class TestesViewCriarVeiculos(TestCase):
    '''
    Classe de testes para a view CriarVeiculos
    '''
    def setUp(self):
        self.user = User.objects.create(username='teste', password='12345')
        self.client.force_login(self.user)
        self.url = reverse('criar-veiculos')

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('form'), FormularioVeiculo)

    def test_post(self):
        dados = {
            'marca': 1,
            'modelo': 'Modelo B',
            'ano': 2021,
            'cor': 2,
            'combustivel': 3,
        }
        response = self.client.post(self.url, dados)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-veiculos'))
        self.assertEqual(Veiculo.objects.count(), 1)
        self.assertEqual(Veiculo.objects.first().marca, 1)
        self.assertEqual(Veiculo.objects.first().modelo, 'Modelo B')
        self.assertEqual(Veiculo.objects.first().ano, 2021)
        self.assertEqual(Veiculo.objects.first().cor, 2)
        self.assertEqual(Veiculo.objects.first().combustivel, 3)

class TestesViewEditarVeiculo(TestCase):
    '''
    Classe de testes para a view EditarVeiculo
    '''
    def setUp(self):
        self.user = User.objects.create(username='teste', password='12345')
        self.client.force_login(self.user)
        self.instancia = Veiculo.objects.create(marca=1, modelo='Modelo Teste', ano=2020, cor=1, combustivel=1)
        self.url = reverse('editar-veiculos', kwargs={'pk': self.instancia.pk})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('object'), Veiculo)
        self.assertIsInstance(response.context.get('form'), FormularioVeiculo)
        self.assertEqual(response.context.get('object').pk, self.instancia.pk)

    def test_post(self):
        dados = {
            'marca': 2,
            'modelo': 'Modelo Editado',
            'ano': 2022,
            'cor': 2,
            'combustivel': 2,
        }
        response = self.client.post(self.url, dados)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-veiculos'))
        self.assertEqual(self.instancia.marca, 2)
        self.assertEqual(Veiculo.objects.count(), 1)
        self.assertEqual(Veiculo.objects.first().pk, self.instancia.pk)

class TestesViewDeletarVeiculos(TestCase):
    '''
    Classe de testes para a view DeletarVeiculos
    '''
    def setUp(self):
        self.user = User.objects.create(username='teste', password='12345')
        self.client.force_login(self.user)
        self.instancia = Veiculo.objects.create(marca=1, modelo='Modelo Teste', ano=2020, cor=1, combustivel=1)
        self.url = reverse('deletar-veiculos', kwargs={'pk': self.instancia.pk})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-veiculos'))
        self.assertEqual(Veiculo.objects.count(), 0)

    def test_post(self):
        response = self.client.post(self.url)

        #Verifica se o redirecionamento ocorreu corretamente
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-veiculos'))
        self.assertEqual(Veiculo.objects.count(), 0)