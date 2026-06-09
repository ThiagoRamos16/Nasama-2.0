from email.message import EmailMessage
import smtplib
import ssl
import json
import interface

email_remetente = 'seuemail@gmail.com'
senha = open('files/senha', 'r').read()

def carrega_contatos():
    try:
        return json.load(open('files/contatos.json', 'r', encoding='utf-8'))
    except:
        return {}

def resolve_destinatario(texto, cria_audio, monitora_audio):
    contatos = carrega_contatos()
    
    palavras = texto.split()       
    for palavra in palavras:
        if palavra in contatos:      
            return contatos[palavra]
        
    cria_audio('mensagem.mp3', 'Contato não encontrado. Diga o endereço de e-mail completo.')
    return formata_email(monitora_audio(executar_comando=False))

def formata_email(texto): 
    texto = texto.replace(' arroba ', '@')
    texto = texto.replace(' ponto com', '.com')
    texto = texto.replace(' ponto ', '.')
    texto = texto.replace(' underline ', '_')
    
    partes = texto.split('@')
    if len(partes) == 2:
        texto = partes[0].replace(' ', '') + '@' + partes[1].strip()
    
    return texto.strip()

def enviar_email(cria_audio, monitora_audio): 
    try:
        interface.inicia_animacao()
        cria_audio('mensagem.mp3', 'Para quem deseja enviar o e-mail?')
        interface.para_animacao() 
        destinatario = resolve_destinatario(                          
            monitora_audio(executar_comando=False), cria_audio, monitora_audio
        )
        interface.inicia_animacao()  
        cria_audio('mensagem.mp3', 'Qual o assunto do e-mail?')
        interface.para_animacao() 
        assunto = monitora_audio(executar_comando=False)
        
        interface.inicia_animacao() 
        cria_audio('mensagem.mp3', 'Qual a mensagem?')
        interface.para_animacao()
        corpo = monitora_audio(executar_comando=False)

        message = EmailMessage()
        message['From'] = email_remetente
        message['To'] = destinatario
        message['Subject'] = assunto
        message.set_content(corpo)

        safe = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as servidor:  

            servidor.login(email_remetente, senha)
            servidor.sendmail(email_remetente, destinatario, message.as_string())

        interface.inicia_animacao() 
        interface.para_animacao()
        return "E-mail enviado com sucesso!"
        
    except Exception as e:
        interface.inicia_animacao()  
        interface.para_animacao()
        return f"Erro ao enviar e-mail: {str(e)}"
        


