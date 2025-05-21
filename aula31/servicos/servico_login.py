from models.usuario import Usuario

class ServicoLogin:
    def __init__(self):
        self.usuario = Usuario()
    
    def autenticar(self, senha_digitada):
        return self.usuario.verificar_senha(senha_digitada)