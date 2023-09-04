import pandas

def aprendendo():
    #TODO: Abrindo arquivo com pandas
    data = pandas.read_csv("Dia 25/Aprendendo Pandas/Arquivos/weather_data.csv")

    #TODO: Passando dados para uma lista
    # lista = data["temp"].to_list()

    #TODO: calculando os dados  
    # media = sum(lista) / len(lista)
    # # media = round(media, 2)
    # print(media)
    # print(data["temp"].max())

    # TODO: Analisando colunas
    # print(data["day"])
    # print(data[data["temp"] == data["temp"].max()])

    #TODO: Criando dataframe  

    # data_dict = {
    #     "jogadores": ["Tiago", "Matheus", "Artur"],
    #     "classes": ["Paladino", "MAgo", "Guerreiro"]
    # }

    # new_data = pandas.DataFrame(data_dict)
    # new_data.to_csv("Dia 25/Aprendendo Pandas/rpg.csv")

def esquilos():
    data = pandas.read_csv("Dia 25/Aprendendo Pandas/Arquivos/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
    
    pelagem_preta = 0
    pelagem_cinza = 0
    pelagem_vermelha = 0
    
    pelos = data["Primary Fur Color"].to_list()

    for cores in pelos:
        if cores == "Black": pelagem_preta += 1
        elif cores == "Gray": pelagem_cinza += 1
        elif cores == "Cinnamon": pelagem_vermelha += 1
    
    cores_esquilos = {
        "cores": ["Preto", "Cinza", "Vermelho"],
        "quantidade":[pelagem_preta, pelagem_cinza, pelagem_vermelha] 
    } 

    quantidade_esquilos_cada_cor = pandas.DataFrame(cores_esquilos)
    quantidade_esquilos_cada_cor.to_csv("Dia 25/Aprendendo Pandas/Arquivos/Quantidade_de_esquilos_de_cada_cor.csv")

esquilos()