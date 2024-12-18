import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"

    tarefas = []

    def adicionar_tarefa(e):
        if campo_tarefa.value:
            tarefas.append(campo_tarefa.value)
            atualizar_lista()
            campo_tarefa.value = ""
            page.update()

    def atualizar_lista():
        lista_tarefas.controls.clear()
        for tarefa in tarefas:
            lista_tarefas.controls.append(ft.Text(tarefa))

    campo_tarefa = ft.TextField(
        hint_text="Digite o nome da tarefa",
        width=300,
    )

    botao_adicionar = ft.ElevatedButton(
        text="Adicionar Tarefa",
        on_click=adicionar_tarefa,
    )

    lista_tarefas = ft.Column()

    page.add(
        ft.Row([campo_tarefa, botao_adicionar]),
        lista_tarefas,
    )

ft.app(target=main)