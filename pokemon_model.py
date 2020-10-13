from connection import connection
import json

def get_trainers_of_pokemon(pok_name):
    # try:
    with connection.cursor() as cursor:
        get_trainers = f'SELECT trainerName FROM pokemon_ownership JOIN pokemons on pokemonId = id WHERE pokemons.name = \"{pok_name}\"'
        cursor.execute(get_trainers)
        trainer = cursor.fetchall()
        return trainer
    # except:
       # return "Error: failed getting trainers of pokemon"

def get_id(poke_name):
    with connection.cursor() as cursor:
        get = f'SELECT id FROM pokemons WHERE name = \"{poke_name}\"'
        cursor.execute(get)
        id = cursor.fetchone()
        return id["id"]

print(get_trainers_of_pokemon("bulbasaur"))