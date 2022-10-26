from pages.page import Page

class TestlinkPage(Page):
    def __init__(self):
        super().__init__()
        self.XPATH_GIT = '//a[.=\'Access Git Repository (GitHub)\']'

    def acessarTestlink(self, url='https://testlink.org/'):
        self.acessarURL(url)

    def clicarRepositorioGit(self):
        elemento = self.encontrarElementoXpath(self.XPATH_GIT)
        elemento.click()