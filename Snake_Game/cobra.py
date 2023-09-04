from turtle import Turtle

class Cobra:
    """Gerencia a cobra"""
    def __init__(self):
        self.cobra = []
        self.constroi_cobra()
        self.cabeca_cobra = self.cobra[0]
        self.cabeca_cobra.color("lime green")
    
    def constroi_cobra(self):
        for i in range(3):
            nova_parte = Turtle(shape= "square")
            nova_parte.color("white")
            nova_parte.penup()
            nova_parte.setx(nova_parte.xcor() - 20*i)
            self.cobra.append(nova_parte)
    
    def aumenta_cobra(self):
        nova_parte = Turtle(shape= "square")
        nova_parte.color("white")
        nova_parte.penup()
        nova_parte.goto(self.cobra[-1].xcor(), self.cobra[-1].ycor())
        self.cobra.append(nova_parte)
    
    def mover(self):
        for parte in range(len(self.cobra) - 1, 0, -1):
            novo_x = self.cobra[parte - 1].xcor()
            novo_y = self.cobra[parte - 1].ycor()
            self.cobra[parte].goto(novo_x, novo_y)

        self.cabeca_cobra.forward(20)
    
    def reset(self):
        """Reinicia a cobra
        
        Tira a cobra antiga da tela, enquanto isso cria uma nova cobra."""
        for partes in self.cobra:
            partes.goto(x= 1000, y = 1000)
        self.cobra.clear()
        self.constroi_cobra()
        self.cabeca_cobra = self.cobra[0]
        self.cabeca_cobra.color("lime green")
    
    def cima(self):
        if self.cabeca_cobra.heading() != 270:
            self.cabeca_cobra.setheading(90)
    
    def baixo(self):
        if self.cabeca_cobra.heading() != 90:
            self.cabeca_cobra.setheading(270)
    
    def esquerda(self):
        if self.cabeca_cobra.heading() != 0:
            self.cabeca_cobra.setheading(180)

    def direita(self):
        if self.cabeca_cobra.heading() != 180:
            self.cabeca_cobra.setheading(0)