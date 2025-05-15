class Funcionario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def exibir_dados(self):
        raise NotImplementedError("O método exibir_dados() precisa ser implementado na subclasse.")