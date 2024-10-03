import mysql 
import mysql.connector

conn = mysql.connector.connect(
    username = 'prata',
    host = 'localhost',
    password = 'projeto020907',
    db = 'projeto_crud'
)


'''
if conn.is_connected():
    print('conectado com o banco')
else:
    print('nao conectado com o banco')'''