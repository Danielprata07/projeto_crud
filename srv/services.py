from conexao import *

def enviar_dados(nome, email, senha):
    criar_usuario(nome, email, senha)

def criar_usuario(nome, email, senha):
    if conn.is_connected():
        print('Banco conectado')

        cursor = conn.cursor()
        
        sql= 'INSERT INTO usuario (nome, email, senha) values(%s, %s, %s)'
        values =(nome, email, senha)

        cursor.execute(sql, values)
        conn.commit()
        conn.close()
        cursor.close()

    else:
        print('Banco nao conectado')

def  listar_usuario():
    if conn.is_connected():
        print('banco de dados conectado')
        cursor = conn.cursor()

        cursor.execute('select id, nome, email from usuario;')

        usuarios = cursor.fetchall()
        cursor.close()
        conn.close()
        return usuarios 
        
    else:
        print('Banco de dados nao conectado')

def remover_usuario(email):
    if conn.is_connected():
        print('Banco conectado')

        cursor = conn.cursor()

        sql_select = 'select id, nome, email from usuario where email=%s;'
        cursor.execute(sql_select,(email,))


        usuario = cursor.fetchone()
        if usuario:
            print('usuario encontrado! ')
            sql_delect = 'delete from usuario where email=%s'
            cursor.execute(sql_delect, (email,))
            print('Usuario deletado!')
            conn.commit()
            cursor.close()
            conn.close()
    else:
        print('Usuario nao encontrado!')

