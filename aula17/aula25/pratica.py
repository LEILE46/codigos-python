




try:
    n1=int(input("numero1:"))
    n2=int(input("numero2:"))
    divisao=n1/n2
    print (divisao)
except (ValueError,ZeroDivisionError) as  erro:
    print("erro: " , erro)
else:
    ...
finally:
    print()