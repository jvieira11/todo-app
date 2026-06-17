import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def get_connect():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

# Backwards-compatible alias: some code expects get_connection()
def get_connection():
    return get_connect()

def listar_tarefas():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, titulo, descricao, concluida, criada_em
        FROM tarefas
        ORDER BY concluida ASC, criada_em DESC
    """)
    tarefas = cursor.fetchall()
    cursor.close()
    conn.close()
    return tarefas

def criar_tarefa(titulo, descricao):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tarefas (titulo, descricao)
        VALUES (%s, %s)
    """, (titulo, descricao))
    conn.commit()
    cursor.close()
    conn.close()

def atualizar_tarefa(id: int, titulo: str, descricao: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE tarefas
        SET titulo = %s, descricao = %s
        WHERE id = %s
    """, (titulo, descricao, id))
    conn.commit()
    cursor.close()
    conn.close()

def concluir_tarefa(id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE tarefas SET concluida = NOT concluida
        WHERE id = %s
    """, (id,))
    conn.commit()
    cursor.close()
    conn.close()

def deletar_tarefa(id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()

def buscar_tarefa(id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, titulo, descricao FROM tarefas WHERE id = %s
    """, (id,))
    tarefa = cursor.fetchone()
    cursor.close()
    conn.close()
    return tarefa
