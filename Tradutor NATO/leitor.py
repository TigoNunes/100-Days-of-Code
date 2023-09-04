import pandas

class Leitor:
    """Lê e obtem dados do arquivo csv"""
    def __init__(self, caminho_arquivo):
        self.dados = pandas.read_csv(caminho_arquivo)
    
    def criar_dicionario(self):
        """cria um dicionario com os dados do arquivo"""
        dic_nato = {conteudo.letter:conteudo.code for (index, conteudo) in self.dados.iterrows()}
        return dic_nato