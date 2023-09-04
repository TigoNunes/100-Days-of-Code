from turtle import Turtle

class Divisoria(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.sety(-300)
        self.setx(0)
        self.setheading(90)
        self.pensize(width= 5)
        self.color("white")
        self.pontos_p1 = 0
        self.pontos_p2 = 0
        self.divisoria()

    def divisoria(self):
        """Pinta a divisoria do campo"""
        while self.ycor() < 301:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(30)
    
    
