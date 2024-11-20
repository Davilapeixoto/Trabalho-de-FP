import random
nume=int(input("digite n 6"))
print("Treino aleatorio: ")
if nume==6:
    numeros= [1,2,3,4,5,6,7]
    treino_aleat = ["treino1: treino de sprint: correr 1 minuto andar 2 minutos X 12",
    "treino2: treino força: caminhar com peso em superficie inclinada 30 minutos",
    "treino3: treino misto: correr ate a falha descansar 1:30 minutos X 15",
    "treino4: treino de fadiga: correr sem pausa",  
    "treino5: treino de sfinkter: fazer escala de corrida/andada 10x4",
    "treino6: treino de jogador: set de 1 hora com pace alto",
    "treino7: treino de ronnie: afunedo ate a falha"]
    random.shuffle(numeros)
    print(numeros)
