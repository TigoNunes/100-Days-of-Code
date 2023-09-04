with open(file= "F:/100 days python bootcamp/Projetos em Python/Cartas Automáticas/Modelo/carta.txt") as carta_modelo:
    modelo = carta_modelo.read()

with open(file= "F:/100 days python bootcamp/Projetos em Python/Cartas Automáticas/Pessoas/nomes.txt") as pessoas_nomes:
    nomes = pessoas_nomes.read()

lista_nomes = nomes.split()
for nomes in lista_nomes:
    nova_carta = f"F:/100 days python bootcamp/Projetos em Python/Cartas Automáticas/Mensagens Prontas/mensagem_para_{nomes}"
    nova_mensagem = modelo.replace("[nome]", nomes)

    with open(file= nova_carta, mode= "w") as pronto_para_envio:
        pronto_para_envio.write(nova_mensagem)
