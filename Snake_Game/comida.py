from turtle import Turtle
import random

class Comida(Turtle):
    """Gerencia a comida no jogo"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.speed(0)
        
        self.respawn()
    
    def respawn(self):
        """espawna as comidas aleatoriamente no cenário"""

        x_aleatorio = random.randint(-280, 280)
        y_aleatorio = random.randint(-280, 280)
        self.goto(x= x_aleatorio, y= y_aleatorio)
        

