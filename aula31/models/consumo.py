from .fatura import Fatura

class Consumo:
    def __init__(self, consumo):
        self.consumo = consumo
    
    def calcular(self):
        valor_agua = 37.47  
        consumo_restante = self.consumo - 5  

        if consumo_restante > 5:
            valor_agua += 5 * 1.16  

            consumo_restante -= 5
        elif consumo_restante > 0:
            valor_agua += consumo_restante * 1.16
            consumo_restante = 0

        if consumo_restante > 5:
            valor_agua += 5 * 6.46  
            consumo_restante -= 5
        elif consumo_restante > 0:
            valor_agua += consumo_restante * 6.46
            consumo_restante = 0

        if consumo_restante > 5:
            valor_agua += 5 * 6.49  
            consumo_restante -= 5
        elif consumo_restante > 0:
            valor_agua += consumo_restante * 6.49
            consumo_restante = 0

        if consumo_restante > 10:
            valor_agua += 10 * 6.55 
            consumo_restante -= 10
        elif consumo_restante > 0:
            valor_agua += consumo_restante * 6.55
            consumo_restante = 0

        if consumo_restante > 0:
            valor_agua += consumo_restante * 11.08  

        valor_esgoto = valor_agua * 0.8
        valor_total = valor_agua + valor_esgoto
        
        return Fatura(valor_agua, valor_esgoto, valor_total)