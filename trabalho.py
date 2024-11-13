import os
os.system("cls")
while True:
    print("1-Criar um treino\n2-visualizar treinos\n3-atualizar treinos\n4-deletar\n5-limpar terminal\n6-Sair")
    try:
        esc=int(input("Oque deseja?\n"))
    except NameError:
        print("Tente um numero")
    if esc==1:
        arquivo=open("trabalho/treinos.txt","a")
        treino=input("Como foi o treino: ")
        data=input("Qual a data: ")
        distancia=input("Qual a distancia: ")
        tempo=input("Qual foi o tempo de corrida")
        localizacao=input("Qual foi a localização: ")
        clima=input("Quais foram as condições climaticas")
        arquivo.write(f"Data: {data}\nDistancia: {distancia}\nTempo: {tempo}\nLocalização: {localizacao}\nClima: {clima}\nTreino: {treino}\n")
        arquivo.close()

    elif esc==2:
        leitura=open("trabalho/treinos.txt","r")
        print(leitura.read())
        leitura.close()
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