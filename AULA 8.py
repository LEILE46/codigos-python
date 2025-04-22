#exercicio 1
"""numeros=[]
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

maior = numeros[0]
menor = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print(f"O maior número é {maior}")
print(f"O menor número é {menor}")""" 

#Exercício 2 - Contar quantas vezes um número aparece na lista
"""numeros = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

numero_procurado = int(input("Digite o número que você deseja contar: "))

quantidade = 0
for numero in numeros:
    if numero == numero_procurado:
        quantidade += 1

print(f"O número {numero_procurado} aparece {quantidade} vezes na lista.")"""

#Exercício 3 - Soma dos elementos de uma lista
"""numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

soma = 0
for numero in numeros:
    soma += numero

print(f"A soma dos números é {soma}.") """

#Exercício 4 - Ordenar uma lista de nomes
"""nomes = []

for i in range(5):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)

nomes.sort()

print("Nomes em ordem alfabética:")
for nome in nomes:
    print(nome)"""

#exercico 5
"""numeros = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

numeros_sem_duplicados = []
for numero in numeros:
    if numero not in numeros_sem_duplicados:
        numeros_sem_duplicados.append(numero)

print("Lista sem números duplicados:", numeros_sem_duplicados)"""

#Exercício 6 - Imprimir somatório e número por linha
"""numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

somatorio = sum(numeros)

print(f"A soma dos números é: {somatorio}")

print("Os números digitados foram:")
for numero in numeros:
    print(numero)"""

#Exercício 7 - Exibir nomes na ordem inversa por linha
nomes = []

for i in range(5):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)

print("Os nomes digitados foram:")
for nome in nomes:
    print(nome)

print("Os nomes na ordem inversa são:")
for nome in reversed(nomes):
    print(nome)

#Exercício 8 - Valores pares e impares em vetores
"""pares=[]
impares=[]
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"Valores pares: {pares}")
print(f"Valores ímpares: {impares}")"""