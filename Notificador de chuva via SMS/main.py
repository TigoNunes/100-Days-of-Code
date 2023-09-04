import requests
from twilio.rest import Client

# Autentificações para sms
account_sid = "AC2fc1a3198702a13e0e104bb875182ba0"
auth_token = "2ab0760e826e1fab9619cbca1ad4e82c"

# Autentificações para status do clima
API_KEY = "7dd0bddc5dc816205b464703f9a689c6"
MINHA_LATITUDE = -19.949250
MINHA_LONGITUDE = -43.929296

PARAMETROS = {
    "lat": MINHA_LATITUDE,
    "lon": MINHA_LONGITUDE,
    "appid": API_KEY,
}

requisicao = requests.get(url = f"https://api.openweathermap.org/data/2.5/forecast?lat=44.34&lon=10.99&appid=7dd0bddc5dc816205b464703f9a689c6") # pega a previsão do tempo dos próximos 5 dias com dados com distância de 3h
requisicao.raise_for_status()

dados = requisicao.json()

previsao = dados["list"][:5]

levar_guarda_chuva = False

for clima in previsao: #Verifica se terá chuva nas próximas 12h
    if clima["weather"][0]["id"] < 700:
        levar_guarda_chuva = True

if levar_guarda_chuva:
    client = Client(account_sid, auth_token)

    # Envia a mensagem SMS
    mensagem = client.messages.create(
        body="Vai Chover, leve um guarda chuva",
        from_='+18156058589',
        to='+5531992889301'
    )

    print(mensagem.status)
