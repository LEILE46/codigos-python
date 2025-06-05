numero= int(input("digite um numero:"))
divisores=0

if numero < 2:
    print("nao e  primo")
elif numero % 2 == 0:
    i=1
    while i<=numero:
        if numero % i == 0 :
            divisores +=1
        i+=1
    
if divisores == 2 :
    print("e primo ")
else:
    print("nao e primo")