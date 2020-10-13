import pymysql
import json
from connection import connection


def insert_pokemon_types_table(p_id, p_type):
    with connection.cursor() as cursor:
        try:
            pokemon_query = f"""INSERT INTO pokemon_types VALUES({p_id}, \"{p_type}\")"""
            cursor.execute(pokemon_query)
            connection.commit()
        except:
            pass


def insert_pokemon_table(id, name, types, height, weight):
    with connection.cursor() as cursor:
        pokemon_query = f"""INSERT INTO pokemons VALUES({id}, \"{name}\", {height}, {weight})"""
        cursor.execute(pokemon_query)
        connection.commit()
    for t in types.split():
        insert_pokemon_types_table(id, t)


def insert_trainer_table(name, town):
    with connection.cursor() as cursor:
        trainer_query = f"""INSERT INTO trainers VALUES(\"{name}\", \"{town}\")"""
        cursor.execute(trainer_query)
        connection.commit()


def insert_pokemon_ownership_table(p_id, t_name):
    with connection.cursor() as cursor:
        relation_query = f"""INSERT INTO pokemon_ownership VALUES({p_id}, \"{t_name}\")"""
        cursor.execute(relation_query)
        connection.commit()


def insert_pokemon(pokemon):
    insert_pokemon_table(pokemon["id"], pokemon["name"], pokemon["type"], pokemon["height"], pokemon["weight"])
    for trainer in pokemon["ownedBy"]:
        try:
            insert_trainer_table(trainer["name"], trainer["town"])
        except:
            pass
        insert_pokemon_ownership_table(pokemon["id"], trainer["name"])


def init_DB():
    with open("pokemons.json") as my_file:
        pokemon_data = json.load(my_file) 
        for pok in pokemon_data:
            insert_pokemon(pok)


def delete_ownership(trainer, pok):
    with connection.cursor() as cursor:
        delete = f"""DELETE from pokemon_ownership
            where trainerName = \'{trainer}\' and pokemonId = (SELECT id from pokemon where name = \'{pok}\')"""
        cursor.execute(delete)
        connection.commit()

# init_DB()