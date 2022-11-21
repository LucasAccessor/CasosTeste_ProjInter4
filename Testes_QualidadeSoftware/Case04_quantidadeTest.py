import unittest
from codigo_deezer import getMusicas
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


class TesteQuantidade(unittest.TestCase):
    def teste(self):
        driver = webdriver.Chrome()

        musicas = getMusicas(driver)
        print(musicas)

        driver.close()

        self.assertEqual(len(musicas), 20, "Quantidade incorreta de musicas coletadas")

if __name__ == '__main__':
    #run all test
    unittest.main() 