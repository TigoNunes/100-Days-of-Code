def BandName():
    repetir = True
    print("Bem vindo ao gerador de nome de bandas")
    while repetir == True:
        cidade = input('Qual o nome da sua cidade?\n> ')
        pet = input('Qual o nome do seu animal de estimação?\n> ')
        bandaRock = cidade + ' ' + pet
        print(bandaRock)
        op = 'A'
        while op != 'S' and op != 'N':
            op = input('Repetir? [S/N]\n> ')
        if op == 'N': 
            repetir = False
        elif op != 'S' and op != 'N': 
            print('Opção invalida\n')

BandName()


