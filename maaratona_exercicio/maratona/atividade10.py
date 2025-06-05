entrada=input("digite numeros separados por espaço: ")
numero=[]
numero_atual=""
for i in entrada:
    if i !=" ":
        numero_atual += i
    else:
        if numero_atual != "":
            numero.append(int(numero_atual))
            numero_atual=""
if  numero_atual != "":
    numero.append(int(numero_atual))

for j in range (len(numero)):
    for k in range (0 , len (numero)-j-1):
        if numero [k]> numero [k+1]:
            numero[k] , numero [k+1]=numero[k+1], numero [k]
print("lista ordenada",numero)