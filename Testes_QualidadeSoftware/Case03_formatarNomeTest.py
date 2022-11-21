import unittest
from codigo_deezer import formatarNomeMusica # code from module you're testing


class SimpleTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCerto(self):
        posicao = 1
        musica = '1. Pipoco'
        valor_esperado = 'Pipoco'
        valor_real = formatarNomeMusica(posicao, musica)
        self.assertEqual(valor_esperado , valor_real, f"Erro, valor errado, valor esperado: {valor_esperado}, valor real: {valor_real}")

    def testErrado(self):
            posicao = 1
            musica = '1. Pipoco'
            valor_esperado = ' Pipoco'
            valor_real = formatarNomeMusica(posicao, musica)
            self.assertEqual(valor_esperado , valor_real, "Erro, o valor errado foi aceito como correto")


    #def testB(self):
     #   """test case B"""
      #  assert foo+foo == 34, "can't add Foo instances"

if __name__ == "__main__":
    unittest.main() # run all tests