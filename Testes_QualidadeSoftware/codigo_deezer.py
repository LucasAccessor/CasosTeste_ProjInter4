# Instalar o virtualenv de forma global:
# python -m pip install virtualenv
#
# Criar o ambiente virtual na pasta do projeto:
# virtualenv .venv
#
# Para ativar o ambiente:
# .venv\Scripts\activate
#
# Depois disso, instalar os pacotes nesse ambiente virtual:
# python -m pip install xxx
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

engine = create_engine('mysql+mysqlconnector://root:root@localhost/vcharts')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--force-device-scale-factor=0.5")
driver = webdriver.Chrome(options=chrome_options)

def getMusicas():
	lista = []

	for i in range(20):
		index = i+1
		
		musica = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.XPATH, f"//*[@id='page_naboo_playlist']/div[1]/div/div[3]/div[2]/div/div/div[{i+1}]/div/div[1]/div[4]/div/span"))
		)

		musica = formatarNomeMusica(index, musica.text)
        
		cantores = WebDriverWait(driver, 10).until(
			EC.presence_of_all_elements_located((By.XPATH, f'//*[@id="page_naboo_playlist"]/div[1]/div/div[3]/div[2]/div/div/div[{i+1}]/div/div[2]/div/a'))
		)
	
		lista_cantores = []

		for cantor in cantores:
		 	lista_cantores.append({
				"id": 0,
				"nome": cantor.accessible_name
			})

    	lista.append({
            "id": 0,
            "nome": musica,
            "posicao": index,
            "lista_cantores": lista_cantores
        })
	return lista


def formatarNomeMusica(posicao, musica):
	posicao = str(posicao) + '. '
	if posicao in musica:
		nomeMusica = musica.replace(posicao, '', 1)

	return nomeMusica

def botaoCookies():
    botao = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='gdpr-btn-accept-all']"))
    )
    
    botao.click()

def inserirCantor(sessao, cantor):
	cantorExistente = sessao.execute(text("SELECT idCantor FROM cantor WHERE nomeCantor = :nomeCantor"), {
		"nomeCantor": cantor["nome"]
	}).first()

	if cantorExistente == None:
		sessao.execute(text("INSERT INTO cantor (nomeCantor) VALUES (:nomeCantor)"), {
			"nomeCantor": cantor["nome"]
		})

		cantorExistente = sessao.execute(text("SELECT last_insert_id() idCantor")).first()

	return cantorExistente.idCantor;

def inserirMusica(sessao, musica):
	musicaExistente = sessao.execute(text("SELECT idMusica FROM musica WHERE nomeMusica = :nomeMusica"), {
		"nomeMusica": musica["nome"]
	}).first()

	if musicaExistente == None:
		sessao.execute(text("INSERT INTO musica (nomeMusica) VALUES (:nomeMusica)"), {
			"nomeMusica": musica["nome"]
		})

		musicaExistente = sessao.execute(text("SELECT last_insert_id() idMusica")).first()

		for cantor in musica["lista_cantores"]:
			cantor["id"] = inserirCantor(sessao, cantor)

			sessao.execute(text("INSERT INTO musica_cantor (idMusica, idCantor) VALUES (:idMusica, :idCantor)"), {
				"idMusica": musicaExistente.idMusica,
				"idCantor": cantor["id"]
			})

	return musicaExistente.idMusica;

def inserirMusicas(musicas):
	with Session(engine) as sessao, sessao.begin():
		for musica in musicas:
			musica["id"] = inserirMusica(sessao, musica)

			sessao.execute(text("INSERT INTO musicaData (idMusica, posicao, dt) VALUES (:idMusica, :posicao, :dt)"), {
				"idMusica": musica["id"],
				"posicao": musica["posicao"],
				"dt": date.today()
			})

if __name__ == '__main__':

    driver.get('https://www.deezer.com/br/playlist/1111141961')

    botaoCookies()

    maisTocadas = getMusicas()    

    print("Top Brazil: ")
    print("As mais ouvidas na Deezer a cada dia.")
    for musicaMaisTocada in maisTocadas:
        print(musicaMaisTocada)

    driver.close()

    inserirMusicas(maisTocadas)