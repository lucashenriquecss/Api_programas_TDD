from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status
class AuthenticationUserTestCase(APITestCase):
    """Teste de  integração"""

    def setUp(self):
        self.listen_url = reverse('programas-list')
        self.user = User.objects.create_user('teste', password='test123')

    def test_auth_user_com_credenciais_corretas(self):
        """verifica a auth do usuario com credenciais corretas"""
        user= authenticate(username='teste', password='test123')
        self.assertTrue((user is not None) and user.is_authenticated)
    def test_requisicao_nao_autorizada(self):
        """VERIFICA UMA REQUISIÇÃO GET SEM AUTENTICAR"""
        response = self.client.get(self.listen_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    def test_auth_username_incorreto(self):
        """Verifica a username se esta incorreta"""
        user= authenticate(username='teste2', password='test123')
        self.assertFalse((user is not None) and user.is_authenticated)
    def test_auth_password_incorreto(self):
        """Verifica a password se esta incorreta"""
        user= authenticate(username='teste', password='test123w')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_requisicao_get_com_user_auth(self):
        """teste verifica requisição get de um user autenticado"""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.listen_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)