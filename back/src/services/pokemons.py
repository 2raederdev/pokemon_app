# -*- coding: utf-8 -*-
import logging
import requests
from datetime import datetime

from sqlalchemy import text
from src.services.bases import BaseService
from src.models.pokemon import Pokemon

class PokemonRequest:
    id = None
    name = None
    caught = None
    types = None
    abilities = None
    hidden_abilities = None
    order_by = 'created_at'
    descending = False
    

class PokemonService(BaseService):

    @staticmethod
    def get_by_id(pokemon_id):
        pokemon = Pokemon.query.get(int(pokemon_id))
        return pokemon
    

    @classmethod
    def get_all_pokemons(cls, request: PokemonRequest = None):
        request = PokemonRequest() if not request else request

        q = f'''
            SELECT * 
            FROM pokemons AS p
            WHERE 1= 1
            {' AND p.name=:name' if request.name else ''}
            {' AND p.abilities::jsonb ? :ability' if request.abilities else ''}
            {' AND p.caught=:caught' if isinstance(request.caught, bool) else ''}
            {' AND p.types ILIKE :types' if request.types else ''}
            order by {request.order_by} {'desc' if request.descending else 'asc'}
        '''

        result = cls.db.engine.execute(
            text(q), 
            name = request.name,
            types = f"%{request.types}%",
            caught = request.caught,
            ability= request.abilities
            )

        pokemons = list()
        for row in result:
            pokemons.append(dict(row))

        return pokemons

    @classmethod
    def get_pokemon(cls, name):
        found = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
        if not found:
            logging.info(f'The pokemon {name} doesn\'t exit')
            return dict()

        pokemon = found.json()

        payload = dict()
        
        payload['name'] = pokemon['name']
        payload['api_id'] = pokemon['id']
        payload['image_url'] = pokemon['sprites']['other']['official-artwork']['front_default']
        payload['weight'] = pokemon['weight']
        payload['abilities'] = [ability['ability']['name'] for ability in pokemon['abilities']]
        payload['hidden_abilities'] = True in [ability['is_hidden'] for ability in pokemon['abilities']]
        payload['types'] = ','.join([t['type']['name'] for t in pokemon['types']]) # Para mantener consistencia, este campo debería ser del mismo tipo que 'abilities, pero lo hago distinto para después mostrar dos formas distintas de filtrar.
        payload['height'] = pokemon ['height']
        payload['caught'] = False


        request = PokemonRequest()
        request.name = name

        existing_pokemon = cls.get_all_pokemons(request)
        if not existing_pokemon or len(existing_pokemon) is 0:
            new_pokemon = cls.insert_pokemon(payload)

        return new_pokemon 

    
    @classmethod
    def insert_pokemon(cls, payload):
        to_save = Pokemon(**payload)
        Pokemon.insert(to_save)

        return to_save.to_dict()

    
    @classmethod
    def update_pokemon(cls, pokemon_id, payload):
        pokemon = Pokemon.query.get(int(pokemon_id))

        payload['updated_at'] = datetime.now()

        Pokemon.update(pokemon, payload)

        return pokemon


    