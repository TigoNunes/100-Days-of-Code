import html

class Quiz:
    """Gerencias as perguntas, respostas do jogador e seus pontos"""
    
    def __init__(self, banco_questoes:list):
        self.num_questao = 0
        self.lista_questoes = banco_questoes
        self.ponto = 0
        self.resposta = ""
    
    def proxima_questao(self):
        """Realiza as perguntas ao jogador"""

        while self.num_questao < len(self.lista_questoes):
            pergunta = html.unescape(self.lista_questoes[self.num_questao].texto)
            self.resposta = self.lista_questoes[self.num_questao].resposta
            self.num_questao += 1
            return f"{pergunta}"
        if self.num_questao == len(self.lista_questoes):
            return("Fim do quiz")

    def restam_questoes(self):
        """Verifica se ainda restam questões"""
        return self.num_questao < len(self.lista_questoes)
    
    def verifica_resposta(self,resposta:str,):
        """Verifica se ojogador acertou ou errou a questão"""
        if resposta.lower() == self.resposta.lower(): return True
        else: return False
            

