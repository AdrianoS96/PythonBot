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

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)

driver.get('https://www.google.com.br/')
campo = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input' )
campo.send_keys(pesquisa)
campo.send_keys(Keys.RETURN)

resultados = driver.find_element(By.ID, 'result-stats').text
print(resultados)

numero_resultados = int(resultados.split('Aproximadamente ')[1].split(' resultados')[0].replace('.','')) #está pegando a string e filtrando para ficar só o número enquanto retira os '.' para não dar erro na conversão
maximo_paginas = numero_resultados / 10

print('Número de páginas: %s'% (maximo_paginas))

url_pagina = driver.find_element(By.XPATH, "//a[@aria-label='Page 2']").get_attribute('href')

pagina_atual = 0
startP = 0

while pagina_atual < 9:
    if not pagina_atual == 0:
        url_pagina = url_pagina.replace('start=%s' % startP, 'start=%s' % (startP+10))
        startP += 10
        driver.get(url_pagina)
    

    divs = driver.find_elements(By.XPATH, "//div[@class='g']")
    divs = divs + driver.find_elements(By.XPATH, "//div[contains(@class, 'g ')]")
    sleep(2)
    for div in divs:
        try:
            titulo = div.find_element(By.TAG_NAME, 'h3')
            link = div.find_element(By.TAG_NAME, 'a').get_attribute('href')
            resultado = '%s  ||  %s' % (titulo.text, link)
            print(resultado)
        except:
            print('Informações não encontradas!')
    pagina_atual += 1