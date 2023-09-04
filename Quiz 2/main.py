from question_model import Question
from quiz import Quiz
import requests
from ui import InterfaceQuiz


parametros = {
    "amount": 10,
    "type": "boolean",
}

api = requests.get(url= "https://opentdb.com/api.php", params= parametros)
api.raise_for_status()

question_data = api.json()
question_data = question_data["results"]

banco_questoes = [] # Armazena todas as perguntas e suas respectivas respostas

for data in question_data:
    banco_questoes.append(Question(data["question"], data["correct_answer"]))

    
quiz = Quiz(banco_questoes)
interface = InterfaceQuiz(quiz)



