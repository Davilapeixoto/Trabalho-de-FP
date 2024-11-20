import os
import random
import matplotlib.pyplot as plt
from datetime import datetime
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

def gerar_grafico():
    datas = []
    distancias = []
    if os.path.exists("historico.txt"):
        with open("historico.txt", "r") as historico:
            for linha in historico:
                linha = linha.strip()
                if linha.endswith(".txt"):
                    treino_nome = linha.split(":")[0]
                    caminho = linha.split(":")[1]
                    if os.path.exists(caminho):
                        with open(caminho, "r") as treino:
                            data = distancia = None
                            for line in treino:
                                if "Data" in line:
                                    data = line.split(":")[1].strip()
                                elif "Distância" in line:
                                    distancia = float(line.split(":")[1].strip())
                                if data and distancia:
                                    datas.append(data)
                                    distancias.append(distancia)
                                    break

    if datas and distancias:
        sorted_dates = sorted(zip(datas, distancias), key=lambda x: datetime.strptime(x[0], "%Y-%m-%d"))
        sorted_datas, sorted_distancias = zip(*sorted_dates)

        plt.figure(figsize=(10, 6))
        plt.plot(sorted_datas, sorted_distancias, marker='o', linestyle='--', color='b', label='Distância (m)')
        plt.xticks(rotation=45)
        plt.xlabel('Data')
        plt.ylabel('Distância (m)')
        plt.title('Desempenho dos Treinos')
        plt.tight_layout() 
        plt.legend()
        plt.show()
    else:
        print("Não há dados suficientes para gerar o gráfico.")


arquivos_treino=carregar()
while True:
    print("1-Criar um treino\n2-visualizar treinos\n3-analisar treino\n4-atualizar treinos\n5-Implementar Metas e desafios\n6-Treino aleatorio\n7-deletar\n8-limpar terminal\n9-Sair\n10-gerar grafico")
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


    elif esc == 3:
        tipo = input("Você deseja analisar seus treinos por distância ou tempo: ").lower().strip()
        
        if tipo == "distancia":
            try:
                d = float(input("A partir de que distância (em metros): "))
            except ValueError:
                print("Por favor, insira um número válido.")
                continue

            for treino, caminho in arquivos_treino.items():
                if os.path.exists(caminho):
                    with open(caminho, "r") as arquivo:
                        linhas = arquivo.readlines()
                        for linha in linhas:
                            if linha.startswith("Distância:"):
                                try:
                                    distancia = float(linha.split(":")[1].strip())
                                    if distancia > d:
                                        print(f"\nTreino: {treino}")
                                        print("".join(linhas))
                                        break
                                except ValueError:
                                    print(f"Erro ao interpretar a distância no treino {treino}.")
        else:
            print("Análise por tempo ainda não implementada.")

    elif esc==4:
        cont = 0
        
        nome = input("Qual arquivo deseja alterar: ").lower().strip()
        caminho = arquivos_treino.get(nome)
        if caminho and os.path.exists(caminho):
            alterar(nome)
            print("Arquivo alterado")
        else:
            print("Treino não encontrado no histórico ou inexistente.")
    

    elif esc==5:
        velocidade = int(0)
        tempo = int(0)
        distancia = int(0)
        tipo_meta = input("Digite o tipo de meta que você quer implementar: ")
    
    elif esc==6:
        print("Treino aleatorio: ")
        aleatorio = [1,2,3,4,5,6,7]
        n = random.choice(aleatorio)
        remove = aleatorio.remove(n)
        with open("Davila/pp.txt", "r") as arquivo:
                linhas = [linha.strip() for linha in arquivo.readlines()] 
                print(linhas[n-1]) 

    elif esc==7:
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

    elif esc ==8:
        os.system("cls")
    elif esc==9:
        break
    elif esc == 10:
        gerar_grafico()
