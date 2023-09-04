from turtle import Turtle

class Placar(Turtle):
    """Escreve o placar e a mensagem de fim de jogo"""
    def __init__(self):
        super().__init__()
        self.pontos = 0
        with open("Snake_Game/dados.txt") as dados:
            self.maior_pontuacao = int(dados.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.placar_pontos()
    
    def placar_pontos(self):
        """Escreve o placar, com os pontos já atualizados"""
        with open("Snake_Game/dados.txt") as dados:
            self.maior_pontuacao = int(dados.read())
        self.clear()
        self.write(arg= f"Placar de pontos: {self.pontos} Maior pontuação: {self.maior_pontuacao}", move= False, align= "center", font=('Arial', 13, 'normal'))

    def reset(self):
        """Zera a pontuação atual e atualiza a pontuação mais alta"""
        if self.pontos > self.maior_pontuacao:
            with open("Snake_Game\dados.txt", mode="w") as dados:
                dados.write(str(self.pontos))
        self.pontos = 0
        self.placar_pontos()

    def fim_de_jogo(self):
        """Escreve a mensagem de fim de jogo"""
        self.goto(0.0, 0.0)
        self.write(arg= f"Fim de Jogo", move= False, align= "center", font=('Arial', 13, 'normal'))