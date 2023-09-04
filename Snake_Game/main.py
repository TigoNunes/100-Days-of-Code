from turtle import Screen
from cobra import Cobra
from comida import Comida
from placar import Placar
import time

tela = Screen() # inicialização da tela do jogo
tela.setup(width= 600, height= 600)
tela.bgcolor("black")
tela.title("Snake Game")
tela.tracer(0)

cobra = Cobra() # inicialização da Cobra
comida = Comida() # inicialização da Comida
placar = Placar() # inicialização do Placar

tela.listen()

# comandos da cobra
tela.onkey(fun= cobra.cima, key= "Up")
tela.onkey(fun= cobra.baixo, key= "Down")
tela.onkey(fun= cobra.esquerda, key= "Left")
tela.onkey(fun= cobra.direita, key= "Right")


jogo_rolando = True

# fazendo o jogo rolar
while jogo_rolando:
    tela.update()
    
    cobra.mover()

    if cobra.cabeca_cobra.distance(comida) < 15:
        comida.respawn()
        placar.pontos += 1
        placar.placar_pontos()
        cobra.aumenta_cobra()

    if cobra.cabeca_cobra.xcor() > 295 or cobra.cabeca_cobra.xcor() < -300 or cobra.cabeca_cobra.ycor() > 290 or cobra.cabeca_cobra.ycor() < -290: 
        cobra.reset()
        placar.reset()
    
    for parte in cobra.cobra[1:]:        
        if cobra.cabeca_cobra.distance(parte) < 10:            
            cobra.reset()
            placar.reset()

    time.sleep(0.1)

tela.exitonclick()