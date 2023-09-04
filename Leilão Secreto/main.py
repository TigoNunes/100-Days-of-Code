from os import system, name
from math import sqrt
# Lista como variaável global
lances = {}

def clear():
    if name == 'nt':
        _ = system('cls')

def cria_lista():
    mais_pessoas = True

    # Construtor da lista
    while mais_pessoas == True:
        nome = input("Qual o seu nome?: ")
        lance = input("Faça o seu lance: R$ ")
        lances[nome] = int(lance)
        pergunta = input("Mais alguem vai participar do leilão?\nDigite[y] para sim\tdigite[n] para não\n-> ")

        if pergunta.upper() == "N":  
            mais_pessoas = False
        
        clear()

def main():
    cria_lista()

    maior = 0
    vencedor =""

    #  Descobre qual o maior lance
    for keys in lances:
        if lances[keys]**2 > maior: 
            maior = lances[keys]**2
            vencedor = keys

    print(lances)
    print(f"O vencedor do leilão foi {vencedor}, com o lance de {sqrt(maior)}")

# Começa o código 
main()