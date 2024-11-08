import os
os.system("cls")
arquivos_nome={}
arquivos_data={}
arquivos_tempo={}
while True:
    print("1-Criar um treino\n2-visualizar treinos\n3-atualizar treinos\n4-deletar\n5-limpar terminal\n6-Sair")
    try:
        esc=int(input("Oque deseja?\n"))
    except NameError:
        print("Tente um numero")
    if esc==1:
        nome=input("Qual o nome do novo arquivo")
        if os.path.exists(f"trabalho/{nome}.txt"):
            print("Use outro nome")
        else:
            arquivo=open(f"trabalho/{nome}.txt","a")
            treino=input("Como foi o treino: ")
            data=input("Qual a data: ")
            distancia=input("Qual a distancia: ")
            tempo=input("Qual foi o tempo de corrida")
            localizacao=input("Qual foi a localização: ")
            clima=input("Quais foram as condições climaticas")
            arquivo.write(f"Data: {data}\nDistancia: {distancia}\nTempo: {tempo}\nLocalização: {localizacao}\nClima: {clima}\nTreino: {treino}\n")
            caminho=f"trabalho/{nome}.txt"
            arquivos_nome[nome]=caminho
            arquivos_data[data]=caminho
            arquivos_tempo[tempo]=caminho
            arquivo.close()

    elif esc==2:
        escolha=input("Voce deseja pesquisar por Nome/Data/Tempo: ").lower().strip()
        nome=input("Qual o treino")
        if escolha=="nome" and nome in arquivos_nome:
            caminho=arquivos_nome[nome]
        elif escolha=="data" and nome in arquivos_data:
            caminho=arquivos_data[data]
        elif escolha=="tempo" and nome in arquivos_tempo:
            caminho=arquivos_tempo[tempo]
        else:
            print("Arquivo Inexistente")
            continue
        with open(caminho,"r") as ler:
            print(ler.read())
    elif esc==3:
        arquivo=open("trabalho/treinos.txt","w")
        treino=input("Como foi o treino: ")
        data=input("Qual a data: ")
        distancia=input("Qual a distancia: ")
        tempo=input("Qual foi o tempo de corrida")
        localizacao=input("Qual foi a localização: ")
        clima=input("Quais foram as condições climaticas")
        arquivo.write(f"Data: {data}\nDistancia: {distancia}\nTempo: {tempo}\nLocalização: {localizacao}\nClima: {clima}\nTreino: {treino}\n")
        arquivo.close()
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