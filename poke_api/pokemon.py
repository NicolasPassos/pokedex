import requests
import json
from pokemon_model import Pokemon

def converter_poke_api_detail_to_pokemon(poke_detail):
    pokemon = Pokemon
    pokemon.poke_id = poke_detail['id']
    pokemon.poke_name = poke_detail['name']
    pokemon.poke_types = poke_detail['types']

    return pokemon

def get_pokemon_detail(pokemons):
    for pokemon in pokemons:
        response = requests.get(url=pokemon['url'])
        poke_detail = json.loads(response.content)

        converter_poke_api_detail_to_pokemon(poke_detail)



def get_pokemons():
    url_get_pokemons = 'https://pokeapi.co/api/v2/pokemon?offset=0&limit=200'
    response = requests.get(url=url_get_pokemons)
    
    pokemon = json.loads(response.content)['results']

    return pokemon


a = get_pokemons()
get_pokemon_detail(a)
print(a)