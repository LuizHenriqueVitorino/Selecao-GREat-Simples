from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Inicializa o driver e abre o navegador no endereço da aplicação
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('https://testlink.org/')

## Algumas verificações na página do Testlink
assert driver.title == "TestLink"
assert driver.find_element(By.XPATH, '//h1').text == 'TestLink Open Source Test Management'

##Clicar no link para o repositório no github
linkGit = driver.find_element(By.XPATH, '//a[.=\'Access Git Repository (GitHub)\']')
linkGit.click()

## Algumas verificações na página do GitHub
# Verificar o autor
assert driver.find_element(By.XPATH, '//a[@rel=\'author\']').text == 'TestLinkOpenSourceTRMS'
# Verifica o nome do repositório
assert driver.find_element(By.XPATH, '//a[@rel=\'author\']/../../strong/a').text == 'testlink-code'

# Pesquisar a palavra 'Opcional' no GitHub
pesquisa = driver.find_element(By.XPATH, '//form/label/input[1]')
pesquisa.send_keys('Opcional')
pesquisa.send_keys(Keys.RETURN)
quantRepo = driver.find_element(By.XPATH, '//nav[1]/a/span[@*=\'Code\']').text

sleep(5)
print("Quantidade de resultados neste repositório: " + quantRepo)



# driver.close()