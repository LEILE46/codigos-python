nota1=float(input(f"digite a 1°nota:"))
nota2=float(input(f"digite a 2°nota:"))
nota3=float(input(f"digite a 3° nota:"))

media= (nota1+nota2+nota3) / 3
print(f"media:{media}")
if media>=6 :
    print("aprovado") 
else:
    print("reprovado")       