from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By #importar BY para o funcionamento do comando
from selenium.webdriver.chrome.service import Service #Para utilizar os serviços para o chromeDrive na nuvem
from webdriver_manager.chrome import ChromeDriverManager#para gerenciar o chromedrive da nuvem
from time import sleep

pesquisa = input('Digite a sua pesquisa: ')

options = webdriver.ChromeOptions()
options.add_argument("--disable-logging") 
options.add_argument("--log-level=3")

'''necessário a criação de comandos para cada navegador
   até o momento se mostra funcional'''

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)
driver2 = webdriver.Chrome(service=s, options=options)

driver.get('https://www.google.com.br/')
driver2.get('https://www.google.com.br/')
campo1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input' )
campo = driver2.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input' )
campo1.send_keys(pesquisa)
campo.send_keys(pesquisa)
sleep(10)