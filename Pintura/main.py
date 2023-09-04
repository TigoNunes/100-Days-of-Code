from turtle import Turtle, Screen
import random

tortuguita = Turtle()
tortuguita.shape("turtle")
tortuguita.speed(10)
tela = Screen()
tela.colormode(255)

cores_rgb = [(198, 159, 116), (70, 92, 129), (147, 85, 53),(218, 210, 116), (138, 160, 191), (178, 160, 38), (184, 146, 164), (28, 32, 46), (58, 34, 23), (120, 70, 93), (139, 175, 154)]
tortuguita.penup()
tortuguita.hideturtle()
print(tortuguita.pos())
tortuguita.setheading(225)

for i in range(5):
    tortuguita.forward(70)

tortuguita.setheading(0)
posicao_x = tortuguita.xcor()

for i in range(10):
    for y in range(10):
        tortuguita.dot(20, random.choice(cores_rgb))
        tortuguita.forward(50)
    tortuguita.setx(posicao_x)
    tortuguita.sety(tortuguita.ycor() + 50)



tela.exitonclick()