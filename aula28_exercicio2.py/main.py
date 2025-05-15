import tkinter as tk
from telas.tela_funcionario import TelaCadastroFuncionario

if __name__ == "__main__":
    janela = tk.Tk()  
    app = TelaCadastroFuncionario(janela)  
    janela.mainloop()