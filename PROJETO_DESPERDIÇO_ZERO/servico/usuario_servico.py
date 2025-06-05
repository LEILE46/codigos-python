from models.usuario import Usuario
from servico.database import get_connection

def cadastrar_usuario(nome, email, tipo_perfil, localizacao):
    try:
        conn = get_connection()
        
        if conn is None:
            return "Falha ao conectar ao banco de dados"

        with conn.cursor() as cursor:
            # Verificar se o e-mail já está cadastrado
            cursor.execute("SELECT COUNT(*) FROM usuarios WHERE email = %s", (email,))
            count = cursor.fetchone()[0]
            
            if count > 0:
                conn.close()
                return "Email já cadastrado"
            
            # Inserir novo usuário
            cursor.execute(
                "INSERT INTO usuarios (nome, email, tipo_perfil, localizacao, bloqueado) VALUES (%s, %s, %s, %s, %s)",
                (nome, email, tipo_perfil, localizacao, False)
            )
            conn.commit()
            
            # Se a inserção for bem-sucedida, você pode verificar a quantidade de linhas afetadas
            print(f"{cursor.rowcount} linha(s) inserida(s)")
        
        conn.close()
        return "Usuário cadastrado com sucesso!"

    except pymysql.MySQLError as e:
        print(f"Erro no MySQL: {e}")
        return f"Erro no MySQL: {e}"

    except Exception as e:
        print(f"Erro desconhecido: {e}")
        return f"Erro desconhecido: {e}"