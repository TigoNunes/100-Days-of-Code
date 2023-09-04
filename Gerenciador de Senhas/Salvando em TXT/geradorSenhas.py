import random as r

class GeradorSenha:
    """Gera senhas aleatoriamente"""
    def __init__(_self):
        _self.letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 
        "A", "B", "C", "D", 'E', "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        _self.numeros = ["1","2","3","4","5","6","7","8","9","0"]
        _self.symbols = ["+","!","#","(",")"]
        _self.senha = ""
        _self._gerar_senha()
    
    def _gerar_senha(_self):
        """Gera a senha"""
        elementos_senha = [r.choice(_self.letras) for _ in range(r.randint(8,10))]
        elementos_senha += [r.choice(_self.numeros) for _ in range(r.randint(2,4))]
        elementos_senha += [r.choice(_self.symbols) for _ in range(r.randint(2,4))]
        r.shuffle(elementos_senha)
        _self.senha = "".join(elementos_senha)
