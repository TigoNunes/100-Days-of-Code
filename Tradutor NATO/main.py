from leitor import Leitor

caminho_arquivo = "Tradutor NATO/arquivos/nato_phonetic_alphabet.csv"

leitor = Leitor(caminho_arquivo)

dicionario = leitor.criar_dicionario()
while True:
    palavra_usuario = input("Qual o seu nome?: ").upper()
    palavra_usuario = [letra for letra in palavra_usuario]

    try:
        palavra_modificada = [dicionario[letra] for letra in palavra_usuario]
    except KeyError as erro:
        print(f"Ocorreum um erro de digitação, o caracter {erro} não é uma letra")
    else:
        break

print(palavra_usuario)
print(palavra_modificada)