import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="seu_usuario",
        password="sua_senha",
        database="livraria"
    )

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros (
            id INT AUTO_INCREMENT PRIMARY KEY,
            titulo VARCHAR(255),
            autor VARCHAR(255),
            preco FLOAT,
            estoque INT
        )
    """)
    conn.commit()
    conn.close()

def inserir_livros_iniciais():
    livros = [
        ("Dom Casmurro", "Machado de Assis", 39.90, 10),
        ("O Cortiço", "Aluísio Azevedo", 45.00, 5),
        ("Memórias Póstumas", "Machado de Assis", 55.00, 2),
        ("Capitães da Areia", "Jorge Amado", 42.50, 0),
        ("Grande Sertão: Veredas", "Guimarães Rosa", 70.00, 1),
    ]
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM livros")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("INSERT INTO livros (titulo, autor, preco, estoque) VALUES (%s, %s, %s, %s)", livros)
        conn.commit()
    conn.close()