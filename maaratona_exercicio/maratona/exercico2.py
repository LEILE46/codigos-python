contador=0
palavra= input("digite um palavra:")
vogais=("aeiouAEIOU")
for vogal in palavra :
    if vogal in vogais:
        contador +=1
print(f"tem {contador} nessa palavra")