n= int(input("digite o tamanho da matriz identidade: "))
i=0

while i< n:
    j=0
    linha=""
    while j<n:
        if i == j:
            linha=linha+"1"
        else:
            linha=linha+"0"
        j=j+1
    print(linha.strip())
    i=i+1