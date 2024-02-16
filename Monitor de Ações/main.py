# API key newsapi: b9825c6f69be40938e6d6188e4fe483e
# API Key alphavantage: TTRXTALDZA2H61K6

import requests
from twilio.rest import Client
import datetime as dt


API_KEYS = {
    "newsapi": "b9825c6f69be40938e6d6188e4fe483e",
    "alphavantage": "TTRXTALDZA2H61K6",
}

DATA_DE_HOJE = dt.datetime.today().date()
EMPRESA = "IBM"

def verifica_mercado():
    data = str(DATA_DE_HOJE).split("-") # cria uma lista com ano, mês e dia
    dias_ano = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    requisicoes_alphavantage = requests.get(url= f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={EMPRESA}&interval=30min&apikey={API_KEYS["alphavantage"]}')
    dados = requisicoes_alphavantage.json()
    mes = int(data[1]) - 1
    data[2] = int(data[2])-1 # Data estabelecida para 1 dia atrás

    veri = False
    while veri != True:
        try:
            ultimo_fechamento = dados["Time Series (30min)"][f"{data[0]}-{data[1]}-{data[2]} 19:30:00"]
        except:
            print("dados não existem")
            if int(data[2]) - 1 != 0:
                data[2] = int(data[2]) - 1

            elif int(data[1]) - 1 != 0:
                data[1] = int(data[1]) - 1
                mes -= 1
                data[2] = dias_ano[mes]

            else:
                data[0] = int(data[0]) - 1
                data[1] = 12
                data[2] = dias_ano[11]
        else:
            veri = True
    
    data[2] = int(data[2])-1 # Data estabelecida para 1 dia deposi da última verificação do mercado
    veri = False

    while veri != True:
        try:
            penultimo_fechamento = dados["Time Series (30min)"][f"{data[0]}-{data[1]}-{data[2]} 19:30:00"]
        except:
            print("dados não existem")
            if int(data[2]) - 1 != 0:
                data[2] = int(data[2]) - 1

            elif int(data[1]) - 1 != 0:
                data[1] = int(data[1]) - 1
                mes -= 1
                data[2] = dias_ano[mes]

            else:
                data[0] = int(data[0]) - 1
                data[1] = 12
                data[2] = dias_ano[11]
        else:
            veri = True

    return [float(penultimo_fechamento["4. close"]), float(ultimo_fechamento["4. close"])]

def busca_noticia():
    requisicoes_newsapi = requests.get(url= f"https://newsapi.org/v2/everything?q={EMPRESA}&from={DATA_DE_HOJE.year}-{DATA_DE_HOJE.month}-{DATA_DE_HOJE.day}&to={DATA_DE_HOJE.year}-{DATA_DE_HOJE.month}-{DATA_DE_HOJE.day}&sortBy=relevancy&language=en&apiKey={API_KEYS['newsapi']}")
    requisicoes_newsapi.raise_for_status()
    noticias = requisicoes_newsapi.json()
    noticia =  noticias["articles"][0]
    # print(noticias)  
    return noticia
    


# TODO: Mercado de ações 
mercado_acoes = verifica_mercado()
rendimento = round(mercado_acoes[1] - mercado_acoes[0], 3)
percentural = round((((mercado_acoes[0]*100)/mercado_acoes[1]) - 100)*-1, 1)

# TODO: Notícias

noticia = busca_noticia()
busca_noticia()

# TODO Enviar SMS
texto_noticia = f"Fonte: {noticia['source']['name']}\nAuthor: {noticia['author']}\n Título: {noticia['title']}\n Descrição: {noticia['description']}\n Conteúdo: {noticia['content']}\n Url: {noticia['url']}\n\n Rendimento IBM = {rendimento}\n Percentual = {percentural}"
account_sid = "AC2fc1a3198702a13e0e104bb875182ba0"
auth_token = "2ab0760e826e1fab9619cbca1ad4e82c"

client = Client(account_sid, auth_token)

mensagem = client.messages.create(
    body=texto_noticia,
    from_='+18156058589',
    to='+5531992889301'
)

print(mensagem.status)
