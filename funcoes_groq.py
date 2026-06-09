from groq import Groq
import json
import os
from dotenv import load_dotenv

load_dotenv()

chave = os.getenv("GROQ_API_KEY")
cliente = Groq(api_key=chave)

historico_conversa = []

def salva_memoria(nome):
    with open('files/memoria.json', 'w') as f:
        json.dump({'nome': nome}, f)
        
        
def carrega_memoria():
    try:
        with open('files/memoria.json', 'r') as f:
            return json.load(f)
    except:
        return None
    

def responde_ia(pergunta):
    
    historico_conversa.append(
        {
            'role' : 'user',
            'content' : pergunta
        }
    )
    
    resposta = cliente.chat.completions.create(
        model='llama-3.1-8b-instant',
        messages=[
            {
                'role': 'system',
                'content': 'Você é a Nasama (pronuncia-se Na-sa-ma), uma assistente virtual simpática e divertida. O usuário se chama {nome_usuario}. Fale sempre em português brasileiro de forma curta e direta. Seja amigável e use emojis com moderação.'
            },
        ] + historico_conversa[-6:]
    )
    texto = resposta.choices[0].message.content
    historico_conversa.append(
        {
            'role': 'assistant',
            'content' : texto
        }
    )
    return texto

def comenta_informacao(informacao):
    resposta = cliente.chat.completions.create(
        model='llama-3.1-8b-instant',
        messages=[
            {
                'role': 'system',
                'content': 'Você é a Nasama. Comente a informação de forma curta e natural em português brasileiro. Não invente dados.'
            },
            {
                'role': 'user',
                'content': informacao
            }
        ]
    )
    return resposta.choices[0].message.content