import os
import random
os.system("cls")
try:    
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    print("Modulo não encontrado, instale a matplotlib")
    input("Pressione Enter para voltar ao menu!")
from datetime import datetime

def salvar():
    try:
        arquivo = open(f"{nome}.txt", "a")
        tipo=input("Qual o tipo de exercicio (Exemplo corrida ou maratona): ")
        while True:
            data = input("Qual a data (YYYY-MM-DD): ")
            if len(data) == 10 and data[4] == '-' and data[7] == '-':
                ano, mes, dia = data[:4], data[5:7], data[8:]
                if ano.isdigit() and mes.isdigit() and dia.isdigit():
                    ano, mes, dia = int(ano), int(mes), int(dia)
                    if 1 <= mes <= 12:
                        dias_no_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                        if mes == 2 and (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
                            dias_no_mes[1] = 29
                        if 1 <= dia <= dias_no_mes[mes - 1]:
                            arquivo.write(data + "\n")
                            print("Data salva com sucesso!")
                            break
                        else:
                            print("Dia inválido. Tente novamente.")
                    else:
                        print("Mês inválido. Tente novamente.")
                else:
                    print("Ano, mês ou dia não são números. Tente novamente.")
            else:
                print("Tente escrever a data no formato (YYYY-MM-DD) Y=ano M-mes D=dia")
        while True:
            try:
                distancia = float(input("Qual a distância em metros: "))
                break
            except ValueError:
                print("tente um numero")
        while True:
            try:
                tempo = float(input("Qual foi o tempo de corrida em minutos: "))
                break
            except ValueError:
                print("tente um numero")
        localizacao = input("Qual foi a localização: ")
        clima = input("Quais foram as condições climáticas: ")
        treino = input(f"Como foi o/a {tipo}: ")
        arquivo.write(f"Tipo: {tipo}\nData: {data}\nDistância: {str(distancia)}\nTempo: {str(tempo)}\nLocalização: {localizacao}\nClima: {clima}\nFeedback: {treino}\n")
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
        tipo=input("Qual o tipo de exercicio (Exemplo corrida ou maratona): ")
        while True:
            data = input("Qual a data (YYYY-MM-DD): ")
            if len(data) == 10 and data[4] == '-' and data[7] == '-':
                ano, mes, dia = data[:4], data[5:7], data[8:]
                if ano.isdigit() and mes.isdigit() and dia.isdigit():
                    ano, mes, dia = int(ano), int(mes), int(dia)
                    if 1 <= mes <= 12:
                        dias_no_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                        if mes == 2 and (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
                            dias_no_mes[1] = 29
                        if 1 <= dia <= dias_no_mes[mes - 1]:
                            arquivo.write(data + "\n")
                            print("Data salva com sucesso!")
                            break
                        else:
                            print("Dia inválido. Tente novamente.")
                    else:
                        print("Mês inválido. Tente novamente.")
                else:
                    print("Ano, mês ou dia não são números. Tente novamente.")
            else:
                print("Tente escrever a data no formato (YYYY-MM-DD) Y=ano M-mes D=dia")
        while True:
            try:
                distancia = float(input("Qual a distância em metros: "))
                break
            except ValueError:
                print("tente um numero")

        while True:
            try:
                tempo = float(input("Qual foi o tempo de corrida em minutos: "))
                break
            except ValueError:
                print("tente um numero")
        localizacao = input("Qual foi a localização: ")
        clima = input("Quais foram as condições climáticas: ")
        treino = input(f"Como foi o/a {tipo}: ")
        arquivo.write(f"Tipo: {tipo}\nData: {data}\nDistância: {str(distancia)}\nTempo: {str(tempo)}\nLocalização: {localizacao}\nClima: {clima}\nFeedback: {treino}\n")
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
    try:
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
    except Exception:
        print("Necessario instalar o matplotlib")
        input("Pressione Enter para voltar ao menu!")




def arquivo_metas():
    try:
        if os.path.exists("metas.txt"):
            with open("metas.txt","r") as file:
                metas = file.readlines()
                metas = [meta.strip().split(",") for meta in metas]
                metas = [[descricao, int(valor)] for descricao, valor in metas]
        else:
            metas = []
        return metas
    except Exception as e:
        print(f"Erro ao carregar o arquivo de metas: {e}")
        return []
    


def salvar_metas(metas):
    try:
        with open("metas.txt","w") as file:
            for descricao, valor in metas:
                file.write(f"{descricao},{valor}\n")
    except Exception as e:
        print(f"Erro ao salvar as metas no arquivo: {e}")



def adicionar_meta(metas):
    try:
        descricao = input("Digite a descrição da meta (exemplo: Correr 100 km por mês ou melhorar o tempo em 5 km):")
        valor_meta = input("Digite o valor da meta (exemplo: 100 para 100 km): ")
        if valor_meta.isdigit():
            metas.append([descricao, int(valor_meta)])
            print("Meta adicionada com sucesso.")
            salvar_metas(metas)
        else:
            print("Insira um valor numérico válido para a meta")
    except Exception as e:
        print(f"Erro ao adicionar a meta: {e}")



def atualizar_meta(metas):
    try:
        if not metas:
            print("Não há metas para atualizar.")
            return
        mostrar_metas(metas)
        meta_id = input("Escolha o número da meta que deseja atualizar: ")
        if meta_id.isdigit() and 1 <= int(meta_id) <= len(metas):
            meta_id = int(meta_id)
            alterar_descricao = input("Você gostaria de alterar a descrição da meta? (s/n) ou sim/não): ")
            if alterar_descricao.lower() == 's' or alterar_descricao.lower() == 'sim':
                nova_descricao = input("Digite a nova descrição da meta: ")
                metas[meta_id - 1][0] = nova_descricao
                print(f"Descrição da meta atualizada para: {nova_descricao}")
                novo_valor = input("Digite o novo valor para a meta: ")
            if novo_valor.isdigit():
                metas[meta_id - 1][1] = int(novo_valor) 
                print(f"Meta atualizada com sucesso para {novo_valor}.")
                salvar_metas(metas)
            else:
                print("Insira um valor numérico válido para a nova meta.")
        else:
            print("Número de meta inválido.")
    except Exception as e:
        print(f"Erro ao atualizar a meta: {e}")



def mostrar_metas(metas):
    try:
        if not metas:
            print("Nenhuma meta definida.")
        else:
            print("\nMeta(s) Atual(is):")
            for idx, (descricao, valor) in enumerate(metas, start=1):
                if valor==0:
                    print(f"{idx}. {descricao} - Concluido")
                else:
                    print(f"{idx}. {descricao} - {valor}km")
    except Exception as e:
        print(f"Erro ao exibir as metas: {e}")



def registrar_progresso(metas):
    try:
        if not metas:
            print("Não há metas para registrar o progresso em.")
            return
        mostrar_metas(metas)
        meta_id = (input("Escolha o número da meta para registrar o progresso em: "))
        if meta_id.isdigit() and 1 <= int(meta_id) <= len(metas):
            meta_id = int(meta_id) 
            progresso = input("Digite o progresso(exemplo: 10): ")
            if progresso.isdigit():
                progresso = int(progresso)
                descricao, valor_meta = metas[meta_id - 1]
                valor_meta -= progresso
                if valor_meta < 0:
                    valor_meta = 0
                metas[meta_id - 1] [1] = valor_meta
                print(f"Progresso registrado: Faltam {metas[meta_id - 1][1]} km ou metros para bater a meta de ({metas[meta_id - 1][0]}).")
                salvar_metas(metas)
                if valor_meta == 0:
                    print(f"a sua meta {descricao} foi atingida.")
            else:
                print("Insira um valor numérico válido para o progresso.")
        else:
            print("Número de meta inválido.")
    except ValueError:
        print("insira um número válido.")
    except Exception as e:
        print(f"Erro ao registrar o progresso: {e}")



def filtrar_distancia():
    try:
        d = float(input("A partir de que distância (em metros): "))
    except ValueError:
        print("Por favor, insira um número válido.")
                
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
                        except Exception:
                            print("Erro inesperado!")



def filtrar_tempos():
    try:
        t = float(input("Qual tempo você quer ver: "))
    except ValueError:
        print("Por favor, insira um número válido.")
                    
    for treino, caminho in arquivos_treino.items():
        if os.path.exists(caminho):
            with open(caminho, "r") as arquivo:
                linhas = arquivo.readlines()
                for linha in linhas:
                    if linha.startswith("Tempo:"):
                        try:
                            tempo = float(linha.split(":")[1].strip())
                            if tempo == t:
                                print(f"\nTreino: {treino}")
                                print("".join(linhas))
                                break
                        except ValueError:
                            print(f"Erro ao interpretar os tempos no treino {treino}.")
                        except Exception:
                            print("Erro inesperado!")

arquivos_treino=carregar()
hist=[]


while True:
    print("1-Criar um treino\n2-visualizar treinos\n3-analisar treino\n4-atualizar treinos\n5-Implementar Metas e desafios\n6-Treino aleatorio\n7-deletar\n8-limpar terminal\n9-Sair\n10-gerar grafico")
    try:
        esc = int(input("O que deseja?\n"))
        if 1 > esc > 10:
            print("Tente um número entre 1 e 10\n")
    except ValueError:
        print("Tente um número válido\n")
        continue


    if esc==1:
        nome = input("Qual o nome do novo treino: ")
        if os.path.exists(f"{nome}.txt"):
            print("Treino/competição existente: Use outro nome\n")
        else:
            salvar()
            arquivos_treino=carregar()


    elif esc == 2:
        if arquivos_treino:
            cont = 0
            for treino in arquivos_treino:
                print(f"Treino/competição {cont + 1}: {treino}")
                cont += 1
            nome = input("Qual arquivo deseja ver: ").lower().strip()
            caminho = arquivos_treino.get(nome)
            if caminho and os.path.exists(caminho):
                with open(caminho, "r") as arquivo:
                    print(arquivo.read())
                    input("Pressione Enter para voltar ao menu!")
            else:
                print("Arquivo não encontrado no histórico ou inexistente.\n")
        else:
            print("Sem Registros")


    elif esc == 3:
        try:
            tipo = int(input("Você deseja analisar seus treinos por distância [1] ou tempo [2]: "))
            if tipo==1:
                filtrar_distancia()
                input("Pressione Enter para voltar ao menu!")
            elif tipo==2:
                filtrar_tempos()
                input("Pressione Enter para voltar ao menu!")
            else:
                print("Analise inválida!\n")
        except ValueError:
            print("Digite um número válido!\n")
                

    elif esc==4:
        if arquivos_treino:
            cont = 0
            for treino in arquivos_treino:
                print(f"Treino/competição {cont + 1}: {treino}")
                cont += 1
            nome = input("Qual arquivo deseja alterar: ").lower().strip()
            caminho = arquivos_treino.get(nome)
            if caminho and os.path.exists(caminho):
                alterar(nome)
                print("Arquivo alterado\n")
            else:
                print("Treino/competição  não encontrado no histórico ou inexistente.\n")
        else:
            print("Sem Registros")
    
    elif esc==5:
        metas = arquivo_metas()
        while True:
            print("\nSistema de Gerenciamento de Metas\n1.Adicionar uma meta\n2.Mostrar metas\n3.Registrar progresso de uma meta\n4.Atualizar meta\n5.Sair")

            try:
                opcao = int(input("Escolha uma opção: "))
                if opcao == 1:
                    adicionar_meta(metas)
                elif opcao == 2:
                    mostrar_metas(metas)
                elif opcao == 3:
                    registrar_progresso(metas)
                elif opcao == 4:
                    atualizar_meta(metas)
                elif opcao == 5:
                    print("Saindo do sistema.\n")
                    break
                else:
                    print("Opção inválida.Tente uma opção de 1 a \n")
            except ValueError:
                print("Insira uma opção válida.\n")
            except Exception as e:
                print(f"Erro inesperado: {e}\n")
    
    elif esc==6:
        print("Treino aleatorio: ")
        treino_aleat = ["Treino1: Treino de sprint: Correr 1 minuto andar 2 minutos X 12",
"Treino2: Treino força: Caminhar com peso em superficie inclinada 30 minutos",
"Treino3: Treino misto: Correr ate a falha descansar 1:30 minutos X 15",
"Treino4: Treino de fadiga: Correr sem pausa",  
"Treino5: Treino de sfinkter: Fazer escala de corrida/andada 10x4",
"Treino6: Treino de jogador: Set de 1 hora com pace alto",
"Treino7: Treino de ronnie: Afunedo ate a falha"]
        while True:
            treino_sugerido = random.choice(treino_aleat)
            if treino_sugerido not in  hist:
                hist.append(treino_sugerido)
                print(treino_sugerido)
                break
            elif len(hist)>=7:
                print("Cota batida\n")
                break


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
                print("Registro apagado")
            with open("historico.txt", "r") as historico:
                linhas = historico.readlines()
            with open("historico.txt", "w") as historico:
                for linha in linhas:
                    if not linha.startswith(f"{nome}:"):
                        historico.write(linha)
        else:
            print("Treino/competição não existe\n")
    elif esc ==8:
        os.system("cls")
    elif esc==9:
        break
    elif esc == 10:
        gerar_grafico()