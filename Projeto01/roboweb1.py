# https://pypi.org/project/webdriver-manager/  ***site para consulta sobre webdriver***
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By #importar BY para o funcionamento do comando
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

options = webdriver.ChromeOptions()
options.add_argument("--disable-logging") 
options.add_argument("--log-level=3")

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)
driver.get('https://registro.br')

pesquisa = driver.find_element(By.ID,'is-avail-field') # O ELEMENTO DO SITE QUE SERÁ UTILIZADO
pesquisa.clear() # LIMPA O CAMPO, APAGANDO Todo O TEXTO
pesquisa.send_keys('coletivodosaber.com.br') # DIGITA O TEXTO ENTRE '' NO CAMPO
pesquisa.send_keys(Keys.RETURN) # APERTA A TECLA ENTER
time.sleep(5)
driver.close()
