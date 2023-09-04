from turtle import Turtle,Screen
import random

class Corrida:    
    corrida_valendo = False
    tela = Screen()
    tela.setup(width= 500, height= 400)
    aposta = tela.textinput(title="Faça a suaaposta",prompt="Qual tartarua vencera a corrida? Escolha umacor: ")

    tartarugas = []
    cores = ["red", "orange", "yellow", "green", "blue", "indigo"]

    for i in range(0, 6):
        nova_tartaruga = Turtle(shape= "turtle")
        nova_tartaruga.color(cores[i])
        nova_tartaruga.penup()
        nova_tartaruga.goto(x = -230, y = -100 + (i * 33.33))
        tartarugas.append(nova_tartaruga)


    if aposta:
        corrida_valendo = True

    while corrida_valendo == True:
        for i in range(len(tartarugas)):
            tartarugas[i].forward(random.randint(1,10))
            if tartarugas[i].xcor() >= 235:
                vencedor = tartarugas[i].color()
                vencedor = vencedor[0]
                corrida_valendo = False
                break
        
    if aposta == str(vencedor): print(f"Vitória! a tartarua gencedora foi a {vencedor}")
    else: print(f"Derrota! a tartarua gencedora foi a {vencedor}")    

    tela.exitonclick()