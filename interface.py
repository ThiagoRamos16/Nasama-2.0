from PIL import Image
import customtkinter as ctk


ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue") 

janela = ctk.CTk()  
janela.title("Nasama") 
janela.geometry("700x700") 

titulo_icone = ctk.CTkLabel(janela, text="🎙️ Nasama", font=("Arial", 24, "bold"))
titulo_icone.place(relx=0.45, rely=0.10, anchor="center") 


def trocar_tema():
    if switch_tema.get() == 1:
        ctk.set_appearance_mode("light")
        switch_tema.configure(text="Light")   
    else:
        ctk.set_appearance_mode("dark")
        switch_tema.configure(text="Dark")   




frame_tema = ctk.CTkFrame(
    janela,
    fg_color=("#cbd5e1", "#334155"),
    corner_radius=20,
    width=140,
    height=45
)
frame_tema.place(relx=0.85, rely=0.05, anchor="center")

switch_tema = ctk.CTkSwitch(
    frame_tema,
    text="Dark",              
    font=("Arial", 14, "bold"),              
    text_color=("#1e293b", "white"),  
    command=trocar_tema,
    onvalue=1,
    offvalue=0
)
switch_tema.place(relx=0.5, rely=0.5, anchor="center")


tamanho = 160 # tamanho do circulo
circulo = ctk.CTkFrame(
    janela,
    width=tamanho,
    height=tamanho,
    corner_radius=tamanho // 2,
    fg_color= "#2563eb"
)
circulo.place(relx=0.5, rely=0.35, anchor="center")


image = ctk.CTkImage(
    light_image=Image.open("images/image.png"),
    size=(80,80)
)

icone = ctk.CTkLabel(
    circulo,
    text="",
    image=image
)
icone.place(relx=0.5, rely=0.5, anchor="center")


bolinha = ctk.CTkLabel(
    janela,
    text="●",
    font=("Arial", 40),
    text_color="green"
)
bolinha.place(relx=0.44, rely=0.52, anchor="center")

# texto status
status = ctk.CTkLabel(
    janela,
    text="Aguardando...",
    font=("Arial", 16, "bold"),
)
status.place(relx=0.55, rely=0.52, anchor="center")

def atualiza_status(estado):
    if estado == "ouvindo":
        bolinha.configure(text_color="green")
        status.configure(text="Ouvindo...")
    elif estado == "falando":
        bolinha.configure(text_color="blue")
        status.configure(text="Falando...")
    elif estado == "aguardando":
        bolinha.configure(text_color="gray")
        status.configure(text="Aguardando...")


animando = False

def pulsar(aumentando=True):
    global animando
    if not animando:
        return
    
    tamanho_atual = int(circulo.cget("width"))
    
    if aumentando:
        novo_tamanho = tamanho_atual + 2
        if novo_tamanho >= 180:
            aumentando = False
    else:
        novo_tamanho = tamanho_atual - 2
        if novo_tamanho <= 160:
            aumentando = True
    
    circulo.configure(
        width=novo_tamanho, 
        height=novo_tamanho,
        corner_radius=novo_tamanho // 2 
    )
    janela.after(30, lambda: pulsar(aumentando))

def inicia_animacao():
    global animando
    animando = True
    janela.after(0, pulsar)

def para_animacao():
    global animando
    animando = False
    janela.after(0, lambda: circulo.configure(
        width=160, 
        height=160,
        corner_radius=80
    ))

# HISTORICO
historico = ctk.CTkTextbox(
    janela,
    width=400,           
    height=150,                         
    font=("Arial", 14),
    state="disabled",
    corner_radius=15, 
    fg_color=("#dbeafe", "#1e293b"), 
    text_color=("#1e293b", "#e2e8f0"), 
    border_width=1,
    border_color=("#93c5fd", "#334155") 
)
historico.place(relx=0.5, rely=0.75, anchor="center")

def adiciona_historico(quem, mensagem):
    historico.configure(state="normal")
    historico.insert("end", f"{quem}: {mensagem}\n")
    historico.configure(state="disabled")
    



# Botão de Fechar 
botao_encerrar = ctk.CTkButton(
    janela,
    text="✕ Encerrar",
    width=120,
    height=40,
    font=("Arial", 14, "bold"),
    fg_color=("#ef4444", "#dc2626"),
    hover_color=("#dc2626", "#b91c1c"),
    corner_radius=20,
    command=janela.destroy
)
botao_encerrar.place(relx=0.5, rely=0.92, anchor="center")



# janela.mainloop()