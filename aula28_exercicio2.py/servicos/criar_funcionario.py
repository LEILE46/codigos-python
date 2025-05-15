from models.funcionario_clt import FuncionarioCLT
from models.funcionario_pj import FuncionarioPJ

class ServicoCriarFuncionario:
    def criar_funcionario(self, nome, email, tipo, cargo=None, cnpj=None):
        if tipo == "CLT":
            if not cargo:
                return None
            return FuncionarioCLT(nome, email, cargo)
        elif tipo == "PJ":
            if not cnpj:
                return None
            return FuncionarioPJ(nome, email, cnpj)
        else:
            return None