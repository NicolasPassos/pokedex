import requests
import json
from pokemon_model import *
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

def get_pokemon_detail(pokemons):
    pokemon_list = []
    for pokemon in pokemons:
        response = requests.get(url=pokemon['url'])
        poke_detail = json.loads(response.content)
        pokemon_list.append(converter_detail_to_pokemon(poke_detail))

    return pokemon_list

def cadastrar_pokemon_photos(pokemon_details):
    with sqlite3.connect('banco_pokemon.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f'''
                       INSERT INTO POKEMON_PHOTOS
                       (id,back_default,back_female,back_shiny,back_shiny_female,front_default,front_female,front_shiny,front_shiny_female) 
                       values ("{pokemon_details["id"]}","{pokemon_details["sprites"]["back_default"]}","{pokemon_details["sprites"]["back_female"]}","{pokemon_details["sprites"]["back_shiny"]}",
                       "{pokemon_details["sprites"]["back_shiny_female"]}","{pokemon_details["sprites"]["front_default"]}","{pokemon_details["sprites"]["front_female"]}",
                       "{pokemon_details["sprites"]["front_shiny"]}","{pokemon_details["sprites"]["front_shiny_female"]}")''')
        cursor.close()
        conn.commit()

def cadastrar_pokemon_details(pokemon_details):
    with sqlite3.connect('banco_pokemon.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f'''
                       INSERT INTO POKEMON_DETAILS
                       (id,name,weight,height,is_default,base_experience) 
                       values ("{pokemon_details["id"]}","{pokemon_details["name"]}","{pokemon_details["weight"]}","{pokemon_details["height"]}",
                       "{pokemon_details["is_default"]}","{pokemon_details["base_experience"]}")''')
        cursor.close()
        conn.commit()

def consultar_pokemon(pokemon):
    with sqlite3.connect('banco_pokemon.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM POKEMON_LIST WHERE NAME = "{pokemon}"')
        pokemon = cursor.fetchall()
        if len(pokemon) <= 0:
            pokemon = None
        else:
            pokemon = pokemon[0]

        cursor.close()
    return pokemon

def cadastrar_pokemons(pokemons):
    with sqlite3.connect('banco_pokemon.db') as conn:
        cursor = conn.cursor()
        for pokemon in pokemons:
            consulta = consultar_pokemon(pokemon=pokemon['name'])
            if consulta == None:
                cursor.execute(f'INSERT INTO POKEMON_LIST (name,url) values ("{pokemon["name"]}","{pokemon["url"]}")')
        cursor.close()
        conn.commit()


def get_pokemons():
    url_get_pokemons = 'https://pokeapi.co/api/v2/pokemon?offset=0&limit=2000'
    response = requests.get(url=url_get_pokemons)
    
    pokemons = json.loads(response.content)['results']

    return pokemons

if __name__ == '__main__':
    a = get_pokemons()
    b = get_pokemon_detail(a)
