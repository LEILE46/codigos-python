pontos_totais = 0

for mes in range(1, 7):
    livros_comprados = int(input(f"Mês {mes}: Digite o número de livros comprados: "))

    if livros_comprados == 0:
        pontos_totais += 0
    elif livros_comprados == 1:
        pontos_totais += 5
    elif livros_comprados == 2:
        pontos_totais += 15
    elif livros_comprados == 3:
        pontos_totais += 30
    else:
        pontos_totais += 60

if 20 <= pontos_totais <= 30:
    brinde = "EcoBag OU Caneta personalizada"
elif 35 <= pontos_totais <= 60:
    brinde = "Um livro (com valor máximo de R$30,00) OU Luminária de cabeceira"
elif pontos_totais > 65:
    brinde = "2 livros (com valor máximo de R$100,00) OU Powerbank"
else:
    brinde = "Sem brindes disponíveis para essa pontuação."

print(f"Você acumulou um total de {pontos_totais} pontos em 6 meses.")
print(f"Você pode escolher o seguinte brinde: {brinde}")

escolha=input ("qual brinde voce escolheu:")
print (f"voce escolheu:{escolha}")