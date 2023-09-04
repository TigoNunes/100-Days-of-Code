
import time
from turtle import Screen
from jogador import Jogador
from bola import Bola
from divisoria import Divisoria
from placar import Placar

tela = Screen()
tela.setup(width= 800, height= 600)
tela.bgcolor("black")
tela.title("Pong")
tela.listen()
tela.tracer(0)



jogador1 = Jogador(1)
jogador2 = Jogador(2)
bola = Bola()
divisoria = Divisoria()
placar_p1 = Placar(-100)
placar_p2 = Placar(100)

# controle jogadores
tela.onkey(fun= jogador1.cima, key= "w")
tela.onkey(fun= jogador1.baixo, key= "s")

tela.onkey(fun= jogador2.cima, key= "Up")
tela.onkey(fun= jogador2.baixo, key= "Down")

jogo_rolando = True

while jogo_rolando:
    bola.mover()
    tela.update()

    if bola.ycor() > 280 or bola.ycor() < -280:
        bola.quicar()
    
    for parte in range(len(jogador1.jogador)):
        if bola.distance(jogador1.jogador[parte]) < 20 or bola.distance(jogador2.jogador[parte]) < 20:
            bola.mudar_direcao()
        
    if bola.xcor() > 390:
        placar_p1.pontos += 1
        bola.resetar()
        placar_p1.placar_pontos()
    elif bola.xcor() < -390:
        placar_p2.pontos += 1
        bola.resetar()
        placar_p2.placar_pontos()

    if placar_p1.pontos == 5 or placar_p2.pontos == 5:
        jogo_rolando = False
    

    time.sleep(bola.velocidade)
    

tela.exitonclick()