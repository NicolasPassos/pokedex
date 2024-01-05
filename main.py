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

    # Criando popup
    popUp = ft.AlertDialog(on_dismiss='')

    def exibir_detalhes(link: str):
        pokemon_api = get_pokemon_detail(link)
        popUp.title = ft.Text(pokemon_api['name'].capitalize())
        info =  ft.Column(controls=[
                                    ft.Image(src=pokemon_api['sprites']['front_default']),
                                    ft.Text(value=f'Nº {pokemon_api["id"]}'),
                                    ft.Text(value=f'Base experience: {pokemon_api["base_experience"]}'),
                                    ft.Text(value=f'Height: {pokemon_api["height"]}'),
                                    ft.Text(value=f'Weight: {pokemon_api["weight"]}'),
                                    ft.Text(value=f'Is default? {pokemon_api["is_default"]}')
                                        ],
                                        horizontal_alignment='center')
        for i in pokemon_api['types']:
            info.controls.append(ft.Container(
                                                ft.Text(value=i['type']['name'].capitalize(), color=ft.colors.BLACK87),
                                                bgcolor=ft.colors.CYAN_800,
                                                padding=10,
                                                
                                                )
                                    )
        popUp.content = info
        popUp.open = True
        page.dialog = popUp
        page.update()

    pokemons = get_pokemons()
    for pokemon in pokemons:
        photo = pokemon['photo']
        id = f"Nº {pokemon['id']}"
        name = pokemon['name'].capitalize()
        detail = pokemon['detail']

        def create_on_click(detail_link):
            return lambda e: exibir_detalhes(detail_link)
    
        container = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Image(src=pokemon['photo']),
                    ft.Text(value=f"Nº {pokemon['id']}"),
                    ft.Text(value=pokemon['name'].capitalize()),
                    ft.Text(value=pokemon['detail'], visible=False)
                ],
                horizontal_alignment='center',
                spacing=2
            ),
            bgcolor=ft.colors.BLACK26,
            expand=True,
            border_radius=ft.border_radius.all(20),
            ink=True,
            on_click=create_on_click(detail)
        )
            
        grid.controls.append(container)

    page.update()

ft.app(target=main, view=ft.WEB_BROWSER, assets_dir='assets')
