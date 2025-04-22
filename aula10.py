"""def verificar_restricao():
    try:
        numero = int(input("Digite o último número da placa do carro: "))

        if numero in [1, 2]:
            print("Não Circular 2ª Feira")
        elif numero in [3, 4]:
            print("Não Circular 3ª Feira")
        elif numero in [5, 6]:
            print("Não Circular 4ª Feira")
        elif numero in [7, 8]:
            print("Não Circular 5ª Feira")
        elif numero in [9, 0]:
            print("Não Circular 6ª Feira")
        else:
            print("Número inválido!")
    except ValueError:
        print("Por favor, insira um número válido!")


verificar_restricao()"""

#atividade2
def calcular_valor_final():

    cardapio = {
        "Pizza": 30.0,
        "Hamburguer": 20.0,
        "Sushi": 40.0,
        "Salada": 15.0,
        "Lasanha": 35.0
    }

    print("Cardápio:")
    for prato, preco in cardapio.items():
        print(f"{prato}: R${preco:}")

    prato_escolhido = input("Escolha um prato (digite o nome exatamente como aparece acima): ")

    if prato_escolhido not in cardapio:
        print("Prato inválido! Por favor, escolha um prato do cardápio.")
        return

    preco_prato = cardapio[prato_escolhido]

    gorjeta = input("Deseja incluir gorjeta de 10%? (s/n): ").strip().lower()

    if gorjeta == 's':
        total = preco_prato + (preco_prato * 0.10)
        gorjeta_valor = preco_prato * 0.10
        print(f"Preço do prato: R${preco_prato}")
        print(f"Gorjeta (10%): R${gorjeta_valor}")
        print(f"Total a pagar: R${total}")
    else:
        print(f"Preço do prato: R${preco_prato}")
        print("Total a pagar (sem gorjeta): R${}".format(preco_prato))

calcular_valor_final()