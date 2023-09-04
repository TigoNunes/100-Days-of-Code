import pandas
import random 
import datetime as dt
import smtplib

DATAS = pandas.read_csv("Dia 32/Projeto/Datas/Datas de aniversário.csv")
MEU_EMAIL = "alunodpython@gmail.com"
MINHA_SENHA = "vzxkjilvucuocorb"

def escolher_mensagem(aniversariante, index):
    n = random.randint(1,3)
    with open(f"Dia 32/Projeto/Mensagens/feliz_aniversario_{n}.txt") as arquivo:
        texto = arquivo.read()
    texto = texto.replace("[Name]", aniversariante.name[index])
    return texto

mes_aniversario = [mes for mes in DATAS.month] #Lista com todos os meses em que ocorrem aniversários
dia_de_hoje = dt.datetime.now() #Data de hoje

if dia_de_hoje.month in mes_aniversario:
    aniversariante = DATAS[DATAS.month == dia_de_hoje.month]
    endereco = [index for (index, _) in aniversariante.iterrows()]
    endereco = endereco[0]
    if aniversariante.day[endereco] == dia_de_hoje.day:
        mensagem = escolher_mensagem(aniversariante, endereco)
        
        try:
            with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
                connection.starttls() #torna a conexção segura
                connection.login(user= MEU_EMAIL, password= MINHA_SENHA)
                connection.sendmail(
                    from_addr= MEU_EMAIL, 
                    to_addrs= aniversariante.email[endereco], 
                    msg= f"Subject:Feliz Aniversario\n\n{mensagem}"
                )
        except:
            print("Arquivo não enviado")
    else:
        print("Hoje não é aniversário de ninguem")        
else:
    print("Ninguem faz aniversário hj")
