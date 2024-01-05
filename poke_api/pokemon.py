import requests
import json
from poke_api.pokemon_model import *

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

def get_pokemon_detail(pokemons):
    pokemon_list = []
    for pokemon in pokemons:
        response = requests.get(url=pokemon['url'])
        poke_detail = json.loads(response.content)
        pokemon_list.append(converter_detail_to_pokemon(poke_detail))

    return pokemon_list


def get_pokemons():
    url_get_pokemons = 'https://pokeapi.co/api/v2/pokemon?offset=0&limit=50'
    response = requests.get(url=url_get_pokemons)
    
    pokemon = json.loads(response.content)['results']

    return pokemon