import smtplib
import datetime as dt
from random import choice

MEU_EMAIL = "alunodpython@gmail.com"
SENHA = "vzxkjilvucuocorb"

enviar_mensagem_motivacional = dt.datetime.now()
if enviar_mensagem_motivacional.weekday() == 3:
    with open("Dia 32/Aprendendo a Mandar emails/quotes.txt") as quotes:
        mensagens = quotes.read()
    mensagens_lista = mensagens.splitlines()
    mensagem = choice(mensagens_lista)

    try:
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls() #torna a conexção segura
            connection.login(user= MEU_EMAIL, password= SENHA)
            connection.sendmail(
                from_addr= MEU_EMAIL, 
                to_addrs= "tiagonunesdecerqueira@gmail.com", 
                msg= f"Subject:mensagem motivacional\n\n{mensagem}"
            )
    except:
        print("não foi possivel enviar o email")
else:
    print("Hoje não é quinta")