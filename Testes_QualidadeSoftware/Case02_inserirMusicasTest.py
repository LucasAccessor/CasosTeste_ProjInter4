import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from datetime import date
import unittest

from codigo_deezer import inserirMusica, inserirMusicas

engine = create_engine('mysql+mysqlconnector://root:root@localhost/vcharts')

def inserirMusicas(musicas):
	contador = 0
	with Session(engine) as sessao, sessao.begin():
		for musica in musicas:
			musica["id"] = inserirMusica(sessao, musica)

			sessao.execute(text("INSERT INTO musicaData (idMusica, posicao, dt) VALUES (:idMusica, :posicao, :dt)"), {
				"idMusica": musica["id"],
				"posicao": musica["posicao"],
				"dt": date.today()
			})
			print("musica inserida")
			contador = contador + 1


class inserirTest(unittest.TestCase):
	def teste(self):
		musicas = [{"id": 0,
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
		inserirMusicas(musicas)

if __name__ == "__main__":
    unittest.main() # run all tests