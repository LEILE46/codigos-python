from .funcionario import Funcionario

class FuncionarioCLT(Funcionario):
    def __init__(self, nome, email, cargo):
        super().__init__(nome, email)
        self.cargo = cargo

    def exibir_dados(self):
        return f"CLT - {self.nome} | Email: {self.email} | Cargo: {self.cargo}"