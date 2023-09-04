import requests
import datetime as dt
import smtplib
import time

MINHA_LAT = -19.912998
MINHA_LONG = -43.94093

PARAMETROS = {
    "lat": MINHA_LAT,
    "lng": MINHA_LONG,
    "formatted": 0,
}

MEU_EMAIL = "alunodpython@gmail.com"
MINHA_SENHA = "vzxkjilvucuocorb"

# --------------- ISS ---------------

def localizacao_iss():
    requisicao_iss = requests.get(url= "http://api.open-notify.org/iss-now.json")
    requisicao_iss.raise_for_status()

    dados_iss = requisicao_iss.json()
    latitude_iss = float(dados_iss["iss_position"]["latitude"])
    longitude_iss = float(dados_iss["iss_position"]["longitude"])
    localizacao_iss = (latitude_iss, longitude_iss)

    if (MINHA_LAT, MINHA_LONG) == localizacao_iss or (MINHA_LAT + 5, MINHA_LONG + 5) == localizacao_iss or (MINHA_LAT - 5, MINHA_LONG - 5) == localizacao_iss:
        return True

# --------------- Sunset ---------------

def escureceu():
    requisicao_sunset = requests.get(url="https://api.sunrise-sunset.org/json", params= PARAMETROS)
    requisicao_sunset.raise_for_status()

    dados_sunset = requisicao_sunset.json()
    sunrise = int(dados_sunset["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(dados_sunset["results"]["sunset"].split("T")[1].split(":")[0])

    dados_dia = dt.datetime.now()
    horas = int(str(dados_dia.time()).split(":")[0])

    if horas >= sunset and horas > sunrise:
        return True

# --------------- Mandar email ---------------

if localizacao_iss() and escureceu():
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls() #torna a conexção segura
            connection.login(user= MEU_EMAIL, password= MINHA_SENHA)
            connection.sendmail(
                from_addr= MEU_EMAIL, 
                to_addrs= MEU_EMAIL, 
                msg= f"Subject:Olhe para cima\n\nA ISS esta acima de voce, olhe para cima"
            )
else:
    print("Não funcionou")

#TODO: faz o programa rodar a cada 60 segundos

# while True:
#     time.sleep(60)
#     if localizacao_iss() and escureceu():
#         with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
#             connection.starttls() #torna a conexção segura
#             connection.login(user= MEU_EMAIL, password= MINHA_SENHA)
#             connection.sendmail(
#                 from_addr= MEU_EMAIL, 
#                 to_addrs= MEU_EMAIL, 
#                 msg= f"Subject:Olhe para cima\n\nA ISS esta acima de voce, olhe para cima"
#             )
#     else:
#         print("Não funcionou")