import os 
os.system("cls")



def filtrar_distancia():
    print("DIGITE [1] - Para filtrar por tempo")
    print("DIGITE [2] - Para filtrar por distãncia")
    tipo = int(input("Você deseja analisar seus treinos por tempo [1] ou por distância [2]: "))
    if tipo == 2:
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
                                    if distancia == d:
                                        print(f"\nTreino: {treino}")
                                        print("".join(linhas))  
                                        break
                                except ValueError:
                                    print(f"Erro ao interpretar a distância no treino {treino}.")

    



