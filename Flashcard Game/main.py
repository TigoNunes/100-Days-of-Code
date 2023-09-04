from tkinter import *
import pandas as pd
from random import choice
GREEN = "#00FA9A"
repetidor_tempo = None

# -------------------------Retirar palavras conhecidas-------------------------
def retira_palavras():
    """Remove as palavras que o usuário já conhece"""
    global palavra_aleatoria,dicionario
    dicionario.pop(palavra_aleatoria)
    

# -------------------------Rotação de palavras-------------------------
def mudar_palavra():
    """Muda a plavra que está na tela"""
    global palavra_aleatoria
    janela.after_cancel(repetidor_tempo)

    palavra_aleatoria = choice(list(dicionario.keys()))
    canvas.itemconfig(carta, image = imagem_card_front)
    canvas.itemconfig(texto_lingua, text="Franch", fill = "Black")
    canvas.itemconfig(texto_palavra, text=f"{palavra_aleatoria}", fill = "Black")

    timer()

def mudar_palavra_acerto():
    """Muda a plavra que está na tela, chama o método retira_palavras"""
    global palavra_aleatoria
    janela.after_cancel(repetidor_tempo)

    palavra_aleatoria = choice(list(dicionario.keys()))
    canvas.itemconfig(carta, image = imagem_card_front)
    canvas.itemconfig(texto_lingua, text="Franch", fill = "Black")
    canvas.itemconfig(texto_palavra, text=f"{palavra_aleatoria}", fill = "Black")  

    retira_palavras()
    timer()
    
# -------------------------Rotação carta-------------------------
def rotacao_carta():
    """Muda a imagem de plano de fundo e os escritos na tela"""
    canvas.itemconfig(carta, image = imagem_card_back)
    canvas.itemconfig(texto_palavra, text=f"{dicionario[palavra_aleatoria]}", fill = "White")
    canvas.itemconfig(texto_lingua, text="English", fill = "White")


# -------------------------timer-------------------------
def timer(tempo = 3):
    """Conta o tempo para que a tela seja atualizada"""
    global repetidor_tempo
    if tempo > 0:
        repetidor_tempo = janela.after(1000, timer, tempo - 1)
    else:
        rotacao_carta()

# -------------------------Dados-------------------------
try: 
    dados = pd.read_csv("Flashcard Game/data/Palavras desconhecidas.csv")
except FileNotFoundError:
    dados = pd.read_csv("Flashcard Game/data/french_words.csv")

dicionario = {conteudo.French:conteudo.English for (_,conteudo) in dados.iterrows()}

palavra_aleatoria = choice(list(dicionario.keys()))

# -------------------------Janela-------------------------

janela = Tk()
janela.title("Flashcard game")
janela.config(padx= 50, pady= 50, bg = GREEN)

# -------------------------Imagens-------------------------

imagem_card_back = PhotoImage(file="Flashcard Game/images/card_back.png")
imagem_card_front = PhotoImage(file="Flashcard Game/images/card_front.png")
imagem_botao_acerto = PhotoImage(file="Flashcard Game/images/right.png")
imagem_botao_erro = PhotoImage(file="Flashcard Game/images/wrong.png")

# -------------------------Canvas-------------------------

canvas = Canvas(width=800, height= 526, bg=GREEN, highlightthickness = 0)
carta = canvas.create_image(405, 270, image = imagem_card_front)
texto_lingua = canvas.create_text(400, 150, text= "Franch", font=("Arial", 40, "italic"))
texto_palavra = canvas.create_text(400, 263, text=f"{palavra_aleatoria}", font=("Arial", 60, "bold"))

canvas.grid(column=0, row=0, columnspan= 2)

# -------------------------Botões-------------------------

botao_acerto = Button(image= imagem_botao_acerto, highlightthickness=0, pady=50, command=mudar_palavra_acerto)
botao_acerto.grid(column=1, row=1)

botao_erro = Button(image= imagem_botao_erro, highlightthickness=0, pady=50, command=mudar_palavra)
botao_erro.grid(column=0, row=1)

# -------------------------Funções padrões-------------------------

timer()
janela.mainloop()

# -------------------------Salvando palavras desconhecidas-------------------------
palavras_desconhecidas = {
    "French": [keys for (keys,value) in dicionario.items()],
    "English": [values for (keys, values) in dicionario.items()]
}

aruivo_palavras_desconhecidas = pd.DataFrame(palavras_desconhecidas)
aruivo_palavras_desconhecidas.to_csv("Flashcard Game/data/Palavras desconhecidas.csv")

