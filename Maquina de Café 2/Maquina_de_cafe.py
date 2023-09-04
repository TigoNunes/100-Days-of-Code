from Cofee_Machine import MENU, resources

class Maquina_de_Cafe:
    """Gerencia a máquina, seus recursos e prepara o café"""
    def retorna_recursos(_self):
        """Retorna os recursos disponíveis ná maquina"""

        for res in resources:
                print(f"{res}: {resources[res]}")

    def verifica_ingredientes(_self, pedido):
        """Verifica se os ingredientespara o pedido estão disponíveis."""
        
        match pedido.lower():
            case 'a':
                if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]: return True
                elif resources["water"] < MENU["espresso"]["ingredients"]["water"]:
                    print("Agua insuficiente para este pedido\n")
                    return False
                elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
                    print("Café insuficiente para este pedido\n")
                    return False
                else:
                    print("Leite insuficiente para este pedido\n")
                    return False               
            case 'b': 
                if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"] and resources["milk"] >= MENU["latte"]["ingredients"]["milk"]: return True
                elif resources["water"] < MENU["espresso"]["ingredients"]["water"]:
                    print("Agua insuficiente para este pedido\n")
                    return False
                elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
                    print("Café insuficiente para este pedido\n")
                    return False
                else:
                    print("Leite insuficiente para este pedido\n")
                    return False 
            case 'c':
                if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"] and resources["milk"] >= MENU["latte"]["ingredients"]["milk"]: return True
                elif resources["water"] < MENU["espresso"]["ingredients"]["water"]:
                    print("Agua insuficiente para este pedido\n")
                    return False
                elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
                    print("Café insuficiente para este pedido\n")
                    return False
                else:
                    print("Leite insuficiente para este pedido\n")
                    return False 
        
    def preparar_cafe(_self, pedido):
        """Subtrai os ingradientes do estoque e "prepara" o café."""

        match pedido.lower():
            case 'a':
                resources['water']= resources['water'] - MENU["espresso"]["ingredients"]["water"] 
                resources['coffee']= resources['coffee'] - MENU["espresso"]["ingredients"]["coffee"]
                
                print("Aqui está seu espresso")
            case 'b': 
                resources['water']= resources['water'] - MENU["latte"]["ingredients"]["water"]
                resources['coffee']= resources['coffee'] -  MENU["latte"]["ingredients"]["coffee"]
                resources['milk'] = resources['milk'] - MENU["latte"]["ingredients"]["milk"]
                
                print("Aqui está seu latte")
            case 'c':
                resources['water'] = resources['water'] - MENU["cappuccino"]["ingredients"]["water"]
                resources['coffee']= resources['coffee'] - MENU["cappuccino"]["ingredients"]["coffee"]
                resources['milk'] = resources['milk'] - MENU["cappuccino"]["ingredients"]["milk"]
                
                print("Aqui está seu cappuccino")
                
                