print('Bem vindo a calculadora de conta!')
class Conta:
    precoTotal = float(input("Valor da conta: "))
    gorjeta = int(input('Qual a porcentagem de gorjeta?: '))
    numPessoas = int(input('Quantas pessoas vão pagar?: '))
class Main:    
    conta = Conta()
    resultado = (conta.precoTotal * (conta.gorjeta/100) + conta.precoTotal)/conta.numPessoas
    print (f'Cada pessoa vai pagar: R${round(resultado, 2)}')
