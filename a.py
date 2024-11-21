def checar_data_simples(data):
    # Verifica o tamanho e os delimitadores
    if len(data) == 10 and data[4] == '-' and data[7] == '-':
        ano, mes, dia = data[:4], data[5:7], data[8:]
        # Verifica se ano, mês e dia são numéricos
        return ano.isdigit() and mes.isdigit() and dia.isdigit()
    return False

# Exemplos de uso
datas = ["2029-11-20", "20-11-2024", "2024-13-01", "2024-11-31"]

for data in datas:
    print(f"{data}: {'Válida' if checar_data_simples(data) else 'Inválida'}")
