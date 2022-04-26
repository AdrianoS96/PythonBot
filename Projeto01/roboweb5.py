from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service #Para utilizar os serviços para o chromeDrive na nuvem
from webdriver_manager.chrome import ChromeDriverManager#para gerenciar o chromedrive da nuvem
import xlrd #para abrir arquivos excel
import time

"""
para retirar todo log de quando roda o código
# option = webdriver.ChromeOptions()
# options.add_argument('--disable-logging')
# options.add_argument('--log-level=3')
# driver = webdriver.Chrome(options = options)
"""

arq = open('Resultado.txt', 'w') #o python gera um arquivo com o nome especificado. o 'w' no final é de write para escrever
#funciona com .txt  .xls(tudo na mesma coluna)

workbook = xlrd.open_workbook('D:\Estudo Python\PythonBot\Projeto01\excel.xls') #entre '' coloca o caminho para o arquivo r Strings** utiliza o r antes das '' para o programa aceitar \
sheet = workbook.sheet_by_name('Plan1') # para mostrar para o programa qual a planilha do arquivo será utilizada
rows = sheet.nrows #variavel para fazer a contagem das linhas
columns = sheet.ncols #variavel para fazer contagem das colunas

options = webdriver.ChromeOptions()
options.add_argument("--disable-logging") 
options.add_argument("--log-level=3")

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)
driver.get('https://registro.br')

for curr_row in range(0, rows):
    conteudo = sheet.cell_value(curr_row, 0)
    pesquisa = driver.find_element(By.ID,'is-avail-field') # O ELEMENTO DO SITE QUE SERÁ UTILIZADO
    time.sleep(1)
    pesquisa.clear() # limpa o campo apagando texto
    time.sleep(1)
    pesquisa.send_keys(conteudo) # DIGITA O TEXTO ENTRE '' NO CAMPO
    time.sleep(1)
    pesquisa.send_keys(Keys.RETURN) # APERTA A TECLA ENTER
    time.sleep(2)

    driver.find_element(By.XPATH,'/html/body/div/main/section/div[2]/div/p/span/strong')
    disponibilidade = driver.find_element(By.XPATH,'/html/body/div/main/section/div[2]/div/p/span/strong').text #para pegar o texto do elemento. não usa os () no final
    resultado = f"Domínio: {conteudo}  Disponibilidade: {disponibilidade} \n"
    arq.write(resultado)
    time.sleep(1)

driver.close()