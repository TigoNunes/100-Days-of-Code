import random
from os import system, name
from time import sleep
from logo import logo

N_ADIVINHAR = random.randint(1, 100) # Variável global do programa

def clear():
    """Limpa a tela do usuário"""
    if name == 'nt':
        _ = system('cls')

def choose_dificulty():
    """Define o número de chances do jogador baseado na dificuldade escolhida"""
    dificuldade = input("Qual dificuldade você deseja jogar?\n[f]-> Fácil\n[m]-> Médio\n[d]-> Difícil\n>> ")
    while True:
        if dificuldade.lower() == "f": return 10
        elif dificuldade.lower() == "m": return 7
        elif dificuldade.lower() == "d": return 5
        else: dificuldade = input("\nOpção inválida, por favor escolha uma opção válida:\n[f]-> fácil\n[m]-> médio\n[d]-> Difícil\n>> ")

def guess_number():
    """
    Onde o jogo é realmente jogado.
    
    O jogador da as suas respostas e elas são comparadas com o número que ele deve adivinhar. Onde é decidido se o jogador vence ou perde
    """
    print(logo)    
    chances = choose_dificulty()  
    
    print(f"Estou pensando em um número entre 1 e 100")
    resposta_jogador = ""
    while chances > 0:
        print(f"\nVocte tem {chances} para acertar")
        resposta_jogador = input("chute um número: ")
        if int(resposta_jogador) > N_ADIVINHAR:
            print("Muito alto")
            chances -= 1
        elif int(resposta_jogador) < N_ADIVINHAR:
            print("Muito baixo")
            chances -=1
        else:
            print(f"\nParabéns, você acertou.\nChances restantes: {chances}")
            sleep(2)
            clear()
            break

guess_number()