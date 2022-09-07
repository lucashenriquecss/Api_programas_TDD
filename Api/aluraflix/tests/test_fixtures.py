from django.test import TestCase
from aluraflix.models import Programa

class FixturesDataTestCase(TestCase):

    fixtures = ['programas_iniciais']

    def test_carregar_fixtures(self):
        programa_bizarro = Programa.objects.get(pk=1)
        todos_programa = Programa.objects.all()
        self.assertEqual(programa_bizarro.titulo, 'Coisas bizarras') #verificando se o nome é esse
        self.assertEqual(len(todos_programa), 9) #verificando se realmente tem 9 filmes

