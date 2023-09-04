from turtle import Turtle

class Placar(Turtle):
    """Escreve o placar e a mensagem de fim de jogo"""
    def __init__(self, xcor):
        super().__init__()
        self.pontos = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x= xcor, y=265)
        self.placar_pontos()
    
    def placar_pontos(self):
        """Escreve o placar, com os pontos já atualizados"""
        self.clear()
        self.write(arg= f"{self.pontos}", move= False, align= "center", font=('Oswald', 20, 'normal'))

    