from .funcionario import Funcionario

class FuncionarioPJ(Funcionario):
    def __init__(self, nome, email, cnpj):
        super().__init__(nome, email)
        self.cnpj = cnpj

    def exibir_dados(self):
        return f"PJ - {self.nome} \n Email: {self.email} \n CNPJ: {self.cnpj}"