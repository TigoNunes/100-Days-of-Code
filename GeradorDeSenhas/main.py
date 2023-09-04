import random

letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 
"A", "B", "C", "D", 'E', "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numeros = ["1","2","3","4","5","6","7","8","9","0"]
symbols = ["+","!","#","(",")"]

Nletras = int(input("Quantas letras em sua senha? "))
Nnumeros = int(input("Quantos números em sua senha? "))
Nsymbols = int(input("Quantos simbolos em sua senha? "))

senha = ""
#Jeito Facil

# for i in range(0, Nletras):
#     senha+= random.choice(letras)
# for i in range(0, Nnumeros):
#     senha+= random.choice(numeros)
# for i in range(0, Nsymbols):
#     senha+= random.choice(symbols)
# print(senha)

#Jeito Menos Facil
elementos_senha =[]
for i in range(0, Nletras):
    elementos_senha.append(random.choice(letras))
for i in range(0, Nnumeros):
    elementos_senha.append(random.choice(numeros))
for i in range(0, Nsymbols):
    elementos_senha.append(random.choice(symbols))
print(elementos_senha)
for i in range(len(elementos_senha)):
    pop = random.choice(elementos_senha)
    senha += pop
    elementos_senha.remove(pop)
print(senha)