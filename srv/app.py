from tkinter import *
from tkinter import ttk 
import services

def main():
    def on_enviar():
        nome = nomeEntry.get()
        email= emailEntry.get()
        senha= senhaEntry.get()
        services.enviar_dados(nome, email, senha)

        #limpar campos 
        nomeEntry.delete(0, END)
        emailEntry.delete(0, END)
        senhaEntry.delete(0, END)   

    def deletar_user(email):
        email = emailEntry.get()
        services.remover_usuario(email)    

    def listar_usuario():
        usuarios = services.listar_usuario()

        #criar janela que vai mostrar a lista de usuario
        janela_listar = Toplevel(janela)
        janela_listar.title('Lista de Usuarios')
        janela_listar.geometry('600x300')

        #criar uma Treeview (view, visualizaçao) da lista de usuarios, show = limpa o cabeçalho
        tree = ttk.Treeview(janela_listar, columns=('ID', 'Nome','Email'), show='headings')
        tree.heading('ID', text='ID')
        tree.heading('Nome', text='Nome')
        tree.heading('Email', text='Email')

        #criar botao de voltar e fechar tela de lista de usuario
        voltar = Button(janela_listar, text='Voltar', width= 10, command=janela_listar.destroy)
        voltar.pack(fill=BOTH, expand=True, side=BOTTOM)

        tree.pack(fill=BOTH, expand=True)

        #inseir dados de usuarios na noosa Treeview
        for usuario in usuarios:
            #END vai inserir o item no final da tabela
            tree.insert('',END,values=usuario)

    janela = Tk()
    janela.geometry('400x300')
    janela.title('Sistema de Gerenciamento de Usuario')

    titulo = Label(janela, text= 'CRUD_BAHIA', font=('Arial black', 20))
    titulo.pack(pady= 20)

    #nome
    nome = Label(janela, text=('Nome:'))
    nome.place(x=50 ,y=100)
    #entrada de nome
    global nomeEntry
    nomeEntry = Entry(janela, width=30)
    nomeEntry.place(x=100, y=100)

    #email
    email = Label(janela, text='Email:')
    email.place(x=50, y=130)
    #entrada email
    global emailEntry
    emailEntry = Entry(janela, width=30)
    emailEntry.place(x=100,y=130)

    #senha
    senha = Label(janela, text='Senha:')
    senha.place(x=50, y=160)
    #entrada senha , show esconde senha
    global senhaEntry
    senhaEntry = Entry(janela, width=30, show='*')
    senhaEntry.place(x=100, y=160)

    cadastrar = Button(janela, text='Cadastrar', width=10, command=on_enviar)
    cadastrar.place(x=50, y=200)

    listar = Button(janela, text='Listar Usuario', width=15, command=listar_usuario)
    listar.place(x=140, y= 200)

    remover = Button(janela, text='Remover', width= 10, command=lambda: deletar_user(email))
    remover.place(x=270,y=200)

    janela.mainloop()

if __name__ == '__main__':
    main()