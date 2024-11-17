import os
os.system("cls")
def salvar():
    try:
        arquivo = open(f"{nome}.txt", "a")
        data = input("Qual a data: ")
        distancia = float(input("Qual a distância em metros: "))
        tempo = int(input("Qual foi o tempo de corrida em minutos: "))
        localizacao = input("Qual foi a localização: ")
        clima = input("Quais foram as condições climáticas: ")
        treino = input("Como foi o treino: ")
        arquivo.write(f"Data: {data}\nDistância: {str(distancia)}\nTempo: {str(tempo)}\nLocalização: {localizacao}\nClima: {clima}\nTreino: {treino}\n")
        arquivo.close()
        caminho = f"{nome}.txt"
    except ValueError:
        print("Tente um numero")
    except Exception:
        print("Erro inesperado")
    with open("historico.txt", "a") as historico: 
        historico.write(f"{nome}:{caminho}\n")

def alterar(nome):
    try:
        arquivo = open(f"{nome}.txt", "w")
        data = input("Qual a data: ")
        distancia = float(input("Qual a distância em metros: "))
        tempo = int(input("Qual foi o tempo de corrida em minutos: "))
        localizacao = input("Qual foi a localização: ")
        clima = input("Quais foram as condições climáticas: ")
        treino = input("Como foi o treino: ")
        arquivo.write(f"Data: {data}\nDistância: {str(distancia)}\nTempo: {str(tempo)}\nLocalização: {localizacao}\nClima: {clima}\nTreino: {treino}\n")
        arquivo.close()
        caminho = f"{nome}.txt"
    except ValueError:
        print("Tente um numero")
    except Exception:
        print("Erro inesperado")

def carregar():
    arquivo_nome={}
    if os.path.exists("historico.txt"):
        with open("historico.txt", "r") as historico:
            for linha in historico:
                linha = linha.strip()
                if ":" in linha:
                    chave, caminho = linha.split(":", 1)
                    arquivo_nome[chave] = caminho

    return arquivo_nome
arquivos_treino=carregar()
while True:
    print("1-Criar um treino\n2-visualizar treinos\n3-atualizar treinos\n4-deletar\n5-limpar terminal\n6-Sair")
    try:
        esc = int(input("O que deseja?\n"))
    except ValueError:
        print("Tente um número válido")
        continue
    if esc==1:
        nome = input("Qual o nome do novo treino: ")
        if os.path.exists(f"{nome}.txt"):
            print("Treino existente: Use outro nome")
        else:
            salvar()
            arquivos_treino=carregar()


    elif esc == 2:
        cont = 0
        for treino in arquivos_treino:
            print(f"Treino {cont + 1}: {treino}")
            cont += 1
        nome = input("Qual arquivo deseja ver: ").lower().strip()
        caminho = arquivos_treino.get(nome)
        if caminho and os.path.exists(caminho):
            with open(caminho, "r") as arquivo:
                print(arquivo.read())
        else:
            print("Arquivo não encontrado no histórico ou inexistente.")


    elif esc==3:
        cont = 0
        for treino in arquivos_treino:
            print(f"Treino {cont + 1}: {treino}")
            cont += 1
        nome = input("Qual arquivo deseja alterar: ").lower().strip()
        caminho = arquivos_treino.get(nome)
        if caminho and os.path.exists(caminho):
            alterar(nome)
            print("Arquivo alterado")
        else:
            print("Treino não encontrado no histórico ou inexistente.")
    elif esc==4:
        cont = 0
        for treino in arquivos_treino:
            print(f"Treino {cont + 1}: {treino}")
            cont += 1
        nome = input("Qual arquivo deseja apagar: ").lower().strip()
        if nome in arquivos_treino:
            caminho = arquivos_treino.pop(nome)
            if os.path.exists(caminho):
                os.remove(caminho)
            with open("historico.txt", "r") as historico:
                linhas = historico.readlines()
            with open("historico.txt", "w") as historico:
                for linha in linhas:
                    if not linha.startswith(f"{nome}:"):
                        historico.write(linha)
        else:
            print("Treino não existe")

    elif esc ==5:
        os.system("cls")
    elif esc==6:
        break

        print("data")