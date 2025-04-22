#Exercício 1 - Criar um retângulo de asteriscos
"""largura=int(input("digite a largura :"))
altura=int(input("digite a altura:"))
if (largura == altura):
    print("nao e um retangulo,tente denovo !!!😁")
else:
    for i in range(altura):
        for j in range (largura):
            print("*",end="")
        print()"""

#Exercício 2 - Exibir a tabuada de 1 a 10
"""for i in range (1,11):
    for j in range (1,11):
        print(f"{i} x {j}= {i*j}",end="\t")
    print ()"""

#Exercício 3
"""n= int(input("Digite um numero:"))
if n >=10:
    print("nao sera um triangulo,entao refaça ")
else:
    for i in range (1,n+1):
        for j in range (1,i + 1):
            print(j, end="")
        print()"""

#exercicio 4
"""for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()""" 

#Exercício 5 - Criar uma matriz de números
"""num = 1
for i in range(5):
    for j in range(5):
        print(num, end=" ")
        num += 1
    print()"""
#Desafio Extra para os Alunos exercicio 6
"""N = int(input("Informe o valor de N (um número ímpar): "))
for i in range(1, N + 1, 2):
    for j in range((N - i) // 2):
        print(" ", end="")
  
    for j in range(i):
        print("*", end="")
    print()
for i in range(N - 2, 0, -2):
    for j in range((N - i) // 2):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()"""