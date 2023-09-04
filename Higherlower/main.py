from game_data import data 
from banner import vs, titulo
import random
from os import system, name
SCORE = 0

def clear():
    """Limpa a tela do usuário"""
    if name == 'nt':
        _ = system('cls')

def game(comp1, comp2):
    """Exibe as opções pro jogador. 
    
    Recebe a resposta do jogador e compara para saber se ele acertou e pontuou ou se errou e perdeu no jogo"""
    global SCORE 
    print(f"Compare A: {comp1['name']}, {comp1['description']}, {comp1['country']}")
    print(vs)
    print(f"Compare B: {comp2['name']}, {comp2['description']}, {comp2['country']}")

    res = input("Qual deles tem mais seguidores?: ").lower()

    while res != 'a' and res != 'b':
        res = input("Opção inexistente, escolha entre A e B: ")

    if res == 'a' and comp1["follower_count"] > comp2["follower_count"]:        
        SCORE += 1
        return True
    elif res == 'b' and comp2["follower_count"] > comp1["follower_count"]:
        SCORE += 1
        return True
    else: return False
    
def main():
    """Define as opções do jogador, inicia e termina o jogo"""
    comp1 = ""
    comp2 = ""
    continuar = True
    while continuar != False:
        print(titulo)
        if comp1 == "": 
            comp1 = random.choice(data)
            while True:
                comp2 = random.choice(data)
                if comp2 != comp1: break
        else:
            comp1 = comp2
            while True:
                comp2 = random.choice(data)
                if comp2 != comp1: break
        
        continuar = game(comp1, comp2)
        clear()
    print(f"{titulo}Fim de jogo\nSua pontuação foi de: {SCORE}")
        
while True:
    main()
    SCORE = 0
    if input("Deseja jogar novamente? Digite [y] para sim: ") != 'y':
        break