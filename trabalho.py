import os
os.system("cls")
arquivos_nome={}
arquivos_data={}
arquivos_tempo={} #essas 3 bibliotecas foram criadas para armazenar o valor e pesquisar facilitar a pesquisa. isso pode ser uma medida temporaria.
def s_historico():# esse def serve para salvar todos os caminhos no historico
    historico=open("trabalho/historico.txt","w")
    historico.write("[Nome]\n")# Aqui esta [Nome] porque elas se tornaram etiquetas para conseguir designar ao local certo
    for nome,caminho in arquivos_nome.items():
        historico.write(f"{nome}:{caminho}\n")
    historico.write("[Data]\n")
    for data,caminho in arquivos_data.items():
        historico.write(f"{data}:{caminho}\n")
    historico.write("[Tempo]\n")
    for tempo,caminho in arquivos_tempo.items():
        historico.write(f"{tempo}:{caminho}\n")
    historico.close()

def c_historico(): #esse def serve para carregar todos os caminhos no historico
    histo=None
    if os.path.exists("trabalho/historico.txt"):
        historico=open("trabalho/historico.txt","r")
        for linha in historico:
            linha=linha.strip()
            if linha=="[Nome]":
                histo=arquivos_nome
            elif linha=="[Data]":
                histo=arquivos_data
            elif linha=="[Tempo]":
                histo=arquivos_tempo
            elif linha and histo is not None:
                chave, caminho = linha.split(":")
                histo[chave]=caminho
        historico.close()
    return arquivos_nome, arquivos_data, arquivos_tempo
arquivos_nome, arquivos_data, arquivos_tempo = c_historico()


while True:
    print("1-Criar um treino\n2-visualizar treinos\n3-atualizar treinos\n4-deletar\n5-limpar terminal\n6-Sair")
    try:
        esc=int(input("Oque deseja?\n"))
    except NameError:
        print("Tente um numero")
    except ValueError:
        print("Use um numero")
    if esc==1:
        nome=input("Qual o nome do novo treino: ")
        if os.path.exists(f"trabalho/{nome}.txt"):
            print("Use outro nome")
        else:
            arquivo=open(f"trabalho/{nome}.txt","a")
            treino=input("Como foi o treino: ")
            data=input("Qual a data: ")
            distancia=input("Qual a distancia: ")
            tempo=input("Qual foi o tempo de corrida: ")
            localizacao=input("Qual foi a localização: ")
            clima=input("Quais foram as condições climaticas: ")
            arquivo.write(f"Data: {data}\nDistancia: {distancia}\nTempo: {tempo}\nLocalização: {localizacao}\nClima: {clima}\nTreino: {treino}\n")
            arquivo.close()
            caminho = f"trabalho/{nome}.txt"
            arquivos_nome[nome] = caminho
            arquivos_data[data] = caminho
            arquivos_tempo[tempo] = caminho
            s_historico()

    elif esc==2:
        escolha=input("Voce deseja pesquisar por Nome/Data/Tempo: ").lower().strip()
        nome=input("Qual o treino")
        if escolha=="nome" and nome in arquivos_nome:
            caminho=arquivos_nome[nome]
        elif escolha=="data" and nome in arquivos_data:
            caminho=arquivos_data[nome]
        elif escolha=="tempo" and nome in arquivos_tempo:
            caminho=arquivos_tempo[nome]
        else:
            print("Arquivo Inexistente")
            continue
        with open(caminho,"r") as ler:
            print(ler.read())


    elif esc==3:
        nome=input("Qual o nome do arquivo que deseja editar: ")
        if nome in arquivos_nome:
            caminho=arquivos_nome[nome]
            arquivo=open(caminho,"w")
            treino=input("Como foi o treino: ")
            data=input("Qual a data: ")
            distancia=input("Qual a distancia: ")
            tempo=input("Qual foi o tempo de corrida")
            localizacao=input("Qual foi a localização: ")
            clima=input("Quais foram as condições climaticas")
            arquivo.write(f"Data: {data}\nDistancia: {distancia}\nTempo: {tempo}\nLocalização: {localizacao}\nClima: {clima}\nTreino: {treino}\n")
            arquivo.close()
            arquivos_data = {chave: entrada for chave, entrada in arquivos_data.items() if entrada != caminho}
            arquivos_tempo = {chave: entrada for chave, entrada in arquivos_tempo.items() if entrada != caminho}
            arquivos_data[data] = caminho
            arquivos_tempo[tempo] = caminho
            s_historico()
    elif esc==4:
        if os.path.exists("trabalho/treinos.txt"):
            os.remove("trabalho/treinos.txt")

    elif esc==5:
        os.system("cls")


    elif esc==6:
        os.system("cls")
        break


    else:
        print("numero invalido")