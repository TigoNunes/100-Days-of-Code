from tkinter import *
from quiz import Quiz

COR_THEMA = "#375362"

class InterfaceQuiz:
    def __init__(self, quiz_brain:Quiz):
        self.quiz = quiz_brain

        self.janela = Tk()
        self.janela.title("QUiz")
        self.janela.config(bg= COR_THEMA, padx= 20, pady= 20)

        self.canvas = Canvas(width= 300, height= 250, bg= "White", highlightthickness=0)
        self.canvas.grid(column=0, row= 1, columnspan= 2, pady=50)
        self.pergunta = self.canvas.create_text(150, 125, text= "pergunta",width= 280 ,font=("Arial", 20, "italic"), )

        self.pontos = 0 #pontos
        self.num_questoes = 0
        self.placar = Label(text=f"Pontuação: {self.pontos}", fg= "White", bg= COR_THEMA)
        self.placar.grid(column= 1, row= 0)

        botao_true_img = PhotoImage( file= "Quiz 2/images/true.png")
        self.botao_true = Button(image= botao_true_img, highlightthickness=0, background= COR_THEMA, command= self.resposta_true)
        self.botao_true.grid(column=0, row=2)

        botao_false_img = PhotoImage( file= "Quiz 2/images/false.png")
        self.botao_false = Button(image= botao_false_img, highlightthickness=0, background= COR_THEMA, command= self.resposta_false)
        self.botao_false.grid(column=1, row=2)

        self.proxima_pergunta()
        
        self.janela.mainloop()

    def proxima_pergunta(self):  
        self.canvas.config(bg= "White")
        self.placar.config(text= f"Pontuação: {self.pontos}")     
        pergunta_atual = self.quiz.proxima_questao()
        self.canvas.itemconfig(self.pergunta, text= pergunta_atual)
        if pergunta_atual == "Fim do quiz":
            self.botao_false["state"] = DISABLED
            self.botao_true["state"] = DISABLED
    
    def resposta_true(self):
        self.verifica_resposta(self.quiz.verifica_resposta("True"))

    
    def resposta_false(self):
        self.verifica_resposta(self.quiz.verifica_resposta("False"))

    def verifica_resposta(self,resp):
        if resp: 
            self.canvas.config(bg= "Green")
            self.pontos += 1
        else: 
            self.canvas.config(bg= "Red")
        self.janela.after(100, self.proxima_pergunta)