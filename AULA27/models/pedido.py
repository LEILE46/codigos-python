

class Pedido:
    def __init__(self, cliente, numero, data , item, item2):
        self.cliente = cliente
        self.numero = numero
        self.data = data
        self.item1 = item
        self.item2 = item2
        self.total = self.item1.qtd * self.item1.preco + \
              self.item2.qtd * self.item1.preco
    def __str__(self):
      return f'{self.cliente} - {self.numero} - {self.data} \n' \
                f'{self.item1} \n'*' * 20'\
                f'total :{self.total}'

    def mostrar(self):
       return f'{self.cliente} - {self.numero} - {self.data} \n' \
                f'{self.item1} \n\n'  \
                f'total :{self.total}'