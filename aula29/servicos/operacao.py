from servicos.db import conectar

def listar_livros():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    conn.close()
    return livros

def pesquisar_por_autor(autor):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros WHERE autor LIKE %s", ('%' + autor + '%',))
    livros = cursor.fetchall()
    conn.close()
    return livros

def atualizar_preco(id_livro, novo_preco):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE livros SET preco = %s WHERE id = %s", (novo_preco, id_livro))
    conn.commit()
    conn.close()

def remover_livro(id_livro):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM livros WHERE id = %s", (id_livro,))
    conn.commit()
    conn.close()

def livros_por_autor(autor):
    return pesquisar_por_autor(autor)

def aplicar_desconto_em_livros_caros():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE livros SET preco = preco * 0.9 WHERE preco > 50")
    conn.commit()
    conn.close()

def relatorio_estoque_vazio():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros WHERE estoque = 0")
    livros = cursor.fetchall()
    conn.close()
    return livros