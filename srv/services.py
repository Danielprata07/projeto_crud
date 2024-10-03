from conexao import *

def enviar_dados(nome, email, senha):
    criar_usuario(nome, email, senha)

def criar_usuario(nome, email, senha):
    if conn.is_connected():
        print('banco conectado')

        cursor = conn.cursor()
        
        sql= 'INSERT INTO usuario (nome, email, senha) values(%s, %s, %s)'
        values =(nome, email, senha)

        cursor.execute(sql, values)
        conn.commit()
        conn.close()
        cursor.close()



    else:
        print('banco nao conectado')

def  listar_usuario():
    if conn.is_connected():
        print('banco de dados conectado')
        cursor = conn.cursor()

        cursor.execute('select id, nome, email from usuario;')

        usuarios = cursor.fetchall()
        return usuarios 


    else:
        print('banco de dados nao conectado')