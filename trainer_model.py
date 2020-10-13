from connection import connection
import json


def get_pok_by_trainer(trainer_name):
    with connection.cursor() as cursor:
        get_pok = f'SELECT name FROM Pokemons JOIN pokemon_ownership on pokemonId = id WHERE trainerName = \"{trainer_name}\"'
        cursor.execute(get_pok)
        poks = cursor.fetchall()
        return poks