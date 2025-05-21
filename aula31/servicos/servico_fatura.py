from models.consumo import Consumo

class ServicoFatura:
    def calcular_fatura(self, consumo):
        consumo_obj = Consumo(consumo)
        fatura = consumo_obj.calcular()
        return fatura