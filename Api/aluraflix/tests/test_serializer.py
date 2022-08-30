from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer

class ProgramaSerializerTestCase(TestCase):

    def setUp(self):
        self.programa = Programa(
            titulo='tal tal tal',
            data_lancamento = '2002-08-05',
            tipo='F',
            likes=200,
            dislikes=50
        )
        self.serializer = ProgramaSerializer(
            instance=self.programa,
        )
    def test_verifica_campos_serializer_do_programa(self):
        data =self.serializer.data
        self.assertEqual(set(data.keys()), set(['titulo','tipo','data_lancamento','likes']))


    def test_verifica_conteudo_dos_campos_serializados(self):
        """Verifica conteudo dos campos serializers"""   
        data =self.serializer.data
        self.assertEqual(data['titulo'], self.programa.titulo)
        self.assertEqual(data['tipo'], self.programa.tipo)
        self.assertEqual(data['data_lancamento'], self.programa.data_lancamento)
        self.assertEqual(data['likes'], self.programa.likes)


