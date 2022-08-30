from django.test import TestCase
from aluraflix.models import Programa
"""Testando os models"""

class ProgramaModelTestCase(TestCase): 
    #teste de unidade
    def setUp(self):
        self.programa = Programa(
            titulo='tal tal tal',
            data_lancamento = '2002-08-05'
        )
    

    def test_verifica_atributos_do_programa(self):
        """Verifica atributos de um programa com valores default"""
        self.assertEqual(
            self.programa.titulo,
            'tal tal tal'
        )
        self.assertEqual(
            self.programa.tipo,
            'F'
        )
        self.assertEqual(
            self.programa.data_lancamento,
            '2002-08-05'
        )
        self.assertEqual(
            self.programa.likes,
            0
        )
        self.assertEqual(
            self.programa.dislikes,
            0
        )


    
    # def test_fail(self):
    #     self.fail('Teste Falhou!')
