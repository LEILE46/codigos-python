rom servico.database import get_connection
from models.alimento import Alimento
from datetime import datetime

def cadastrar_alimento(nome, validade, quantidade, usuario):
    try:
        validade_date = datetime.strptime(validade, "%Y-%m-%d").date()
        if validade_date < datetime.today().date():
            return None  # alimento vencido
    except ValueError:
        return None  # formato inválido

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO alimentos (nome, validade, quantidade, doador_id) VALUES (%s, %s, %s, %s)",
                (nome, validade, quantidade, usuario.id)
            )
            conn.commit()

    return Alimento(None, nome, validade, quantidade, usuario.id)

def listar_alimentos_disponiveis():
    with get_connection() as conn:
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT id, nome, validade, quantidade, doador_id FROM alimentos WHERE validade >= CURDATE()")
            rows = cursor.fetchall()

    alimentos = [Alimento(row['id'], row['nome'], row['validade'], row['quantidade'], row['doador_id']) for row in rows]
    return alimentos

def buscar_alimento_por_id(alimento_id):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM alimentos WHERE id = %s", (alimento_id,))
            alimento_db = cursor.fetchone()

    if alimento_db:
        return Alimento(
            id_=alimento_db[0],
            nome=alimento_db[1],
            validade=alimento_db[2],
            quantidade=alimento_db[3],
            doador_id=alimento_db[4]
        )

    return None