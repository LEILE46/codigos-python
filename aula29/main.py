from servicos.db import criar_tabela, inserir_livros_iniciais
from telas.inteface import exibir_livros

if __name__ == "__main__":
    criar_tabela()
    inserir_livros_iniciais()
    exibir_livros()