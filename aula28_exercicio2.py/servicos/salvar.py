class ServicoSalvarFuncionario:
    def salvar_funcionario(self, funcionario):
        try:
            with open("funcionarios.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(funcionario.exibir_dados() + "\n")
        except:
            return False
        return True