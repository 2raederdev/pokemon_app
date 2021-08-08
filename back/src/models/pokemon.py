# -*- coding: utf-8 -*-
import datetime

from src.services.db import db
from src.models.bases import BaseModel
from sqlalchemy.dialects.postgresql import JSON


class Pokemon(BaseModel):
    __tablename__ = 'pokemons'
     # poner aqui columnas que no queremos que se devuelvan en una respuesta
    __not_include__ = []
    __UPDATABLE_BY_USER__ = ['caught']

    id = db.Column(db.Integer, db.Sequence('pokemons_id_seq'), primary_key=True)
    name = db.Column(db.String)
    api_id = db.Column(db.Integer)
    image_url = db.Column(db.String)
    weight = db.Column(db.Integer)
    abilities = db.Column(JSON)
    hidden_abilities = db.Column(db.Boolean, default=False)
    types = db.Column(db.String)
    height = db.Column(db.Integer)
    caught = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now)