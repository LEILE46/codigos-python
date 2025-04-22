"""import turtle  # Importando a biblioteca Turtle

# Criando a tela do desenho
tela = turtle.Screen()
tela.bgcolor("white")  # Cor do fundo
tela.title("Desenhando com Turtle")  # Título da janela

# Criando o objeto Turtle
desenho = turtle.Turtle()
desenho.speed(3)  # Velocidade do desenho

# Pedindo ao usuário para escolher a cor
cor = input("Escolha a cor do desenho: ")

# Definindo a cor do desenho
desenho.color(cor)

# Estrutura para garantir uma opção válida
while True:
    # Perguntando ao usuário qual forma desenhar
    print("Escolha a forma geométrica para desenhar:")
    print("1 - Quadrado")
    print("2 - Triângulo")
    print("3 - Círculo")

    opcao = int(input("Digite o número da opção desejada: "))
    
    if opcao in [1, 2, 3]:
        break  # Sai do laço se a opção for válida
    else:
        print("Opção inválida! Escolha 1, 2 ou 3.")

# Perguntando o tamanho do lado ou raio
tamanho = int(input("Digite o tamanho do lado ou raio: "))

# Estrutura condicional para desenhar a forma escolhida
if opcao == 1:
    for _ in range(4):  # Quadrado tem 4 lados
        desenho.forward(tamanho)  # Anda para frente
        desenho.right(90)  # Gira 90 graus para a direita
elif opcao == 2:
    for _ in range(3):  # Triângulo tem 3 lados
        desenho.forward(tamanho)  # Anda para frente
        desenho.right(120)  # Gira 120 graus para a direita
elif opcao == 3:
    desenho.circle(tamanho)  # Desenha um círculo com o raio dado

# Finaliza o desenho
turtle.done()"""


# Par ou Ímpar


"""numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")"""


#maior entre dois números


"""
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))


if numero1 > numero2:
    print(f"O maior número é {numero1}.")
elif numero1 < numero2:
    print(f"O maior número é {numero2}.")
else:
    print("Os dois números são iguais.")"""


# Cálculo de Desconto


"""preco = float(input("Digite o valor do produto: R$ "))

if preco > 100:
    desconto = preco * 0.10
elif preco >= 50:
    desconto = preco * 0.05
else:
    desconto = 0


preco_final = preco - desconto
print(f"O preço final do produto com desconto é: R$ {preco_final}")"""


#Verificação de Maioridade


"""idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")"""


#Classificação de um Número

"""numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")"""


# Cálculo de Média e Situação do Aluno
"""
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f"Média: {media:.1f}. Você foi aprovado!")
elif media >= 5:
    print(f"Média: {media:.1f}. Você está em recuperação.")
else:
    print(f"Média: {media:.1f}. Você foi reprovado.")"""
 
 
 
 #Calculadora Simples

"""numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Erro! Divisão por zero."
else:
    resultado = "Operação inválida!"

print(f"Resultado: {resultado}")"""



# 8️ Classificação de um Triângulo

"""lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

if lado1 == lado2 == lado3:
    print("O triângulo é equilátero.")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("O triângulo é isósceles.")
else:
    print("O triângulo é escaleno.")"""
 
 
 
 #9 Verificação de Múltiplos

"""numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 % numero2 == 0:
    print(f"{numero1} é múltiplo de {numero2}.")
else:
    print(f"{numero1} não é múltiplo de {numero2}.")"""


#  Conversor de Temperatura

"""celsius = float(input("Digite a temperatura em graus Celsius: "))

conversao = input("Digite 'F' para Fahrenheit ou 'K' para Kelvin: ").upper()

if conversao == 'F':
    fahrenheit = celsius * 1.8 + 32
    print(f"{celsius}°C é igual a {fahrenheit}°F.")
elif conversao == 'K':
    kelvin = celsius + 273.15
    print(f"{celsius}°C é igual a {kelvin}K.")
else:
    print("Opção de conversão inválida!")"""