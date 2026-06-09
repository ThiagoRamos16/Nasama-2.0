from requests import get
from dotenv import load_dotenv
import os

load_dotenv()

CHAVE_API = os.getenv("OPENWEATHER_API_KEY")

def temperatura(cidade):
    try:
        if not CHAVE_API:
            return "A chave da API de clima não foi configurada."
        
        url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={CHAVE_API}&units=metric&lang=pt_br'
        resposta = get(url)
        dados = resposta.json()
        
        if dados['cod'] == 404:
            return f'Não encontrei a cidade {cidade}. Fale novamente um nome de alguma cidade que queira saber o clima.'
        
        
        temp = round(dados['main']['temp'])  
        sensacao = round(dados['main']['feels_like'])  
        umidade = dados['main']['humidity'] 
        descricao = dados['weather'][0]['description']

        return f'Em {cidade} a temperatura é {temp} graus, sensação térmica de {sensacao} graus, umidade de {umidade} por cento e o céu está {descricao}'
    except:
        return f'Não consegui buscar o clima de {cidade}, tente novamente'

