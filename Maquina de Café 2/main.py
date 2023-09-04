from Pagamento import Pagamento
from Maquina_de_cafe import Maquina_de_Cafe

maquina_on = True
pagar = Pagamento()
maquina = Maquina_de_Cafe()

while maquina_on != False:
    cont_pedido = False
    
    pedido = input("Qual sabor de café você gostaria de beber?\n[A] Espresso\t[B] Latte\t[C] Cappucino\n>> ")

    if pedido == "report":
        maquina.retorna_recursos()
        print(f"Carteira: R${pagar.dinheiro}")
    elif pedido == "off":
        maquina_on = False
    else:
        maquina.verifica_ingredientes(pedido)
        cont_pedido = True
    
    
    if cont_pedido == True:
        pagar.verifica_pagamento(pedido)
        cont_pedido = pagar.aprovado 

    if cont_pedido == True:
        maquina.preparar_cafe(pedido)
