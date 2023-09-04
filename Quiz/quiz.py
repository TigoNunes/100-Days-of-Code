class Quiz:
    """Gerencias as perguntas, respostas do jogador e seus pontos"""
    
    def __init__(self, banco_questoes:list):
        self.num_questao = 0
        self.lista_questoes = banco_questoes
        self.ponto = 0
    
    def proxima_questao(self):
        """Realiza as perguntas ao jogador"""
        for questao in self.lista_questoes:
            resp = input(f"Q.{self.num_questao + 1}: {questao.texto} (True/False): ")
            self.num_questao += 1
            self.verifica_resposta(resp, questao.resposta)

    def restam_questoes(self):
        """Verifica se ainda restam questões"""
        return self.num_questao < len(self.lista_questoes)
    
    def verifica_resposta(self,resposta:str, resposta_questao:str):
        """Verifica se ojogador acertou ou errou a questão"""
        if resposta.lower() == resposta_questao.lower():
            self.ponto += 1
            print(f"Muito bem, você acertou\nacertos: {self.ponto}/{self.num_questao}\n")
        else: print(f"Você errou\nResposta correta: {resposta_questao}\nacertos: {self.ponto}/{self.num_questao}\n")
            

