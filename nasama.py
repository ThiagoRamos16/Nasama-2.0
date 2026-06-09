import edge_tts
import asyncio
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import speech_recognition as sr
import sys
import funcoes_so
import funcoes_email
import funcoes_cotacao
import funcoes_noticias
import funcoes_clima
import funcoes_groq
import threading
import interface
import time
import re

def limpa_texto(texto):
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"
        u"\U0001F300-\U0001F5FF"
        u"\U0001F680-\U0001F9FF"
        u"\U00002702-\U000027B0"
        "]+", flags=re.UNICODE)
    return emoji_pattern.sub('', texto).strip()


async def gera_audio(texto, arquivo):
    tts = edge_tts.Communicate(texto, voice = "pt-BR-FranciscaNeural")
    await tts.save(arquivo)

def cria_audio(audio, mensagem):
    asyncio.run(gera_audio(mensagem, audio))
    pygame.mixer.init()
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    pygame.mixer.quit()
    os.remove(audio)
    

def monitora_audio(executar_comando=True):
    recon = sr.Recognizer()
    with sr.Microphone() as source:
        recon.adjust_for_ambient_noise(source, duration=1)
        while True:
            print("Diga alguma coisa")
            
            try:
                audio = recon.listen(source, timeout=10, phrase_time_limit=10)
                mensagem = recon.recognize_google(audio, language= 'pt-br')
                mensagem = mensagem.lower()
                print("Você disse: ", mensagem)
                interface.adiciona_historico("Você", mensagem)
            
                if executar_comando:
                    executa_comandos(mensagem)
                break
            except sr.WaitTimeoutError:
                interface.atualiza_status("falando")
                interface.inicia_animacao()
                cria_audio("erro.mp3", "Não ouvi nada. Pode repetir?.")
                interface.adiciona_historico("Nasama", "Não ouvi nada. Pode repetir?")
                interface.para_animacao()
                interface.atualiza_status("ouvindo")
            except sr.UnknownValueError:
                interface.atualiza_status("falando")
                interface.inicia_animacao()
                cria_audio("erro.mp3", "Não consegui entender. Tente novamente.")
                interface.adiciona_historico("Nasama", "Não consegui entender. Tente novamente.")
                interface.para_animacao()
                interface.atualiza_status("ouvindo")
            except sr.RequestError:
                interface.atualiza_status("falando")
                interface.inicia_animacao()
                cria_audio("erro.mp3", "Erro ao conectar ao serviço de reconhecimento.")
                interface.adiciona_historico("Nasama", "Erro ao conectar ao serviço de reconhecimento.")
                interface.para_animacao()
                interface.atualiza_status("ouvindo")
        return mensagem 
    

