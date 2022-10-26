from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Page(object):
    driver = webdriver.Firefox()
    
    def __init__(self):
        self.driver.implicitly_wait(10)

    def acessarURL(self, url):
        self.driver.get(url)

    def encontrarElementoXpath(self, xpath):
        elemento = self.driver.find_element(By.XPATH, xpath)
        return elemento

    def tituloPagina(self):
        titulo = self.driver.title
        return titulo

    def pesquisarNoInput(self, xpathInput, pesquisa):
        inputPesquisa = self.encontrarElementoXpath(xpathInput)
        inputPesquisa.send_keys(pesquisa)
        inputPesquisa.send_keys(Keys.RETURN)

    def fecharBrowser(self):
        self.driver.close()