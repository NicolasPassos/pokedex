import flet as ft
from poke_api.pokemon import *

# Padronização do tamanho dos campos
_with_input = 250
_size_text = 20
_with_button = 250
_height_button = 50

def main(page: ft.Page):
    # Definindo orientação da página
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 50

    # Criando a logo
    logo_pokemon = ft.Image(src='/images/Pokemon-Logo.png',
                            width=1000,
                            height=300)

    # Criando grid
    grid = ft.GridView(
        expand=1,
        runs_count=5,
        max_extent=180,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )

    # Inserindo os itens na pagina
    #page.add(logo_pokemon)
    page.add(grid)

    pokemons = get_pokemons()
    details = get_pokemon_detail(pokemons)
    widgets = converter_detail_to_widget(details)
    for widget in widgets:
        container = ft.Container(
            content=ft.Column(
                            controls=[
                                        ft.Image(src=widget['photo']),
                                        ft.Text(value=f"Nº {widget['id']}"),
                                        ft.Text(widget['name'].capitalize())
                                        
                                        ],
                                        horizontal_alignment='center',
                                        spacing=2
                                )
                            ,bgcolor=ft.colors.BLACK26,
                            expand=True,
                            border_radius=ft.border_radius.all(20),
                            ink=True,
                            on_click=lambda e: None
                            )
        
        grid.controls.append(container)


    page.update()

ft.app(target=main, view=ft.WEB_BROWSER, assets_dir='assets')
