import random
from os import system, name
from logo import logo

def clear():
    """Limpa a tela do usuário"""
    if name == 'nt':
        _ = system('cls')

def dealer(n, mao):
    """Sorteia as cartas e retorna para os participantes"""
    cards = {
        "A": [11,1],
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "R": 10,
    }

    baralho = []
    for card in cards:
        baralho.append(card)
    
    veri = ""
    for i in range(n):
        veri = random.choice(baralho)
        if veri == 'A':
            x = 0
            for val in mao:
                x += val
            if x + 11 > 21:
                mao.append(1)
            else:
                mao.append(11)
        else:
            mao.append(cards[veri])
        
    return mao

def main():
    print(logo)
    player_hand = []
    dealer_hand = []

    dealer(2, player_hand)
    dealer(1, dealer_hand)

    cont_player = player_hand[0] + player_hand[1]
    cont_dealer = 0

    print(f"\nMão do jogador: {player_hand}\nMão do dealer: {dealer_hand}")
    if cont_player < 21:
        if input(f"Você tem {cont_player}, deseja comprar mais cartas? presione [y] para sim e [n] para não\n>> ").lower() == 'y': continuar = True 
        else: continuar = False
    else: continuar = False
    
    # aqui o jogador está adquirindo novas cartas. Se sua mão passar de 21 ele perde, se ela for exatamente 21 ele ganha e se for menos ele pode escolher comprar mais ou não 
    while continuar == True:
        dealer(1, player_hand)
        print(f"Mão do jogador: {player_hand}\nMão do dealer: {dealer_hand}")
        cont_player += player_hand[-1]
        
        if cont_player > 21: 
            return print(f"seu score foi de {cont_player}, você perdeu")
        elif cont_player == 21: 
            return print(f"seu score foi de {cont_player}, parabéns você venceu")
        elif input(f"Você tem {cont_player}, deseja comprar mais cartas? presione [y] para sim e [n] para não\n>> ").lower() != 'y': continuar = False
    
    #  Aqui o dealer compra a sua segunda carta
    dealer(1, dealer_hand)
    print(f"Mão do jogador: {player_hand}\nMão do dealer: {dealer_hand}")

    for val in dealer_hand:
        cont_dealer += val
    
    # Aqui o dealer compra cartas até possuir um score de no mínimo 17
    while cont_dealer < 17:
        dealer(1, dealer_hand)
        cont_dealer += dealer_hand[-1]
        print(f"\nMão do jogador: {player_hand}\nMão do dealer: {dealer_hand}")
    
    if cont_dealer > 21: print(f"\n\tJogador\t  Dealer\nCartas:\t{player_hand}\t {dealer_hand}\nPontos:\t{cont_player}\t    {cont_dealer}\n--------------------------\nVencedor: Jogador\n--------------------------")
    elif cont_player > cont_dealer: print(f"\n\tJogador\t   Dealer\nCartas:\t{player_hand}\t {dealer_hand}\nPontos:\t{cont_player}\t    {cont_dealer}\n--------------------------\nVencedor: Jogador\n--------------------------")
    elif cont_player == cont_dealer: print(f"\n\tJogador\t   Dealer\nCartas:\t{player_hand}\t {dealer_hand}\nPontos:\t{cont_player}\t    {cont_dealer}\n--------------------------\nEmpate\n--------------------------")
    else: print(f"\n\tJogador\t Dealer\nCartas:\t{player_hand}\t  {dealer_hand}\nPontos:\t{cont_player}\t       {cont_dealer}\n--------------------------\nVencedor: Dealer\n--------------------------")
   
while True:
    if input("Deseja jogar Blackjack? Digite [y] caso sim\n>> ").lower() == 'y': 
        clear()
        main()        
    else: 
        print("OK, tenha um bom dia")
        break
