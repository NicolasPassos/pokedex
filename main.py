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
    popUp = ft.AlertDialog(on_dismiss='',)

    def exibir_detalhes(link: str):
        pokemon_api = get_pokemon_detail(link)
        popUp.title = ft.Text(pokemon_api['name'].capitalize())
        types = ft.Row(alignment='center')
        info =  ft.Container(
                            content=ft.ListView(controls=[
                                                            ft.Container(ft.Image(src=pokemon_api['sprites']['front_default']),bgcolor=ft.colors.BLACK26, border_radius=10,),
                                                            ft.Text(value=f'Nº {pokemon_api["id"]}'),
                                                            ft.Text(value=f'Base experience: {pokemon_api["base_experience"]}'),
                                                            ft.Text(value=f'Height: {pokemon_api["height"]}'),
                                                            ft.Text(value=f'Weight: {pokemon_api["weight"]}'),
                                                            ft.Text(value=f'Is default? {pokemon_api["is_default"]}'),
                                                            types
                                                                ],
                                                    #height=300,
                                                    expand=1,
                                                    spacing=5,
                                                    padding=10,
                                                                                         
                                                    )
                                    )
        for i in pokemon_api['types']:
            poke_type = i['type']['name']
            if poke_type == 'fire':
                color = ft.colors.RED_500
            elif poke_type == 'grass':
                color = ft.colors.GREEN_500
            elif poke_type == 'poison':
                color = ft.colors.PURPLE_500
            elif poke_type == 'water':
                color = ft.colors.LIGHT_BLUE_500
            elif poke_type == 'bug':
                color = ft.colors.LIGHT_GREEN_500
            elif poke_type == 'flying':
                color = ft.colors.PURPLE_ACCENT_100
            elif poke_type == 'electric':
                color = ft.colors.YELLOW_500
            elif poke_type == 'ground':
                color = ft.colors.BROWN_500
            elif poke_type == 'fairy':
                color = ft.colors.PINK_500
            elif poke_type == 'normal':
                color = ft.colors.BROWN_200
            elif poke_type == 'fighting':
                color = ft.colors.AMBER_500
            elif poke_type == 'psychic':
                color = ft.colors.PINK_ACCENT_500
            elif poke_type == 'steel':
                color = ft.colors.GREY_500
            elif poke_type == 'ghost':
                color = ft.colors.DEEP_PURPLE_500
            elif poke_type == 'dragon':
                color = ft.colors.PURPLE_ACCENT_500
            elif poke_type == 'ice':
                color = ft.colors.LIGHT_BLUE_100
            elif poke_type == 'dark':
                color = ft.colors.BLACK12
            elif poke_type == 'rock':
                color = ft.colors.BROWN100
            else:
                color = ft.colors.WHITE

            types.controls.append(ft.Container(
                                                ft.Text(value=poke_type.capitalize(), color=ft.colors.WHITE),
                                                bgcolor=color,
                                                padding=6,
                                                border_radius=10

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

ft.app(target=main, view=ft.AppView.WEB_BROWSER, assets_dir='assets',host='127.0.0.1',port=8000)
