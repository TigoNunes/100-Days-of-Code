import random

#functions
def forca(cha):
    Forca =['''
    +----+
       | |
       O |
      /|\|
      / \|   
    
    ''',
    '''
    +----+
       | |
       O |
      /|\|
      /  |   
    
    ''','''
    +----+
       | |
       O |
      /|\|
         |   
    
    ''', '''
    +----+
       | |
       O |
      /| |
         |   
    
    ''', '''
    +----+
       | |
       O |
       | |
         |   
    
    ''', '''
    +----+
       | |
       O |
         |
         |   
    
    ''','''
    +----+
         |
         |
         |
         |   
    
    ''']
    return Forca[cha]
#code
chances = 6
palavra = ["DEPUTADO", "APERITIVO", "CARRO", "COMPETITIVO", "ARROZ", "BRASIL"]
palavra_escolhida = random.choice(palavra)
resposta = []; resposta.extend(palavra_escolhida.upper())
blank=[]
for letras in resposta:
    blank.append('_')


while chances > 0 and blank.count("_") > 0:
    print(forca(chances))
    print(f"\n{blank}\n Chances: {chances}")
    letra = input("Chute uma letra: ")
    if letra.upper() in resposta:
       cont = -1
       for letras in resposta:
        cont += 1
        if letras == letra.upper():
            blank[cont] = letras
            
    else:
        print(f"Errou, letra({letra.upper()}) não pertence a resposta")
        chances-=1

if chances >0:
    print(f"\n{forca(chances)}")
    print(f"\nPalavra: {blank}\nParabéns pela vitória, você ainda tinha: {chances} chances")
else:
    print(f"\n{forca(chances)}")
    print(f"\nInfelizmente você não conseguiu\nPalavra: {resposta}\t Acertos: {blank}")

