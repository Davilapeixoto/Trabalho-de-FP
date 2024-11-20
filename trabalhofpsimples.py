import os
import matplotlib.pyplot as plt
from datetime import datetime

os.system("cls")

# Função para salvar dados de um treino
def salvar():
    try:
        arquivo = open(f"{nome}.txt", "a")
        data = input("Qual a data (formato YYYY-MM-DD): ")
        distancia = float(input("Qual a distância em metros: "))
        tempo = int(input("Qual foi o tempo de corrida em minutos: "))
        localizacao = input("Qual foi a localização: ")
        clima = input("Quais foram as condições climáticas: ")
        treino = input("Como foi o treino: ")
        arquivo.write(f"Data: {data}\nDistância: {str(distancia)}\nTempo: {str(tempo)}\nLocalização: {localizacao}\nClima: {clima}\nTreino: {treino}\n")
        arquivo.close()
        caminho = f"{nome}.txt"
    except ValueError:
        print("Tente um número")
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

# Função para carregar os arquivos de treino
def carregar():
    arquivo_nome = {}
    if os.path.exists("historico.txt"):
        with open("historico.txt", "r") as historico:
            for linha in historico:
                linha = linha.strip()
                if ":" in linha:
                    chave, caminho = linha.split(":", 1)
                    arquivo_nome[chave] = caminho
    return arquivo_nome

# Função para gerar o gráfico de desempenho dos treinos
def gerar_grafico():
    datas = []
    distancias = []

    # Carregar os treinos do histórico
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
        # Ordenar os dados pela data
        sorted_dates = sorted(zip(datas, distancias), key=lambda x: datetime.strptime(x[0], "%Y-%m-%d"))
        sorted_datas, sorted_distancias = zip(*sorted_dates)

        # Criando o gráfico
        plt.figure(figsize=(10, 6))
        plt.plot(sorted_datas, sorted_distancias, marker='o', linestyle='--', color='b', label='Distância (m)')
        plt.xticks(rotation=45)  # Gira as datas para melhor visualização
        plt.xlabel('Data')
        plt.ylabel('Distância (m)')
        plt.title('Desempenho dos Treinos')
        plt.tight_layout()  # Ajusta o layout para não cortar as datas
        plt.legend()
        plt.show()
    else:
        print("Não há dados suficientes para gerar o gráfico.")

# Função para lidar com metas
def arquivo_metas():
    try:
        if os.path.exists("metas.txt"):
            with open("metas.txt","r") as file:
                metas = file.readlines()
                metas = [meta.strip() for meta in metas]
        else:
            metas = []
            return metas
    except Exception as e:
        print(f"Erro ao carregar o arquivo de metas: {e}")
        return []

def salvar_metas(metas):
    try:
        with open("metas.txt","w") as file:
            for meta in metas:
                file.write(meta + "\n")
    except Exception as e:
        print(f"Erro ao salvar as metas no arquivo: {e}")

def adicionar_meta(metas):
    try:
        descricao = input("Digite a descrição da meta (exemplo: Correr 100 km por mês ou melhorar o tempo em 5 km):")
        metas.append(descricao)
        print("Meta adicionada com sucesso.")
        salvar_metas(metas)
    except Exception as e:
        print(f"Erro ao adicionar a meta: {e}")

def mostrar_metas(metas):
    try:
        if not metas:
            print("Nenhuma meta definida.")
        else:
            print("\nMeta(s) Atual(is):")
            for idx, meta in enumerate(metas, start=1):
                print(f"{idx}.{meta}")
    except Exception as e:
        print(f"Erro ao exibir as metas: {e}")

def registrar_progresso(metas):
    try:
        if not metas:
            print("Não há metas para registrar o progresso em.")
            return
        mostrar_metas(metas)
        meta_id = int(input("Escolha o número da meta para registrar o progresso em: "))
        if 1 <= meta_id <= len(metas):
            progresso = input("Digite o progresso(exemplo: Corri 10 km): ")
            print(f"Progresso registrado: {progresso} para a meta: {metas[meta_id - 1]}")
        else:
            print("Número de meta inválido.")
    except ValueError:
        print("Por favor, insira um número válido.")
    except Exception as e:
        print(f"Erro ao registrar o progresso: {e}")

# Menu principal
while True:
    print("1-Criar um treino\n2-Visualizar treinos\n3-Alterar treino\n4-Atualizar treinos\n5-Implementar Metas e desafios\n6-Treino aleatório\n7-Deletar\n8-Limpar terminal\n9-Sair\n10-Gerar gráfico")
    try:
        esc = int(input("O que deseja?\n"))
    except ValueError:
        print("Tente um número válido")
        continue

    if esc == 1:
        nome = input("Qual o nome do novo treino: ")
        if os.path.exists(f"{nome}.txt"):
            print("Treino existente: Use outro nome")
        else:
            salvar()
            arquivos_treino = carregar()

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

    elif esc == 4:
        tipo = input("Você deseja analisar seu treino por distância ou tempo: ").lower().strip()

    elif esc == 5:
        metas = arquivo_metas()
        while True:
            print("\nSistema de Gerenciamento de Metas")
            print("1. Adicionar uma meta")
            print("2. Mostrar metas")
            print("3. Registrar progresso de uma meta")
            print("4. Sair")
            try:
                opcao = int(input("Escolha uma opção: "))
                if opcao == 1:
                    adicionar_meta(metas)
                elif opcao == 2:
                    mostrar_metas(metas)
                elif opcao == 3:
                    registrar_progresso(metas)
                elif opcao == 4:
                    print("Saindo do sistema.")
                    break
                else:
                    print("Opção inválida. Tente uma opção de 1 a 4.")
            except ValueError:
                print("Insira uma opção válida.")
            except Exception as e:
                print(f"Erro inesperado: {e}")

    elif esc == 6:
        print("Treino aleatório: ")

    elif esc == 7:
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
            print("Treino não existe.")

    elif esc == 8:
        os.system("cls")

    elif esc == 9:
        break

    elif esc == 10:
        gerar_grafico()