def executa_comandos(acao):
    if 'fechar assistente' in acao or 'fechar' in acao and 'assistente' in acao:
        interface.janela.after(0, interface.janela.destroy)
        sys.exit()

    # ✅ HORAS — aceita variações
    elif any(palavra in acao for palavra in ['hora', 'horas', 'que horas', 'horário', 'horario']):
        hora = funcoes_so.verifica_hora()
        interface.atualiza_status("falando")
        interface.inicia_animacao()
        interface.adiciona_historico("Nasama", hora)
        cria_audio('mensagem.mp3', hora)
        interface.para_animacao()
        interface.atualiza_status("ouvindo")

    # ✅ EMAIL — aceita variações
    elif any(palavra in acao for palavra in ['enviar email', 'enviar e-mail', 'mandar email', 'mandar e-mail', 'email', 'e-mail']):
        interface.atualiza_status("ouvindo")
        status_email = funcoes_email.enviar_email(cria_audio, monitora_audio)
        interface.atualiza_status("falando")
        interface.inicia_animacao()
        interface.adiciona_historico("Nasama", status_email)
        cria_audio('mensagem.mp3', status_email)
        interface.para_animacao()
        interface.atualiza_status("ouvindo")

    # ✅ DESLIGAR — aceita variações
    elif any(palavra in acao for palavra in ['desligar', 'desliga']) and any(palavra in acao for palavra in ['uma hora', '1 hora', 'sessenta minutos']):
        interface.atualiza_status("falando")
        interface.inicia_animacao()
        interface.adiciona_historico("Nasama", "Computador será desligado em uma hora")
        cria_audio('mensagem.mp3', "Computador será desligado em uma hora.")
        funcoes_so.desliga_computador_uma_hora()
        interface.para_animacao()
        interface.atualiza_status("ouvindo")

    elif any(palavra in acao for palavra in ['desligar', 'desliga']) and any(palavra in acao for palavra in ['meia hora', '30 minutos', 'trinta minutos']):
        interface.atualiza_status("falando")
        interface.inicia_animacao()
        interface.adiciona_historico("Nasama", "Computador será desligado em meia hora.")
        cria_audio('mensagem.mp3', "Computador será desligado em meia hora.")
        funcoes_so.desliga_computador_meia_hora()
        interface.para_animacao()
        interface.atualiza_status("ouvindo")

    # ✅ CANCELAR DESLIGAMENTO
    elif any(palavra in acao for palavra in ['cancelar desligamento', 'cancela desligamento', 'não desligar', 'cancela']):
        interface.atualiza_status("falando")
        interface.inicia_animacao()
        interface.adiciona_historico("Nasama", "Desligamento cancelado.")
        cria_audio('mensagem.mp3', "Desligamento cancelado.")
        funcoes_so.cancela_desligamento()
        interface.para_animacao()
        interface.atualiza_status("ouvindo")

    # ✅ COTAÇÕES — aceita variações
    elif any(palavra in acao for palavra in ['dólar', 'dolar', 'dollar', 'cotação do dólar', 'quanto está o dólar']):
        interface.atualiza_status("falando")
        interface.inicia_animacao()
        cotacao = funcoes_cotacao.cotacao_moeda("Dólar")
        interface.adiciona_historico("Nasama", cotacao)
        cria_audio('mensagem.mp3', cotacao)
        interface.para_animacao()
        interface.atualiza_status("ouvindo")

    elif any(palavra in acao for palavra in ['euro', 'euros', 'cotação do euro', 'quanto está o euro']):
        interface.atualiza_status("falando")
        interface.inicia_animacao()
        cotacao = funcoes_cotacao.cotacao_moeda("Euro")
        interface.adiciona_historico("Nasama", cotacao)
        cria_audio('mensagem.mp3', cotacao)
        interface.para_animacao()
        interface.atualiza_status("ouvindo")

    elif any(palavra in acao for palavra in ['bitcoin', 'btc', 'cotação do bitcoin', 'quanto está o bitcoin']):
        interface.atualiza_status("falando")
        interface.inicia_animacao()
        cotacao = funcoes_cotacao.cotacao_moeda("Bitcoin")
        interface.adiciona_historico("Nasama", cotacao)
        cria_audio('mensagem.mp3', cotacao)
        interface.para_animacao()
        interface.atualiza_status("ouvindo")

    # ✅ NOTÍCIAS — aceita variações
    elif any(palavra in acao for palavra in ['notícia', 'noticia', 'notícias', 'noticias', 'novidade', 'novidades']):
        interface.atualiza_status("falando")
        interface.inicia_animacao()
        cria_audio('mensagem.mp3', 'De qual site você quer as notícias? Google, Globo, UOL, BBC ou Folha?')
        interface.para_animacao()
        interface.atualiza_status("ouvindo")

        resposta = monitora_audio(executar_comando=False)

        if 'globo' in resposta or 'g1' in resposta:
            fonte = "globo"
        elif 'bbc' in resposta:
            fonte = "bbc"
        elif 'uol' in resposta:
            fonte = "uol"
        elif 'folha' in resposta:
            fonte = "folha"
        else:
            fonte = "google"

        interface.atualiza_status("falando")
        interface.inicia_animacao()
        noticias = funcoes_noticias.ultimas_noticias(fonte)
        comentario = funcoes_groq.responde_ia(
            f"Leia esses títulos de notícias exatamente como estão, sem inventar detalhes, "
            f"apresentando de forma curta e natural: {noticias}"
        )
        interface.adiciona_historico("Nasama", comentario)
        cria_audio('mensagem.mp3', limpa_texto(comentario))
        interface.para_animacao()
        interface.atualiza_status("ouvindo")

    # ✅ CLIMA — aceita variações
    elif any(palavra in acao for palavra in ['clima', 'temperatura', 'tempo', 'previsão', 'previsao', 'faz calor', 'está frio']):
        while True:
            interface.atualiza_status("falando")
            interface.inicia_animacao()
            cria_audio('mensagem.mp3', 'Qual cidade deseja saber a temperatura?')
            interface.adiciona_historico("Nasama", "Qual cidade deseja saber a temperatura?")
            interface.para_animacao()
            interface.atualiza_status("ouvindo")

            cidade = monitora_audio(executar_comando=False)

            interface.atualiza_status("falando")
            interface.inicia_animacao()
            resultado = funcoes_clima.temperatura(cidade)
            interface.adiciona_historico("Nasama", resultado)
            cria_audio('mensagem.mp3', resultado)
            interface.para_animacao()
            interface.atualiza_status("ouvindo")

            if 'Não encontrei' not in resultado and 'Não consegui' not in resultado:
                break

    # ✅ IA RESPONDE TUDO QUE NÃO FOI RECONHECIDO
    else:
        resposta = funcoes_groq.responde_ia(acao)
        interface.atualiza_status("falando")
        interface.inicia_animacao()
        interface.adiciona_historico("Nasama", resposta)
        cria_audio('mensagem.mp3', limpa_texto(resposta))
        interface.para_animacao()
        interface.atualiza_status("ouvindo")
            

nome_usuario = None          

def main():
    thread_nasama = threading.Thread(target=inicia_nasama, daemon=True)
    thread_nasama.start()
    time.sleep(0.5) 
    interface.janela.mainloop()
    

def inicia_nasama():
    global nome_usuario
    
    memoria = funcoes_groq.carrega_memoria()
    
    if memoria:
        nome_usuario = memoria['nome']
        boas_vindas = funcoes_groq.responde_ia(f"Me dê as boas vindas de volta de forma simpática, o usuário se chama {nome_usuario}")
        interface.atualiza_status("falando")
        interface.inicia_animacao()
        cria_audio("wellcome.mp3", limpa_texto(boas_vindas))
        interface.para_animacao()
        interface.adiciona_historico("Nasama", boas_vindas)
        
    else: 
        interface.atualiza_status("falando")
        interface.inicia_animacao()
        cria_audio("wellcome.mp3", "Olá! Eu sou a Nasama. Qual o seu nome?")
        interface.adiciona_historico("Nasama", "Olá! Eu sou a Nasama. Qual o seu nome?")
        interface.para_animacao()
        interface.atualiza_status("ouvindo")
        nome_usuario = monitora_audio(executar_comando=False)
        funcoes_groq.salva_memoria(nome_usuario)
        interface.atualiza_status("falando")
        interface.inicia_animacao()
        apresentacao = funcoes_groq.responde_ia(f"Me apresente para {nome_usuario} de forma simpática e curta")
        cria_audio("mensagem.mp3", limpa_texto(apresentacao))
        interface.adiciona_historico("Nasama", apresentacao)
        interface.para_animacao()
        
    while True:                              
        interface.atualiza_status("ouvindo")
        monitora_audio()

main()