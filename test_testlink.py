from pages.github_page import GitHubPage
from pages.testlink_page import TestlinkPage

tlPage = TestlinkPage()
gitHubPage = GitHubPage()

##===== Página do TestLink =======##

tlPage.acessarTestlink()

titulo = tlPage.tituloPagina()
cabecalho = tlPage.encontrarElementoXpath('//h1').text

assert titulo == "TestLink"
assert cabecalho == 'TestLink Open Source Test Management'

tlPage.clicarRepositorioGit() # Apartir daqui, seremos direcionado para o GitHub


##===== Página do GitHub do Projeto =======#

# Algumas verificações na página do GitHub
autor       = tlPage.encontrarElementoXpath(gitHubPage.XPATH_AUTOR).text
repositorio = tlPage.encontrarElementoXpath(gitHubPage.XPATH_REPOSITORIO).text

assert autor == 'TestLinkOpenSourceTRMS'
assert repositorio == 'testlink-code'

# Pesquisar a palavra 'Opcional' no GitHub
gitHubPage.pesquisar('Opcional')
quantRepo = gitHubPage.encontrarElementoXpath('//nav[1]/a/span[@*=\'Code\']').text

print("Quantidade de resultados neste repositório: " + quantRepo)

# Fecha o navegador
gitHubPage.fecharBrowser()