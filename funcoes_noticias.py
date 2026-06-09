from requests import get
from bs4 import BeautifulSoup

def ultimas_noticias(fonte="google"):
    
    fontes = {
        "google": "https://news.google.com/rss?gl=BR&hl=pt-BR&ceid=BR:pt-419",
        "globo":  "https://g1.globo.com/rss/g1/",
        "uol":    "https://rss.uol.com.br/feed/noticias.xml",
        "bbc":    "https://feeds.bbci.co.uk/portuguese/rss.xml",
        "folha":  "https://feeds.folha.uol.com.br/emcimadahora/rss091.xml"
    }
    
    url = fontes.get(fonte, fontes["google"])
    site = get(url)
    noticias = BeautifulSoup(site.content, 'xml')
    
    titulos = []
    for item in noticias.find_all('item')[1:4]:
        titulos.append(item.title.text)
    
    mensagem = "Aqui estão as últimas notícias.\n"
    for i, titulo in enumerate(titulos, 1):
        mensagem += f"Notícia {i}: {titulo}\n"
    
    return mensagem
