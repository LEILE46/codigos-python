def calcular_fatura(consumo):
    faixas = [
        (0, 10, 37.47),  # 1ª faixa
        (10, 15, 1.16),  # 2ª faixa
        (15, 20, 6.46),  # 3ª faixa
        (20, 25, 6.49),  # 4ª faixa
        (25, 35, 6.55),  # 5ª faixa
        (35, 42, 11.08), # 6ª faixa
    ]

    valor_agua = 0


    for faixa in faixas:
        if consumo > faixa[0]:  
            consumo_faixa = min(consumo, faixa[1]) - faixa[0]  
            valor_agua += consumo_faixa * faixa[2]  

    valor_agua_total = valor_agua
    valor_esgoto = valor_agua_total * 0.8 
    valor_total = valor_agua_total + valor_esgoto  

    return valor_agua_total, valor_esgoto, valor_total