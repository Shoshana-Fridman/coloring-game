from connection import connection
import json


def get_poks_of_type(type_name):
    with connection.cursor() as cursor:
        get_poks = f"""SELECT name FROM Pokemons JOIN pokemon_types on pokemonId = id WHERE pokemonType = \"{type_name}\""""
        cursor.execute(get_poks)
        poks = cursor.fetchall()
        return poks