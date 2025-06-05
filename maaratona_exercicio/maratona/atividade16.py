expressao=input("digite uma expressao simples (ex:3+4):")
num1_str=""
num2_str=""
operador=""
i=0

while i < len(expressao) and (expressao[i]>='0' and expressao [i]<='9'):
    num1_str=num1_str+ expressao[i]
    i=i+1

while i< len(expressao) and expressao [i]==" ":
    i=i+1
if i < len(expressao):
    operador =expressao[i]
    i=i+1
else:
    print("expressao invalida")

while i< len(expressao) and expressao [i]==" ":
    i=i+1

while i < len(expressao) and (expressao[i]>='0' and expressao [i]<='9'):
    num2_str=num2_str+ expressao[i]
    i=i+1

if num1_str == "" or num2_str == "" or operador == "":
    print("expressao invalida")
else:
    num1= int(num1_str)
    num2=int(num2_str)


    if operador == '+':
        resultado=num1+num2
    elif operador == '-':
        resultado=num1-num2
    elif operador == '*':
        resultado = num1*num2
    elif operador == '/':
        if num2 == 0 :
            print("erro: divisao por zero")
        else:
            print("operador invalido")
          
    print("resultado: ",resultado)
    