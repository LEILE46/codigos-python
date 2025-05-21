import mysql.connector
from tkinter import messagebox

def conectar():
    conn = mysql.connector.connect(host="localhost", user="root", password="")
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS livraria_db")
    conn.database = "livraria_db"
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros (
            id INT AUTO_INCREMENT PRIMARY KEY,
            titulo VARCHAR(255),
            autor VARCHAR(255),
            preco DECIMAL(10,2),
            estoque INT
        )
    """)
    return conn, cursor

def inserir_livros(cursor, conn):
    cursor.execute("SELECT COUNT(*) FROM livros")
    if cursor.fetchone()[0] == 0:
        livros = [
            ('O Senhor dos Anéis', 'J.R.R. Tolkien', 120.00, 5),
            ('1984', 'George Orwell', 45.50, 10),
            ('Dom Quixote', 'Miguel de Cervantes', 60.00, 2),
            ('O Pequeno Príncipe', 'Antoine de Saint-Exupéry', 35.00, 0),
            ('Harry Potter', 'J.K. Rowling', 70.00, 8)
        ]
        cursor.executemany("INSERT INTO livros (titulo, autor, preco, estoque) VALUES (%s, %s, %s, %s)", livros)
        conn.commit()

def exibir_livros(cursor):
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    texto = "\n".join([f"{id} - {titulo} ({autor}) R$ {preco} - Estoque: {estoque}" for id, titulo, autor, preco, estoque in livros])
    messagebox.showinfo("Livros Cadastrados", texto or "Nenhum livro encontrado.")

def pesquisar_por_autor(cursor, autor):
    cursor.execute("SELECT * FROM livros WHERE autor = %s", (autor,))
    livros = cursor.fetchall()
    texto = "\n".join([f"{titulo} - R$ {preco}" for _, titulo, _, preco, _ in livros])
    messagebox.showinfo(f"Livros de {autor}", texto or "Nenhum livro encontrado.")

def atualizar_preco(cursor, conn, id_livro, novo_preco):
    cursor.execute("UPDATE livros SET preco = %s WHERE id = %s", (novo_preco, id_livro))
    conn.commit()
    messagebox.showinfo("Atualizado", f"Livro ID {id_livro} teve o preço atualizado.")

def remover_livro(cursor, conn, id_livro):
    cursor.execute("DELETE FROM livros WHERE id = %s", (id_livro,))
    conn.commit()
    messagebox.showinfo("Removido", f"Livro ID {id_livro} removido.")

def livros_por_autor(cursor, autor):
    cursor.execute("SELECT titulo, preco FROM livros WHERE autor = %s", (autor,))
    livros = cursor.fetchall()
    texto = "\n".join([f"{titulo} - R$ {preco}" for titulo, preco in livros])
    messagebox.showinfo(f"Livros de {autor}", texto or "Nenhum livro encontrado.")

def aplicar_desconto(cursor, conn):
    cursor.execute("UPDATE livros SET preco = preco * 0.9 WHERE preco > 50")
    conn.commit()
    messagebox.showinfo("Desconto Aplicado", "Desconto de 10% aplicado nos livros acima de R$ 50.")

def relatorio_estoque(cursor):
    cursor.execute("SELECT titulo FROM livros WHERE estoque = 0")
    livros = cursor.fetchall()
    texto = "\n".join([titulo for (titulo,) in livros])
    messagebox.showinfo("Fora de Estoque", texto or "Todos os livros estão disponíveis.")