from Cofee_Machine import MENU, resources

MOEDAS = {
    "25 centavos": 0.25,
    "10 centavos": 0.10,
    "5 centavos": 0.05,
    "1 centavo": 0.01,
}

DINHEIRO = 5.00

CONT = True


def verifica(agua, cafe, leite):
    """Verifica se os ingredientespara o pedido estão disponíveis."""

    if resources["water"] >= agua and resources["coffee"] >= cafe and resources["milk"] >= leite: return True
    elif resources["water"] < agua:
        print("Agua insuficiente para este pedido\n")
        return False
    elif resources["coffee"] < cafe:
        print("Café insuficiente para este pedido\n")
        return False
    else:
        print("Leite insuficiente para este pedido\n")
        return False


def pagamento(pedido):
    """Verifica se o usuário tem dinheiro suficiente para realizar o pedido, caso tenha ele realiza a compra."""

    val_pagar = 0
    global DINHEIRO
    custo = 0

    match pedido.lower():
        case 'a':
            custo = MENU["espresso"]["cost"]
        case 'b': 
            custo = MENU["latte"]["cost"]
        case 'c':
            custo = MENU["cappuccino"]["cost"]
    
    if DINHEIRO < custo:
        print(f"Você tem {DINHEIRO}R$, seu pedido custa {custo}R$. Dinheiro insuficiente")
        return False
    else:
        for moeda in MOEDAS:
            val_pagar += int(input(f"Quantas moedas de {moeda} você deseja utilizar?: ")) * MOEDAS[moeda]
        
        DINHEIRO -= val_pagar
        DINHEIRO += val_pagar - custo
        return True

    
def preparar_cafe(pedido):
    """Subtrai os ingradientes do estoque e "prepara" o café."""

    match pedido.lower():
        case 'a':
            resources['water']= resources['water'] - MENU["espresso"]["ingredients"]["water"] 
            resources['coffee']= resources['coffee'] - MENU["espresso"]["ingredients"]["coffee"]
            
            print("Aqui está seu espresso")
        case 'b': 
            resources['water']= resources['water'] - MENU["latte"]["ingredients"]["water"],
            resources['coffee']= resources['coffee'] -  MENU["latte"]["ingredients"]["coffee"], 
            resources['milk'] = resources['milk'] - MENU["latte"]["ingredients"]["milk"]
            
            print("Aqui está seu latte")
        case 'c':
            resources['water'] = resources['water'] - MENU["cappuccino"]["ingredients"]["water"], 
            resources['coffee']= resources['coffee'] - MENU["cappuccino"]["ingredients"]["coffee"], 
            resources['milk'] = resources['milk'] - MENU["cappuccino"]["ingredients"]["milk"]
            
            print("Aqui está seu cappuccino")


def main():  
    global CONT  
    cont_pedido = False # variável para saber se o pedido vai ou não continuar    
    pedido = input("Qual sabor de café você gostaria de beber?\n[A] Espresso\t[B] Latte\t[C] Cappucino\n>> ")

    match pedido.lower():
        case 'a':
            cont_pedido = verifica(MENU["espresso"]["ingredients"]["water"], MENU["espresso"]["ingredients"]["coffee"], 0)
        case 'b': 
            cont_pedido = verifica(MENU["latte"]["ingredients"]["water"], MENU["latte"]["ingredients"]["coffee"], MENU["latte"]["ingredients"]["milk"])
        case 'c':
            cont_pedido = verifica(MENU["cappuccino"]["ingredients"]["water"], MENU["cappuccino"]["ingredients"]["coffee"], MENU["cappuccino"]["ingredients"]["milk"])
        case 'report':
            for res in resources:
                print(f"{res}: {resources[res]}")
            
            print(f"Dinheiro: R${DINHEIRO}")
        case 'off':
            CONT = False
            return
    
    if cont_pedido == True:
        cont_pedido = pagamento(pedido)
    
    if cont_pedido == True:
        preparar_cafe(pedido)

while CONT != False and DINHEIRO >= 1.5:
    main()
if DINHEIRO < 1.5: print("Seu dinheiro é insuficiente\n")
