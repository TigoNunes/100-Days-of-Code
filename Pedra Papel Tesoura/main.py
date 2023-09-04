import random
jogadas = ["pedra", "papel", "tesoura"]
jogadaJogador = int(input("Faça a sua jogada:\n [0] Pedra\n [1] Papel\n [2] Tesoura\n>> "))
jogadaMaquina = random.choice(jogadas)

if jogadaJogador == 0:
    jogadaJogador = jogadas[0]
elif jogadaJogador == 1:
    jogadaJogador = jogadas[1]
elif jogadaJogador == 2:
    jogadaJogador = jogadas[2]

if jogadaJogador == jogadas[0] and jogadaMaquina == jogadas[2]:
    print(f"Você jogou {jogadaJogador} e a maquina jogou {jogadaMaquina}\nVocê venceu!!!")
elif jogadaJogador == jogadas[1] and jogadaMaquina == jogadas[0]:
    print(f"Você jogou {jogadaJogador} e a maquina jogou {jogadaMaquina}\nVocê venceu!!!")
elif jogadaJogador == jogadas[2] and jogadaMaquina == jogadas[1]:
    print(f"Você jogou {jogadaJogador} e a maquina jogou{ jogadaMaquina}\nVocê venceu!!!")

elif jogadaMaquina == jogadas[0] and jogadaJogador == jogadas[2]:
    print(f"Você jogou {jogadaJogador} e a maquina jogou {jogadaMaquina}\nVocê perdeu")
elif jogadaMaquina == jogadas[1] and jogadaJogador == jogadas[0]:
    print(f"Você jogou {jogadaJogador} e a maquina jogou {jogadaMaquina}\nVocê perdeu")
elif jogadaMaquina == jogadas[2] and jogadaJogador == jogadas[1]:
    print(f"Você jogou {jogadaJogador} e a maquina jogou {jogadaMaquina}\nVocê perdeu")