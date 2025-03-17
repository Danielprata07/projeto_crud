from services.tarefa_service import cadastrar_tarefa, excluir_tarefa, editar_tarefa
import flet as ft
from sqlalchemy.orm import sessionmaker
from connection import Session
from model.tarefa_model import Tarefa  # Ajuste de import, caso o seu modelo esteja em models.py

# Função para atualizar a lista de tarefas
def atualizar_lista_tarefas(tarefas_column):
    # Criação de uma nova sessão para pegar as tarefas
    session = Session()
    
    try:
        # Limpa a coluna de tarefas
        tarefas_column.controls.clear()

        # Busca todas as tarefas no banco de dados
        todas_tarefas = session.query(Tarefa).all()

        # Adiciona cada tarefa à coluna de tarefas
        for tarefa in todas_tarefas:
            tarefas_column.controls.append(
                ft.Row(
                    [
                        ft.Text(f"ID: {tarefa.id} - Descrição: {tarefa.descricao} - Concluída: {'Sim' if tarefa.situacao else 'Não'}")
                    ]
                )
            )

        # Atualiza a tela com as novas tarefas
        tarefas_column.update()

    finally:
        # Fechar a sessão após o processo
        session.close()


def on_add_tarefa_click(e, descricao_input, situacao_input, result_text, tarefas_column):
    descricao = descricao_input.value
    situacao = situacao_input.value
    
    # Chama a função de cadastro da tarefa
    tarefa_cadastrada = cadastrar_tarefa(descricao, situacao)
    
    if tarefa_cadastrada:
        result_text.value = f"Tarefa cadastrada com sucesso! ID: {tarefa_cadastrada.id}"
        # Atualiza a lista de tarefas na tela
        atualizar_lista_tarefas(tarefas_column)
    else:
        result_text.value = "Erro ao cadastrar a tarefa."
    
    # Atualiza o texto na tela
    result_text.update()

def on_excluir_tarefa_click(e, tarefa_id, tarefas_column):
    excluir_tarefa(tarefa_id)
    atualizar_lista_tarefas(tarefas_column)



def modal_editar(page, tarefa, tarefa_column):
    descricao_input = ft.TextField(label="Nova descriçao", value=tarefa.descricao)
    situacao_input = ft.Checkbox(label="Tarefa concluída", value=tarefa.situacao)


    def salvar_edicao(e):
        editar_tarefa(tarefa.id, descricao_input, situacao_input)
        page.dialog.close()
        page.update()
        atualizar_lista_tarefas(tarefa_column)


    modal = ft.AlertDialog(
        title=ft.Text("Editar Tarefa"),
        content=ft.Column([descricao_input, situacao_input]),
        actions=[ft.TextButton("Salvar", on_click=salvar_edicao),
                 ft.TextButton("Cancelar", on_click=lambda e: page.dialog.close())]
    )

    page.dialog = modal
    modal.open = True 
    page.update()

class Task(ft.Row):
    def __init__(self, text):
        super().__init__()
        self.text_view = ft.Text(text)
        self.text_edit = ft.TextField(text, visible=False)
        self.edit_button = self.create_edit_button()
        self.save_button = self.create_save_button()
        self.checkbox = ft.Checkbox()

        self.controls = [
            self.checkbox,
            self.text_view,
            self.text_edit,
            self.edit_button,
            self.save_button,
        ]

    def create_edit_button(self):
        return ft.IconButton(icon=ft.Icons.EDIT, on_click=self.edit)

    def create_save_button(self):
        return ft.IconButton(
            visible=False, icon=ft.Icons.SAVE, on_click=self.save
        )

    def edit(self, e):
        self.toggle_visibility(editing=True)

    def save(self, e):
        self.text_view.value = self.text_edit.value
        self.toggle_visibility(editing=False)

    def toggle_visibility(self, editing: bool):
        """Helper function to toggle visibility of components."""
        self.edit_button.visible = not editing
        self.save_button.visible = editing
        self.text_view.visible = not editing
        self.text_edit.visible = editing
        self.update()


def main(page: ft.Page):
    tasks = [
        Task(text="Do laundry"),
        Task(text="Cook dinner"),
    ]
    page.add(*tasks)


ft.app(main)

