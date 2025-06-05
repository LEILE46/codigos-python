from data.db import criar_tabela
from view.login import tela_login

def main():
    criar_tabela()
    tela_login()

if __name__ == "__main__":
    main()