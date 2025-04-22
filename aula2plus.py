'''def rodizio_veicular():
    ultimo_numero = int (input("Digite o último número da placa do carro: "))
    
    
    if ultimo_numero == 1 :
        print("Seu carro não pode circular na segunda-feira.")
    elif ultimo_numero == 2:
        print("Seu carro não pode circular na terça-feira.")
    elif ultimo_numero == 3:
        print("Seu carro não pode circular na quarta-feira.")
    elif ultimo_numero == 4:
        print("Seu carro não pode circular na quinta-feira.")
    elif ultimo_numero == 5:
        print("Seu carro não pode circular na sexta-feira.")
    elif ultimo_numero == 6 :
        print("Seu carro não pode circular na segunda-feira.")
    elif ultimo_numero == 7:
        print("Seu carro não pode circular na terça-feira.")
    elif ultimo_numero == 8:
        print("Seu carro não pode circular na quarta-feira.")
    elif ultimo_numero == 9:
        print("Seu carro não pode circular na quinta-feira.")
    elif ultimo_numero == 0:
        print("Seu carro não pode circular na sexta-feira.")
    else:
        print("Número inválido!")

rodizio_veicular()'''

#Calcular o custo estimado de uma viagem de carro
"""def custo_viagem():
    
    distancia = float(input("Informe a distância da viagem em km: "))
    consumo_por_litro = float(input("Informe o consumo do carro em km por litro: "))
    preco_combustivel = float(input("Informe o preço do combustível por litro: "))
   
    litros_necessarios = distancia / consumo_por_litro
    
    custo_total = litros_necessarios * preco_combustivel
    
    print(f"O custo estimado da viagem é: R${custo_total}")

custo_viagem()"""

#Calcular o salário final de um funcionário com comissão de 4% sobre as vendas (Um funcionário recebe um salário fixo mais 4% de comissão sobre vendas. Fazer um programa que receba o salário fixo de um funcionário e o valor de suas vendas, calcule e mostre o valor da comissão e o salário final do funcionário.)
salario_fixo = float(input("Digite o salário fixo do funcionário: R$ "))
vendas = float(input("Digite o valor das vendas realizadas: R$ "))

comissao = vendas * 0.04
salario_final = salario_fixo + comissao

print(f"Comissão sobre as vendas: R$ {comissao}")
print(f"Salário final do funcionário: R$ {salario_final}")

"""numero=int(input("digite um numero:"))

if numero % 2 == 0:
    print("numero e par")
else :
    print ("numero e impar")"""

"""nota=float(input("digite sua nota:"))
nota2=float(input("digite a segunda nota :"))
nota3=float (input("digite a terceira nota: "))
media = (nota+nota2+nota3) /3
if media >=7:
    print("esta aprovado")
elif 5 <=media < 6.9:
    print(" esta de recuperaçao")
else:
    print("esta reprovado")     """


""""quantd_DE_produto_que_comprei=float(input("digite  a quantidade de produtos"))
preço_unitario=float(input("digite o preço unitario:"))
preco_total=quantd_DE_produto_que_comprei * preço_unitario
desconto = preco_total * 0.10
preço_com_desconto= preco_total - desconto
if quantd_DE_produto_que_comprei >=10:
    print(f"vai ter um desconto e seu preço total sera {preço_com_desconto}")
else :
    print(f" esse foi seu preço {preco_total}")"""


"""numero=int(input("digite um numero" ))
dobro= 2 * numero 
triplo= 3* numero 
print (f"o dobro do {numero} e :{dobro}")
print(f"o triplo do {numero} e :{triplo}")"""

"""largura= int(input("digite sua largura:"))
altura= int(input("digite sua altura : "))
resultado= largura*altura
print(f"area do retangulo e {resultado } cm ")"""