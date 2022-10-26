from selenium.webdriver.common.keys import Keys
from pages.page import Page

class GitHubPage(Page):
    def __init__(self):
        super().__init__()
        self.XPATH_AUTOR = '//a[@rel=\'author\']'
        self.XPATH_REPOSITORIO = '//a[@rel=\'author\']/../../strong/a'
        self.XPATH_PESQUISA = '//form/label/input[1]'


    def pesquisar(self, pesquisa):
        self.pesquisarNoInput(self.XPATH_PESQUISA, pesquisa)