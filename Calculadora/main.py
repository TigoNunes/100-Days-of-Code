def calculadora(num1, num2, op):
    """Função recebe os valores da conta e o operaodr, então devolve o resultado"""
    match op:
        case "+": 
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case"/":
            return num1 / num2
        case _:
            print("invalid operator")

def main():
    while True:        
        num_um = input("Digite o primeiro número: ")

        while True:
            while True:
                operador = input("Eslcolha o operador:\n+ -> somar\n- -> subtrair\n* -> multiplicar\n/ -> dividir\n>> ")
                if operador != "+" and operador != "-" and operador != "*" and operador != "/":
                        print("operador inválido, insira um válido")
                else:
                    break
            print(num_um, operador)
            num_dois = input("Digite o segundo número: ")

            num_um = float(num_um)
            num_dois = float(num_dois)

            resultado = calculadora(num_um, num_dois, operador)
            print(f"\nResultado: {num_um} {operador} {num_dois} = {resultado}")

            if input("\nDigite [y] caso deseje continuar a conta: ").lower() != 'y': break 

            num_um = resultado
            print("\n")
        
        if input("\nCaso deseje sair do programa digite [n]: ").lower() == "n": break 

main()