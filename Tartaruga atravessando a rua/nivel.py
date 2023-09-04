from turtle import Turtle

class Nivel(Turtle):
    """Escreve o nivel e a mensagem de derrota"""
    def __init__(self):
        super().__init__()
        self.nivel = 0
        self.dificuldade =  0.1
        self.hideturtle()
        self.penup()
        self.goto(x=-270,y= 280)
        self.mostrar_nivel()
    
    def mostrar_nivel(self):
        """Escreve o nível em que o jogador está"""
        self.clear()
        self.write(arg= f"Nível: {self.nivel}", move= False, align= "center", font=('Arial', 10, 'normal'))
    
    def fim_de_jogo(self):
        """Escreve a mensagem de fim de jogo"""
        self.goto(0.0, 0.0)
        self.write(arg= f"Fim de Jogo", move= False, align= "center", font=('Arial', 20, 'normal'))

    def dificulde_jogo(self):
        """Aumenta a velocidade dos carros e da tartaruga"""
        self.dificuldade *= 0.9