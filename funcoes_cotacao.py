from requests import get
from datetime import datetime

def cotacao_moeda(moeda):
    data_consulta = datetime.now().strftime("%d/%m/%Y às %H:%M")
    if moeda == "Dólar":
        requisicao = get('https://economia.awesomeapi.com.br/json/last/USD-BRL')
        cotacao = requisicao.json()
        nome = cotacao['USDBRL']['name']
        valor = cotacao['USDBRL']['bid']
        mensagem = f'Cotação do {nome} consultada em {data_consulta}, último valor registrado: {valor} reais'
    elif moeda == "Euro":
        requisicao = get('https://economia.awesomeapi.com.br/json/last/EUR-BRL')
        cotacao = requisicao.json()
        nome = cotacao['EURBRL']['name']
        valor = cotacao['EURBRL']['bid']
        mensagem = f'Cotação do {nome} consultada em {data_consulta}, último valor registrado: {valor} reais'
    elif moeda == "Bitcoin":
        requisicao = get('https://economia.awesomeapi.com.br/json/last/BTC-BRL')
        cotacao = requisicao.json()
        nome = cotacao['BTCBRL']['name']
        data = cotacao['BTCBRL']['create_date']
        valor = cotacao['BTCBRL']['bid']
        mensagem = f'Cotação do {nome} consultada em {data_consulta}, último valor registrado: {valor} reais'
    return mensagem
    
