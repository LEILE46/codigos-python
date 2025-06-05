cpf=input("digite o cpf: ")
cpf_limpo=""
for caractere in cpf:
    if caractere >="0" and caractere <="9":
        cpf_limpo=cpf_limpo+caractere
if len(cpf_limpo)== 11 and  not cpf_limpo == cpf_limpo[0]*11:
    print("CPF valido.")
else:
    print("CPF invalido.")