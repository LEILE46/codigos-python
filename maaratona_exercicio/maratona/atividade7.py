
frase=input("digite uma palavra ou frase:").lower()
frase_sem_espaço=""
for letra in frase :
    if letra != " ":
        frase_sem_espaço +=letra

if frase_sem_espaço == frase_sem_espaço[::-1]:
   print("e um polimetro")
else:
    print ("nao e um polimetro")