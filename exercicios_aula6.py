"""for i in range(1, 21):
    if i % 2 == 0:
       print(i)"""
 
 # atividade 2
"""numero = int(input("Digite um número para ver sua tabuada: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")"""

#atividade 3
"""for i in range(10, 0, -1):
    print(i)
print("FIM!")"""

#atividade 4
"""soma = 0
for i in range(5):
    numero = int(input("Digite um número: "))
    soma += numero
print(f"A soma dos números informados é: {soma}")"""

# Exercício 5 - Verificar a Quantidade de Vogais em uma Palavra
"""palavra = input("Digite uma palavra: ")
vogais = 'aeiouAEIOU'  
contagem_vogais = 0

for letra in palavra:
    if letra in vogais:
        contagem_vogais += 1

print(f"A quantidade de vogais na palavra '{palavra}' é: {contagem_vogais}")"""


# desafio 1 
"""n= int(input("digite um numero inteiro"))
if n <=0 :
    print("por favor, insira um numero inteiro positivo")
else:
    a,b=0,1
    for i in range (n):
        print(a, end=' ')
        a,b=b,a+b"""

#desafio 2
"""for i in range(1, 31):
    if i % 3 == 0:
        print(i)"""

#desafio3 
"""soma = 0
for i in range(1, 51):
    if i % 2 != 0:
        soma += i
print(f'A soma dos números ímpares entre 1 e 50 é: {soma}')"""

#desafio 4
"""frase = input("Digite uma frase: ")
contador = 0

for letra in frase:
    if ('a' <= letra <= 'z') or ('A' <= letra <= 'Z'): 
        contador += 1

print(f'O número de letras na frase é: {contador}')"""

#desafio 5
"""numero = int(input("Digite um número para verificar se é primo: "))
if numero > 1:
    for i in range(2, numero):
        if numero % i == 0:
            print(f'O número {numero} não é primo.')
            break
    else:
        print(f'O número {numero} é primo.')
else:
    print(f'O número {numero} não é primo.')"""


#desafio 6
"""n = int(input("Quantos números você quer digitar? "))
soma = 0
for i in range(n):
    num = float(input(f"Digite o {i + 1}º número: "))
    soma += num
media = soma / n
print(f'A média dos números digitados é: {media}')"""

#desafio 7
"""palavra = input("Digite uma palavra: ")
print(f'A palavra ao contrário é: {palavra[::-1]}')"""
   
#desafio 8
"""maior_numero = None

for i in range(5):
    num = int(input(f"Digite o {i + 1}º número: "))
    
    if maior_numero is None or num > maior_numero:
        maior_numero = num

print(f'O maior número digitado foi: {maior_numero}')"""
 #deafio 9
"""palavra = input("Digite uma palavra: ")
letra = input("Digite a letra que deseja contar: ")
contagem = 0

for i in palavra:
    if i == letra:
        contagem += 1

print(f'A letra "{letra}" aparece {contagem} vezes na palavra "{palavra}".')"""

#desafio 10
"""n = int(input("Digite o número de linhas para a pirâmide: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))"""