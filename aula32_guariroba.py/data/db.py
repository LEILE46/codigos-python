import sqlite3

def connect():
    return sqlite3.connect('aguas_guariroba.db')

def criar_tabela():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_user(nome, senha):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (nome, senha) VALUES (?, ?)', (nome, senha))
    conn.commit()
    conn.close()

def find_user_by_name(nome):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE nome = ?', (nome,))
    user = cursor.fetchone()
    conn.close()
    return user