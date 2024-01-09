import requests
import json
from poke_api.pokemon_model import *
import sqlite3

def converter_detail_to_widget(pokemon_list):
    widget_pokemon = []
    for pokemon in pokemon_list:
        name = pokemon['name']
        photo = pokemon['sprites']['front_default']
        types = pokemon['types']
        id = pokemon['id']
        pokemon_details = PokemonWidget(name=name,
                                       photo=photo,
                                       types=types,
                                       id=id).__dict__
        
        widget_pokemon.append(pokemon_details)
    return widget_pokemon

def converter_detail_to_pokemon(poke_detail):
    pokemon = Pokemon(**poke_detail)

    return pokemon.__dict__

def get_pokemon_detail(link: str):
    response = requests.get(url=link)
    poke_detail = json.loads(response.content)
    pokemon = converter_detail_to_pokemon(poke_detail)

    return pokemon

def get_pokemons_detail(pokemons):
    pokemon_list = []
    for pokemon in pokemons:
        response = requests.get(url=pokemon['url'])
        poke_detail = json.loads(response.content)
        pokemon_list.append(converter_detail_to_pokemon(poke_detail))

    return pokemon_list

def get_pokemons():
    widgets_list = []
    with sqlite3.connect('banco_pokemon.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
                        select pd.id, pl.name, pp.front_default, pl.url
						from pokemon_list pl
                        join pokemon_details pd on pl.name = pd.name
                        join pokemon_photos pp on pp.id = pd.id
                        where pp.front_default <> 'None'
                        --LIMIT 9
                        ''')
        pokemons = cursor.fetchall()
        cursor.close()

        for pokemon in pokemons:
            widget = PokemonWidget(id=pokemon[0],
                                    name=pokemon[1],
                                    photo=pokemon[2],
                                    detail=pokemon[3]).__dict__
            widgets_list.append(widget)
            
    return widgets_list

if __name__ == '__main__':
    a = get_pokemons()
    b = get_pokemon_detail(a)
