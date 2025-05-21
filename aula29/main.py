from servicos.livro_serviços import conectar, inserir_livros
from telas.inteface import iniciar_interface

if __name__ == "__main__":
    conn, cursor = conectar()
    inserir_livros(cursor, conn)
    iniciar_interface(cursor, conn)
    cursor.close()
    conn.close()