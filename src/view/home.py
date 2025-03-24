import flet as ft
from connection import Session
from view.tarefa_view import on_add_tarefa_click, atualizar_lista_tarefas, on_excluir_tarefa_click, modal_editar, tarefa_id, cadastrar_tarefa     
from model.tarefa_model import Tarefa 

def main(page: ft.Page):
    page.title = "Cadastro de Tarefa"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Campo de entrada para a descrição da tarefa
    descricao_input = ft.TextField(label="Descrição da Tarefa", autofocus=True, width=300)
    
    # Campo de entrada para a situação (Checkbox)
    situacao_input = ft.Checkbox(label="Tarefa concluída", value=False)
    
    # Botão para adicionar a tarefa
    add_button = ft.ElevatedButton("Cadastrar Tarefa", on_click=lambda e: on_add_tarefa_click(e, descricao_input, situacao_input, result_text, tarefas_column))
    
    # Área de resultado (onde será mostrado se a tarefa foi cadastrada ou não)
    result_text = ft.Text()

    # Coluna para exibir a lista de tarefas
    tarefas_column = ft.Column()

    # Adiciona todos os componentes na página
    page.add(descricao_input, situacao_input, add_button, result_text, tarefas_column,excluir_button)

    # Inicializa a lista de tarefas
    atualizar_lista_tarefas(tarefas_column)

    # Botão para excluir a tarefa
    excluir_button = ft.ElevatedButton(label="Excluir Tarefa", on_click=lambda e: on_excluir_tarefa_click(e, tarefa_id, tarefas_column))

# Inicia o aplicativo Flet
   
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

def carregar_tarefas(page, tarefas_column):
    session = Session()
    try:
        tarefas_column.controls.clear()
        todas_tarefas = session.query(Tarefa).all()  # Corrigido para usar Tarefa
        
        for tarefa in todas_tarefas:
            tarefas_column.controls.append(
                ft.Row(
                    [
                        ft.Text(f"ID: {tarefa.id} - {tarefa.descricao} - {'Concluída' if tarefa.situacao else 'Pendente'}"),
                        ft.IconButton(icon=ft.icons.EDIT, on_click=lambda e, t=tarefa: modal_editar(page, t, tarefas_column)),
                        ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e, id=tarefa.id: on_excluir_tarefa_click(e, id, tarefas_column))
                    ]
                )
            )

        page.update()
    finally:
        session.close()

page(add.update())