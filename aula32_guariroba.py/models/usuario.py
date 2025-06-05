class Usuario:
    def __init__(self, nome, senha=None):
        self._nome = nome
        self._senha = senha  
    def carregar_dados(self):
     
        if self._nome == "admin":
            self._senha = "agua2024" 
    

    def verificar_senha(self, senha):
        return self._senha == senha