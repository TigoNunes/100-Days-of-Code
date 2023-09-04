from question_model import Question
from quiz import Quiz
from data import question_data

banco_questoes = [] # Armazena todas as perguntas e suas respectivas respostas

for data in question_data:
    banco_questoes.append(Question(data["question"], data["correct_answer"]))

    
quiz = Quiz(banco_questoes)

while quiz.restam_questoes() != False:
    quiz.proxima_questao()

print(f"Você completou o quiz!\nSua pontuação: {quiz.ponto}/{quiz.num_questao}\n")

