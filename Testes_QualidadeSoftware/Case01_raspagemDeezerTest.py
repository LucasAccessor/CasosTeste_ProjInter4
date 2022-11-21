from utils import DataAccessLayer, SqlUtils, formatarNomeMusica
import unittest
from sqlalchemy import text

mock_musicas_cantores = [{
        "id": 0,
        "nome": "Eu Gosto Assim (Ao Vivo)",
        "posicao": 1,
        "lista_cantores": [
            {
                "id": 0,
                "nome": "Gustavo Mioto"
            },
            {
                "id": 0, "nome": "Mari Fernandez"
            }]
    },
    {
        "id": 0,
        "nome": "Haja Colírio (feat. Hugo & Guilherme) (Ao Vivo)",
        "posicao": 2,
        "lista_cantores": [
            {
                "id": 0,
                "nome": "Guilherme & Benuto"
            },
            {
                "id": 0,
                "nome": "Hugo & Guilherme"
            }]
    }]

class TestUtils(unittest.TestCase):

    def test_inserir_musicas(self):
        self.dal = DataAccessLayer("mysql+mysqlconnector://root:root@localhost/teste")
        self.utils = SqlUtils(self.dal)
        result = self.utils.inserirMusicas(mock_musicas_cantores)
        self.assertTrue(isinstance(result, int))
    
    def test_formatar_nome_musica(self):
        mock_nome = "ASDASD ASD ASD"
        self.assertEqual(formatarNomeMusica(mock_musicas_cantores), "")
