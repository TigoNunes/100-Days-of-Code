jogador = input("Qual o seu nome?\n")
print(f"O jovem aventureiro {jogador} saiu em uma busca por um tesouro, porém, no meio de sua jornada ele se viu perdido em uma caverna.\nPerante uma encruzilhada uma decisão deveria ser tomada!")
res = input("Esquerda ou Direita?: \n")
if res.lower() == 'esquerda':
    print(f"{jogador} toma o caminho da esquerda, caminhando por pedras cada vez mais humidas ele se depara com um lago subterrâneo.\nMais uma vez uma decisão precisava ser tomada!")
    res = input("Esperar ou Nadar?: \n")
    if res.lower() == 'esperar':
        print(f"{jogador} pacientemente aguarda o desconhecido, para sua surpresa 3 pequenos barcos chegam até ele, cada barquinho contendo uma pintura dierente.\nE mais uma veeez uma decisão precisava ser tomada!")
        res = input("Qual embarcação pegar? Vermelha, Azul ou Amarela?: ")
        if res.lower() == 'amarela':
            print(f"Por mais inesperado que seja e por pura sorte, já que não existem razões lógicas para a escolha de nosso aventureiro, ele conseguiu. {jogador} conquistou o tesouro perdido!!!!")
        else:
            print(f"Fim da jornada de {jogador}\nGAME OVER!!!!!!!")
    else:
        print(f"Fim da jornada de {jogador}\nGAME OVER!!!!!!!")
else:
    print(f"Fim da jornada de {jogador}\nGAME OVER!!!!!!!")

