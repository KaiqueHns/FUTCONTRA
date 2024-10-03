import mysql.connector
from mysql.connector import Error

def conectar_mysql():
    try:
        # Conectar ao banco de dados MySQL
        conn = mysql.connector.connect(
            host='localhost',       # Endereço do servidor
            user='seu_usuario',     # Seu nome de usuário
            password='sua_senha',   # Sua senha
            database='nome_do_banco'  # Nome do banco de dados
        )

        if conn.is_connected():
            print("Conectado ao MySQL!")

            # Criar um cursor
            cursor = conn.cursor()

            # Inserir dados
            cursor.execute('''
            INSERT INTO usuarios (nome, idade) VALUES (%s, %s)
            ''', ('Alice', 30))

            # Salvar (commit) as mudanças
            conn.commit()
            print("Dados inseridos com sucesso!")

            # Consultar dados
            cursor.execute('SELECT * FROM usuarios')
            rows = cursor.fetchall()

            print("Resultados da consulta:")
            for row in rows:
                print(row)

    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
    finally:
        if (conn.is_connected()):
            cursor.close()
            conn.close()
            print("Conexão com MySQL encerrada.")

if __name__ == "__main__":
    conectar_mysql()