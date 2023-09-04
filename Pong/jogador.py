from turtle import Turtle

class Jogador:
    def __init__(self,p_controle):
        self.jogador = []
        self.constroi_jogador(p_controle)
        self.jogador[0].setheading(90)
        self.jogador[-1].setheading(270)

    def constroi_jogador(self, p_controle):
        """Instancia as pastes do corpo do jogador"""
        for i in range(4):
            fragmento = Turtle(shape= "square")
            fragmento.color("white")
            fragmento.penup()
            if p_controle == 1: fragmento.goto(-370,fragmento.ycor() - 20*i)
            else: fragmento.goto(370,fragmento.ycor() - 20*i) 

            self.jogador.append(fragmento)     
   
    # funções de movimento 
    def cima(self):
        """Move o jogador para cima"""
        if self.jogador[0].ycor() < 280:
            for parte in range(len(self.jogador) - 1, 0, -1):
                novo_y = self.jogador[parte - 1].ycor()
                self.jogador[parte].goto(self.jogador[parte].xcor(), novo_y)

            self.jogador[0].forward(20)
    
    def baixo(self):
        """Move o jogador para baixo"""
        if self.jogador[-1].ycor() > -280:
            for parte in range(len(self.jogador) - 1):
                novo_y = self.jogador[parte + 1].ycor()
                self.jogador[parte].goto(self.jogador[parte].xcor(), novo_y)
                    
            self.jogador[-1].forward(20)
        
