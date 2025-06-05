frase= input("digite uma frase:").strip()
palavras=False
contador=0
for i in frase :
    if i  != " " and not palavras:
        contador+=1
        palavra=True
    elif i == " ":
        palara=False
print("numero de palavras:",contador)