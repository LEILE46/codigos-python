import pymysql.cursors

def get_connection():
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="",  # Adicione sua senha aqui, se necessário
            database="doacao_alimentos",
            cursorclass=pymysql.cursors.DictCursor  # Usando DictCursor para trabalhar com dicionários
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None