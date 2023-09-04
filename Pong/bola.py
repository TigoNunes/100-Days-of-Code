from turtle import Turtle
import random

class Bola(Turtle):
    """Gerencia a bola"""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed(0)
        self.penup()
        self.setx(0)
        self.sety(0)
        self.direcao_x = 10
        self.direcao_y = 10
        self.velocidade = 0.1
        
    
    def mover(self):
        """Move a bola pelo jogo"""
        novo_x = self.xcor() + self.direcao_x
        novo_y = self.ycor() + self.direcao_y
        self.goto(x= novo_x, y= novo_y)
    
    def quicar(self):
        """Muda a direção do eixo y da bola ao bater em uma parede"""
        self.direcao_y *= -1
    
    def mudar_direcao(self):
        """Muda a direção do eixo y da bola ao bater em um jogador"""
        self.direcao_x *=-1
        self.velocidade *= 0.9
        if random.randint(0,1) == 0:
            self.direcao_y *= -1

    def resetar(self):
        """Volta a bola para posição original"""
        self.goto(x= 0, y= 0)
        self.velocidade = 0.1
            
    

