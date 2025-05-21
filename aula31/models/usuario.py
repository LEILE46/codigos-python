class Usuario:
    def __init__(self):
        self.__senha = "agua2024" 
    
    def verificar_senha(self, senha_digitada):
        return senha_digitada == self.__senha