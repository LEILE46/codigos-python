from models.cliente import Cliente

class Pedido:
    def __init__(self, numero, valor_total, cliente: Cliente):
        self.numero = numero
        self.valor_total = valor_total
        self.cliente = cliente

    def __str__(self):
        return f"Pedido {self.numero} \n R$ {self.valor_total} \n Cliente: {self.cliente}"
