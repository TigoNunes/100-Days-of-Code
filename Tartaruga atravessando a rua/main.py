from turtle import Screen
import time
from tartaruga import Tartaruga
from carro import Carro
from nivel import Nivel

tela = Screen()
tela.setup(width= 600, height= 600)
tela.title("Atravessar a rua")
tela.listen()
tela.tracer(0)

tartaruga = Tartaruga()
nivel = Nivel()

pos_carro = 9 # Variavel que controla a posição dos carros no eixo x
carros = []
for i in range(20): #instância os carros 
    carro = Carro(pos_carro)
    carros.append(carro)
    if pos_carro == 0:
        pos_carro = 9
    else:
        pos_carro -=1

tela.onkey(fun= tartaruga.mover_tartaruga, key= "w") 

jogo_on = True

while jogo_on:
    tela.update()
    time.sleep(nivel.dificuldade)

    for carro in carros:
        carro.mover()
    
    # Verifica se os carros atravessaram a tela
    for carro in carros:
        if carro.carro[1].xcor() < -301:
            carro.retorna_carro(pos_carro)

            if pos_carro == 0:
                pos_carro = 9
            else:
                pos_carro -= 1

    # Verifica se a tartaruga atravessou a rua
    if tartaruga.ycor() > 280:
        tartaruga.posciao_inicial()
        nivel.nivel += 1
        nivel.mostrar_nivel()
        nivel.dificulde_jogo()

        for carro in carros:
            carro.novo_nivel(pos_carro)

            if pos_carro == 0: pos_carro = 9
            else: pos_carro -= 1

    # Verifica se a tartaruga bateu em um carro
    for carro in carros:
        for parte in carro.carro:
            if tartaruga.distance(parte) < 15:
                jogo_on = False
                nivel.fim_de_jogo()

tela.exitonclick()