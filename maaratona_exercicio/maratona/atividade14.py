senha= input("digite a senha: ")
tem_maiuscula=False
tem_numero=False
tem_simbolo=False
simbolos="!@#$%&^*()-_=+[]{}|;:',.<>/?~`"

i=0
while i < len(senha):
    caractere=senha[i]
    if caractere>= 'A' and caractere <='Z':
        tem_maiuscula=True
    if caractere >='0'and caractere <= '9':
        tem_numero=True
    if caractere in simbolos:
        tem_simbolo=True 
    i=i+1
tamanho_valido=len(senha)>=8
if tem_maiuscula and tem_numero and tem_simbolo and tamanho_valido:
    print("senha forte")
else:
    print("senha fraca")