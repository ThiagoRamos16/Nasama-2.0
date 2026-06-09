import os
from datetime import datetime

def verifica_hora():
    hora = datetime.now().strftime("%H:%M")
    frase = f"Agora são {hora}"
    return frase


def desliga_computador_uma_hora():
    os.system('shutdown /s /t 3600')
    
def desliga_computador_meia_hora():
    os.system('shutdown /s /t 1800')
    
def cancela_desligamento():
    os.system('shutdown /a')