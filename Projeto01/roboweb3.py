from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service #Para utilizar os serviços para o chromeDrive na nuvem
from webdriver_manager.chrome import ChromeDriverManager#para gerenciar o chromedrive da nuvem
import time

"""
para retirar todo log de quando roda o código
# option = webdriver.ChromeOptions()
# options.add_argument('--disable-logging')
# options.add_argument('--log-level=3')
# driver = webdriver.Chrome(options = options)
"""

dominios = ['coletivodosaber.com.br', 'hotmart.com.br', 'clubedobolinha.com.br', 'uol.com.br', 'pycursos.com.br']

options = webdriver.ChromeOptions()
options.add_argument("--disable-logging") 
options.add_argument("--log-level=3")

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)
driver.get('https://registro.br')

for dominio in dominios:

    pesquisa = driver.find_element(By.ID,'is-avail-field') # O ELEMENTO DO SITE QUE SERÁ UTILIZADO
    pesquisa.clear() # limpa o campo apagando texto
    pesquisa.send_keys(dominio) # DIGITA O TEXTO ENTRE '' NO CAMPO
    pesquisa.send_keys(Keys.RETURN) # APERTA A TECLA ENTER
    time.sleep(2)

    driver.find_element(By.XPATH,'/html/body/div/main/section/div[2]/div/p/span/strong')
    disponibilidade = driver.find_element(By.XPATH,'/html/body/div/main/section/div[2]/div/p/span/strong').text #para pegar o texto do elemento. não usa os () no final
    print(f"Domínio: {dominio} \n"
        f"Disponibilidade: {disponibilidade}")

driver.close()