# -*- coding: utf-8 -*-
from http import HTTPStatus

import flask

from src.exceptions.response_exceptions import ConflictException, NotFoundException, BadRequestException
from src.services.pokemons import PokemonService, PokemonRequest


pokemons_bp = flask.Blueprint('pokemons', __name__, url_prefix='/api/v1/pokemons')

@pokemons_bp.route('/<name>', methods=['GET'])
def get_pokemon(name):
    pokemon = PokemonService.get_pokemon(name)

    return flask.jsonify(pokemon), HTTPStatus.OK.value


@pokemons_bp.route('', methods=['GET'])
def get_all_pokemons():
    request = PokemonRequest()

    if 'name' in flask.request.args:
        request.name = flask.request.args.get('name')    
    if 'types' in flask.request.args:
        request.types = flask.request.args.get('types')    
    if 'caught' in flask.request.args:
        request.caught = flask.request.args.get('caught') == 'true'
    if 'abilities' in flask.request.args:
        request.abilities = flask.request.args.get('abilities')  
    if 'hidden_abilities' in flask.request.args:
        request.hidden_abilities = flask.request.args.get('hidden_abilities') == 'true'
    if 'order_by' in flask.request.args:
        request.order_by = flask.request.args.get('order_by')
    if 'descending' in flask.request.args:
        request.descending = flask.request.args.get('descending')

    pokemons = PokemonService.get_all_pokemons(request)

    return flask.jsonify(pokemons), HTTPStatus.OK.value


@pokemons_bp.route('/<pokemon>', methods=['POST'])
def save_pokemon(name):
    pokemon = PokemonService.get_all_pokemons({ name })
    if pokemon:
        raise ConflictException('This pokemon has been already saved')

    payload = flask.request.get_json(cache=False)

    saved = PokemonService.insert_pokemon(payload)

    return flask.jsonify(saved), HTTPStatus.OK.value


@pokemons_bp.route('/<int:pokemon_id>', methods=['PUT', 'PATCH'])
def update_pokemon(pokemon_id):

    pokemon = PokemonService.get_by_id(pokemon_id)
    if not pokemon:
        raise NotFoundException('This pokemon doesn\'t belong to your team yeat')

    payload = flask.request.get_json()
    if not payload:
        raise BadRequestException()

    saved = PokemonService.update_pokemon(pokemon_id, payload)

    return flask.jsonify(saved.to_dict()), HTTPStatus.OK.value
