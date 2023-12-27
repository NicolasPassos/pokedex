import requests
import json
from pokemon_model import Pokemon

def converter_detail_to_pokemon(poke_detail):
    pokemon = Pokemon(**poke_detail)

    return pokemon

def get_pokemon_detail(pokemons):
    pokemon_list = []
    for pokemon in pokemons:
        response = requests.get(url=pokemon['url'])
        poke_detail = json.loads(response.content)
        pokemon_list.append(converter_detail_to_pokemon(poke_detail))

    return pokemon_list


def get_pokemons():
    url_get_pokemons = 'https://pokeapi.co/api/v2/pokemon?offset=0&limit=200'
    response = requests.get(url=url_get_pokemons)
    
    pokemon = json.loads(response.content)['results']

    return pokemon


a = get_pokemons()
get_pokemon_detail(a)
print(a)