

import random 


aleatorio = [1,2,3,4,5,6,7]
while True:
    texte= int(input("digite 6 "))
    if texte ==6:
        
            
            n = random.choice(aleatorio)
            remove = aleatorio.remove(n)
            

            #print(n)
            #print(aleatorio)
            with open("pp.txt", "r") as arquivo:
                linhas = [linha.strip() for linha in arquivo.readlines()] 
                #Se você quer ler todas as linhas de uma vez e garantir que cada uma esteja sem a quebra de linha, pode usar readlines() e aplicar strip() em cada linha:
                print(linhas[n-1]) #-1 é pra contar certinho 

                
                # linhasp = linhas[n]
                # print(linhasp)