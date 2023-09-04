from Cofee_Machine import MENU

class Pagamento:
    """Gerencia o dinheiro do usuário, realiza a compra do café"""
    
    def __init__(_self):
        _self.dinheiro = 5.00
        _self.moedas = {
            "25 centavos": 0.25,
            "10 centavos": 0.10,
            "5 centavos": 0.05,
            "1 centavo": 0.01,
        }
        _self.aprovado = False
         
    
    def verifica_pagamento(_self, pedido):
        """Verifica se o usuário tem dinheiro suficiente para realizar o pedido, caso tenha ele realiza a compra."""

        val_pagar = 0
        custo = 0

        match pedido.lower():
            case 'a':
                custo = MENU["espresso"]["cost"]
            case 'b': 
                custo = MENU["latte"]["cost"]
            case 'c':
                custo = MENU["cappuccino"]["cost"]

        if _self.dinheiro < custo:
            print(f"Você tem {_self.dinheiro}R$, seu pedido custa {custo}R$. Dinheiro insuficiente")
            _self.aprovado = False
        else:
            for moeda in _self.moedas:
                val_pagar += int(input(f"Quantas moedas de {moeda} você deseja utilizar?: ")) * _self.moedas[moeda]
            
            _self.dinheiro -= val_pagar
            _self.dinheiro += val_pagar - custo
            _self.aprovado = True



