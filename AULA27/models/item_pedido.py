class ItemPedido:
    def __init__(self,nome,qtd,preco):
        self.nome=nome
        self.qtd=qtd
        self.preco=preco
    def __str__(self):
        return f"{self.nome} - {self.qtd}- {self.preco}"
    
    def mostrar(self):
       print(f"{self.nome}-{self.qtd}-{self.preco}")


