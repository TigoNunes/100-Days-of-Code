from turtle import Turtle
import random

CORES = ("Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet")
POSICOES_X = (305, 355, 405, 455, 505, 555, 605, 655, 705, 755)
class Carro:
    """Gerencia os carros"""
    def __init__(self, pos_carro):
        self.carro = []
        self.constroi_carro(pos_carro)
    
    def constroi_carro(self, pos_carro):
        """Constroi o carro"""
        cor_carro = random.choice(CORES)
        posicao_y = random.randint(-240, 240)
        for i in range(2):
            parte = Turtle(shape= "square")
            parte.penup()
            parte.color(cor_carro)
            parte.goto(x= POSICOES_X[pos_carro] + 20*i, y= posicao_y)
            parte.setheading(180)
            self.carro.append(parte)
    
    def mover(self):
        """Faz os carros atravessarem a rua"""
        for parte in range(len(self.carro) - 1, 0, -1):
            novo_x = self.carro[parte - 1].xcor()
            novo_y = self.carro[parte - 1].ycor()
            self.carro[parte].goto(novo_x, novo_y)

        self.carro[0].forward(20)

    def retorna_carro(self, pos_carro):
        """Reposiciona o carro depois que ele cruza a rua"""
        self.carro[0].goto(x= POSICOES_X[pos_carro],y= self.carro[0].ycor())

    def novo_nivel(self, pos_carro):
        """Gera novas posições para os carros"""
        posicao_y = random.randint(-240, 240)
        self.carro[0].goto(x= POSICOES_X[pos_carro],y= posicao_y)
            