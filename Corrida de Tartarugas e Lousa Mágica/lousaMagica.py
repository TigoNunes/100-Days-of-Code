from turtle import Turtle,Screen

caneta = Turtle()
tela = Screen()

def mover_frente():
    caneta.forward(30)

def mover_tras():
    caneta.forward(-30)

def mover_antihorario():
    caneta.left(10)

def mover_horario():
    caneta.right(10)

def reset():
    caneta.reset()

tela.listen()
tela.onkey(fun =mover_frente, key = "w")
tela.onkey(mover_tras, "s")
tela.onkey(mover_antihorario, "a")
tela.onkey(mover_horario, "d")
tela.onkey(reset, "c")

tela.exitonclick()

    