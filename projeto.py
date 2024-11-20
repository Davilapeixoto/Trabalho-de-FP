import os
os.system("cls")
import random
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
                print(f"{idx}. {descricao} - {valor}")
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
            progresso = input("Digite o progresso(exemplo: Corri 10 km): ")
            if progresso.isdigit():
                progresso = int(progresso)
                descricao, valor_meta = metas[meta_id - 1]
                valor_meta -= progresso
                if valor_meta < 0:
                    valor_meta = 0
                metas[meta_id - 1] [1] = valor_meta
                print(f"Progresso registrado: {progresso} para a meta de {metas[meta_id - 1][0]} com valor {metas[meta_id - 1][1]}.")
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
while True:
    print("1-Criar um treino\n2-visualizar treinos\n3-analisar treino\n4-atualizar treinos\n5-Implementar Metas e desafios\n6-Treino aleatorio\n7-deletar\n8-limpar terminal\n9-Sair")
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
        tipo=input("Voce deseja analisar seu treinos por distancia ou tempo: ").lower().strip

    elif esc==5:
        metas = arquivo_metas()
        while True:
            print("\nSistema de Gerenciamento de Metas")
            print("1.Adicionar uma meta")
            print("2.Mostrar metas")
            print("3.Registrar progresso de uma meta")
            print("4.Atualizar meta")
            print("5.Sair")

            try:
                opcao = int(input("Escolha uma opção "))
                if opcao == 1:
                    adicionar_meta(metas)
                elif opcao == 2:
                    mostrar_metas(metas)
                elif opcao == 3:
                    registrar_progresso(metas)
                elif opcao == 4:
                    atualizar_meta(metas)
                elif opcao == 5:
                    print("Saindo do sistema.")
                    break
                else:
                    print("Opção inválida.Tente uma opção de 1 á 5")
            except ValueError:
                print("Insira uma opção válida.")
            except Exception as e:
                print(f"Erro inesperado: {e}")
    elif esc==6:
            aleatorio = [1,2,3,4,5,6,7]       
            n = random.choice(aleatorio)
            remove = aleatorio.remove(n)
            
                    
            with open("pp.txt", "r") as arquivo:
                linhas = [linha.strip() for linha in arquivo.readlines()] 
                        #Se você quer ler todas as linhas de uma vez e garantir que cada uma esteja sem a quebra de linha, pode usar readlines() e aplicar strip() em cada linha:
                print(linhas[n-1]) #-1 é pra contar certinho 

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
