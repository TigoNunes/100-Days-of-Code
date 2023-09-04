from turtle import Turtle

POSICAO_COMECO = (0.0, -280)

class Tartaruga(Turtle):
    """Classe da tartaruga que será controlada pelo jogador"""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.posciao_inicial()
        self.setheading(90)
    
    def posciao_inicial(self):
        """Posiciona a tartaruga na posição de início"""
        self.goto(POSICAO_COMECO)
    
    def mover_tartaruga(self):
        """Move a tartaruga para frente"""
        self.forward(20)