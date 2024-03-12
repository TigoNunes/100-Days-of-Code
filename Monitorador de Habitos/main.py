import requests as r
from datetime import datetime
import webbrowser

# Globais ------------------------------------------
NOME_DE_USUARIO = "tiagonunesdecerqueira"
TOKEN = "bdciieGHYBADYSIUFBI"
ID_GRAFICO = "a01"

# Criando usuário------------------------------------------

pixela_http = "https://pixe.la/v1/users"
users_request_body = {
    "token": "bdciieGHYBADYSIUFBI",
    "username": "tiagonunesdecerqueira",
    "agreeTermsOfService": 'yes',
    "notMinor": "yes"
}

# resposta = r.post(url= pixela_http, json= users_request_body)
# print(resposta.text)

# Criando grafico ------------------------------------------

graph_request_body = {
    "id": "a01",
    "name": "Estudos",
    "unit": "commit",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_endpoint = f"{pixela_http}/{NOME_DE_USUARIO}/graphs"

# resposta = r.post(url= graph_endpoint, json= graph_request_body, headers= headers)
# print(resposta.text)

# Postando no Grafico ------------------------------------------
dia = datetime.today()
dia_hoje = dia.strftime('%Y%m%d')

post_endpoint = f"{pixela_http}/{NOME_DE_USUARIO}/graphs/{ID_GRAFICO}"

post_request_body = {
    "date": dia_hoje,
    "quantity": input("De 0 a 9, o quanto eu estudei hoje? > ")
}

resposta = r.post(url= f"{post_endpoint}", json= post_request_body, headers= headers)
print(resposta.text)
if resposta.status_code == 200:
    webbrowser.open(f"https://pixe.la/v1/users/{NOME_DE_USUARIO}/graphs/{ID_GRAFICO}.html")

# Atualizando o Grafico ------------------------------------------

dia_atualizar = datetime(year=2024, month=2, day=15)
dia_atualizar_tratado = dia_atualizar.strftime('%Y%m%d')

update_endpoint = f"{post_endpoint}/{dia_atualizar_tratado}"

update_request_body = {
    "quantity": "6"
}

# resposta = r.put(url= f"{update_endpoint}", json= update_request_body, headers= headers)
# print(resposta.text)

# Deletando pixel do Grafico ------------------------------------------

dia_deletar = datetime(year=2024, month=2, day=1)
dia_deletar_tratado = dia_deletar.strftime('%Y%m%d')

delete_endpoint = f"{post_endpoint}/{dia_deletar_tratado}"

# resposta = r.delete(url= f"{delete_endpoint}", headers= headers)
# print(resposta.text)
