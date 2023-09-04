import turtle
import pandas

tela = turtle.Screen()
tela.title("Jogo dos estados dos EUA")

imagem = "Dia 25/Jogo Estados EUA/Arquivos/blank_states_img.gif"

tela.addshape(imagem)

turtle.shape(imagem)
dados = pandas.read_csv("Dia 25/Jogo Estados EUA/Arquivos/50_states.csv")
acertos = []
estados = dados["state"].to_list()

while len(acertos) < 50:
    resposta = tela.textinput(title= f"{len(acertos)}/50 estados", prompt= "Qual o próximo estado?r").title()

    if resposta in estados:
        acertos.append(resposta)
        estados.remove(resposta)
        texto = turtle.Turtle()
        texto.penup()
        texto.hideturtle()
        dados_estado = dados[dados["state"] == resposta]
        texto.goto(int(dados_estado["x"]), int(dados_estado["y"]))
        texto.write(resposta)
    elif resposta == "Sair":        
        break

estados_nao_acertados = {
    "estados perdidos": estados
}

novo_csv = pandas.DataFrame(estados_nao_acertados)
novo_csv.to_csv("Dia 25/Jogo Estados EUA/Arquivos/ estados_não_acertados.csv")

tela.exitonclick()

