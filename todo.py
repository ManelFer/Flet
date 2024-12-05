import flet as ft

def main(page: ft.Page):
    page.title = "Meu Projeto Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Adicionando um texto
    page.add(ft.Text("Olá, Flet!"))

    # Adicionando um botão
    def button_click(e):
        page.add(ft.Text("Você clicou no botão!"))

    page.add(ft.ElevatedButton("Clique aqui", on_click=button_click))

# Executa o aplicativo
ft.app(target=main)