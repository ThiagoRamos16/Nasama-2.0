# 🎙️ Nasama 2.0 — Assistente Virtual com IA Conversacional

Evolução da Nasama com inteligência artificial generativa integrada!

> O nome **Nasama** é uma homenagem aos meus 3 pets: **Na**ni, **Sa**ndy e **Ma**ya. 🐾

## 🆕 Mudanças da v2.0

| Recurso | v1.0 | v2.0 |
|---|---|---|
| **Voz** | gTTS (robótica) | Edge TTS (natural) |
| **Inteligência** | Comandos fixos | IA Conversacional |
| **Memória** | ❌ | ✅ Lembra seu nome |
| **Personalidade** | Genérica | Própria personalidade |
| **Comandos** | Exatos | Linguagem natural |

## 🚀 Funcionalidades

- 🤖 **IA Conversacional** — responde qualquer pergunta com Groq
- 🎙️ **Voz Natural** — síntese de voz com Edge TTS
- 📝 **Memória** — lembra seu nome entre conversas
- ⏰ **Hora** — "qual a hora?", "me diga as horas", "horário"
- 📧 **Email** — "enviar email", "mandar mensagem"
- 💵 **Cotações** — dólar, euro, bitcoin em tempo real
- 📰 **Notícias** — busca em 5 sites (Google, Globo, UOL, BBC, Folha)
- 🌡️ **Clima** — temperatura de qualquer cidade
- 🖥️ **Sistema** — desligar computador, cancelar desligamento
- 🌓 **Interface** — dark mode / light mode
- 💬 **Histórico** — conversa salva na tela

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Edge-TTS](https://img.shields.io/badge/Edge--TTS-7.2.8-green?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-API-orange?style=for-the-badge)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-2.2-purple?style=for-the-badge)

- **Edge TTS** — síntese de voz natural
- **SpeechRecognition** — reconhecimento de voz
- **Groq API** — IA generativa (llama-3.1-8b-instant)
- **CustomTkinter** — interface moderna
- **BeautifulSoup** — web scraping de notícias
- **Requests** — consumo de APIs

## 📁 Estrutura

nasama-2.0/
│
├── .env.example          # exemplo de configuração
├── .gitignore
│
├── files/
│   ├── senha             # não incluso — senha de app do Gmail
│   ├── contatos.json     # não incluso — agenda de contatos
│   └── memoria.json      # não incluso — memória do usuário
│
├── images/
│   └── image.png         # ícone da interface
│
├── screenshots/
│   ├── dark.png          # interface tema dark
│   └── light.png         # interface tema light
│
├── funcoes_clima.py      # temperatura por cidade
├── funcoes_cotacao.py    # cotação de moedas
├── funcoes_email.py      # envio de e-mail por voz
├── funcoes_groq.py       # integração com Groq AI
├── funcoes_noticias.py   # notícias de 5 fontes RSS
├── funcoes_so.py         # funções do sistema operacional
├── interface.py          # interface gráfica
├── nasama.py             # arquivo principal
├── requirements.txt
└── README.md

---

## ⚙️ Configuração

### 1. Clone o repositório
```bash
git clone https://github.com/ThiagoRamos16/Nasama-2.0.git
cd Nasama-2.0
```

### 2. Instale as dependências
```bash
py -3.12 -m pip install -r requirements.txt
```

### 3. Configure as variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto:
GROQ_API_KEY=sua_chave_aqui
OPENWEATHER_API_KEY=sua_chave_aqui

Obtenha as chaves gratuitamente:
- Groq: https://console.groq.com
- OpenWeather: https://openweathermap.org

### 4. Senha do Gmail
Crie o arquivo `files/senha` com sua senha de app do Gmail.
Veja como gerar: [Senhas de app Google](https://myaccount.google.com/apppasswords)

### 5. Agenda de contatos
Crie o arquivo `files/contatos.json`:
```json
{
    "exemplo": "exemplo@gmail.com",
    "exemplo2": "exemplo2@gmail.com"
}
```

### 6. Execute
> ⚠️ **Recomendado: Python 3.12** — versões mais recentes podem ter incompatibilidade com o PyAudio.

```bash
# Windows com múltiplas versões Python
py -3.12 nasama.py

# Outros sistemas
python nasama.py
```

---

## 🗣️ Exemplos de comandos

| Comando | Ação |
|---|---|
| *"que horas são?"* | Informa a hora atual |
| *"enviar email"* | Inicia o fluxo de envio de e-mail por voz |
| *"notícias"* | Pergunta a fonte e lê as 3 últimas notícias |
| *"quanto está o dólar?"* | Informa a cotação do Dólar |
| *"cotação do euro"* | Informa a cotação do Euro |
| *"bitcoin"* | Informa a cotação do Bitcoin |
| *"temperatura em SP"* | Informa o clima atual |
| *"desligar em uma hora"* | Agenda desligamento em 1 hora |
| *"cancelar desligamento"* | Cancela o desligamento agendado |
| *"fechar assistente"* | Encerra a Nasama |
| *Qualquer pergunta livre* | Groq AI responde! |

---

## ⚠️ Segurança

Os arquivos `files/senha`, `files/contatos.json`, `files/memoria.json` e o `.env` **não estão no repositório** por segurança. Utilize sempre senha de app do Gmail, nunca a senha principal.

---

## 🔮 Próximas versões

- [ ] Integração com N8N (Nasama 3.0)
- [ ] Controle do computador via IA (PyAutoGUI)
- [ ] Avatar animado (estilo Alexa)
- [ ] Integração com Google Calendar
- [ ] Multi-idioma

---

## 👨‍💻 Autor

**Thiago Ramos da Silva**
[linkedin.com/in/thiagoramosdasilva](https://linkedin.com/in/thiagoramosdasilva)

---

**Versão anterior:** [Nasama 1.0](https://github.com/ThiagoRamos16/Nasama-1.0)