from servico.database import get_connection
from models.avaliacao import Avaliacao

def avaliar_usuario(usuario, nota, comentario):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO avaliacoes (usuario_id, nota, comentario) VALUES (%s, %s, %s)",
                           (usuario.id, nota, comentario))
            conn.commit()

def listar_avaliacoes():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, usuario_id, nota, comentario FROM avaliacoes ORDER BY id DESC")
            rows = cursor.fetchall()

    return [Avaliacao(*row) for row in rows]