
def Criptografar(frase, cod, alfabeto,  alfabeto_maiusculo):
    frase_codficada = [] 
    frase_codficada.extend(frase)
    
    for i in range (len(frase_codficada)):
        for w in alfabeto:
            if w == frase_codficada[i]:
                frase_codficada[i] = alfabeto[alfabeto.index(w) + int(cod)]
                break
    
    for i in range (len(frase_codficada)):
        for w in alfabeto_maiusculo:
            if w == frase_codficada[i]:
                frase_codficada[i] = alfabeto_maiusculo[alfabeto_maiusculo.index(w) + int(cod)]
                break
    
    mensagem = ""
    for letra in frase_codficada:
        mensagem = mensagem + letra
    return mensagem
    
def  Descriptografar(frase, cod, alfabeto,  alfabeto_maiusculo):
    frase_codficada = [] 
    frase_codficada.extend(frase)
    
    for i in range (len(frase_codficada)):
        for w in alfabeto:
            if w == frase_codficada[i]:
                frase_codficada[i] = alfabeto[alfabeto.index(w) - int(cod)]
                break
    
    for i in range (len(frase_codficada)):
        for w in alfabeto_maiusculo:
            if w == frase_codficada[i]:
                frase_codficada[i] = alfabeto_maiusculo[alfabeto_maiusculo.index(w) - int(cod)]
                break
    
    mensagem = ""
    for letra in frase_codficada:
        mensagem = mensagem + letra
    return mensagem
    
def main():
    alfabeto =['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q', 
           'r','s','t','u','v','w','x','y','z','a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q', 
           'r','s','t','u','v','w','x','y','z']
    alfabeto_maiusculo = []
    for letra in alfabeto: alfabeto_maiusculo.append(letra.upper())

    res = input("Deseja encriptografar ou descriptografar uma mensagem?\n[a]encriptografar\t[b]descriptografar\n\n-> ")
    if res.lower() == "a":
        frase = input("Escreva a frase que deseja encriptografar: ")
        valor = input("Digite o valor de codficação: ")
        valido = False
        while valido == False:
            if int(valor) > 25:
                valor = input("Digite um valor menor ou igual a 25: ")
            else:
                valido = True

        criptografia = Criptografar(frase, valor, alfabeto, alfabeto_maiusculo)

        print(f"Mensagem criptografada:\n{criptografia}")

        res = input("Deseja descriptografar a mensagem?\n[a]Sim\t[b]Não\n\n-> ")
        if res.lower() == "a":
            descriptografia = Descriptografar(criptografia, valor, alfabeto, alfabeto_maiusculo)

            print(f"Mensagem descriptografada:\n{descriptografia}")
        else:
            print("programa encerrado\n")
    elif res.lower() == "b":
        frase = input("Escreva a frase que deseja descriptografar: ")
        valor = input("Digite o valor de decodficação: ")
        valido = False
        while valido == False:
            if int(valor) > 25:
                valor = input("Digite um valor menor ou igual a 25: ")
            else:
                valido = True

        descriptografia = Descriptografar(frase, valor, alfabeto, alfabeto_maiusculo)

        print(f"Mensagem descriptografada:\n{descriptografia}")
    else:
        print("programa encerrado\n")

end_program = False
while end_program == False:
    main()
    resp_user = input("\nDeseja encerrar o programa?\n[S]SIM\t[N]NÃO\n-> ")
    if resp_user.upper() == 'S':
        end_program = True
        print("programa encerrado")


