def analise():
    tabuleiro=[]
    n= int(input("Digite o número de campos no tabuleiro: "))
    for i in range(n):
        while True:
            num=int(input(f"campo {i+1}: "))
            if num in [1,0]:
                tabuleiro.append(num)
                break
            else:
                print("tente 1 ou 0")
    nt=tabuleiro.copy()
    for i in range(n):
        vizinho=0
        if tabuleiro[i]==0:
            if (i>0 and tabuleiro[i-1]==1) or (i<n-1 and tabuleiro[i+1]==1):
                nt[i]=1
        elif tabuleiro[i]==1:
            if i>0 and tabuleiro[i-1]==1:
                vizinho+=1
            if i<n-1 and tabuleiro[i+1]==1:
                vizinho+=1
            if vizinho==2:
                nt[i]=3
            elif vizinho==1:
                nt[i]=2
    print("novo tabuleiro")
    print(nt)
analise()