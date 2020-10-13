import requests
from flask import Flask, Response, request
import json
import pymysql
import manipulate_tables
import pokemon_model
import trainer_model
import type_model
from pymysql import IntegrityError


app = Flask(__name__)


@app.route('/')
def root():
    return "Welcome to Pokemon API"


@app.route('/trainers/<trainer_name>')
def get_pok_by_trainer(trainer_name):
    try:
        poks = trainer_model.get_pok_by_trainer(trainer_name)
        return json.dumps(poks)

    except Exception as e:
        return json.dumps({"Error": str(e)}), 500


@app.route('/pokemons/<pok_name>')
def get_trainer_of_pok(pok_name):
    try:
        trainers = pokemon_model.get_trainers_of_pokemon(pok_name)
        return json.dumps(trainers)

    except Exception as e:
        return json.dumps({"Error": str(e)}), 500


@app.route('/types/<type_name>')
def get_pok_by_type(type_name):
    try:
        poks = type_model.get_poks_of_type(type_name)
        return json.dumps(poks)

    except Exception as e:
        return json.dumps({"Error": str(e)}), 500


@app.route('/<trainer>/<pok>', methods = ["DELETE"])
def delete_pok(trainer, pok):
    try:
        manipulate_tables.delete_ownership(trainer, pok)
        return json.dumps({"Deleted":f'{trainer} - {pok}'}), 200

    except Exception as e:
        return json.dumps({"Error": str(e)}), 500


@app.route('/pokemons', methods = ["POST"])
def add():
    try:
        pokemon = request.get_json()
        manipulate_tables.insert_pokemon(pokemon)
        return json.dumps({"Added": f'{pokemon}'}), 201

    except IntegrityError as e:
        return json.dumps({"Error": str(e)}), 409

    except Exception as e:
        return json.dumps({"Error": str(e)}), 500


@app.route('/types/<poke_name>', methods = ["PUT"])
def update(poke_name):
    try:
        id = pokemon_model.get_id(poke_name)
        type_url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(poke_name)
        res = requests.get(url=type_url, verify = False).json()
        types = res.get("types")

        for t in types:
            manipulate_tables.insert_pokemon_types_table(id, t["type"]["name"])
        return json.dumps({"updated": [t["type"]["name"] for t in types]})

    except Exception as e:
        return json.dumps({"Error": str(e)}), 500
    

if __name__ == '__main__':
    app.run(port=3000)