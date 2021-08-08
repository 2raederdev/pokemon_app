# -*- coding: utf-8 -*-
import datetime
import json
import decimal
from uuid import UUID
from src.services.db import db

from sqlalchemy.ext.declarative import DeclarativeMeta


def _extended_encoder(x):
    if isinstance(x, datetime.date):
        return x.isoformat()
    if isinstance(x, UUID) or isinstance(x, bytes):
        return str(x)
    if isinstance(x, decimal.Decimal):
        return float(x)
    return x


class Jsonifyable(object):
    __RELATIONSHIPS_TO_DICT__ = False
    __not_include__ = []

    def __iter__(self):
        return self.to_dict().iteritems()

    def to_dict(self, rel=None, backref=None):

        if rel is None:
            rel = self.__RELATIONSHIPS_TO_DICT__
        res = {column.key: _extended_encoder(getattr(self, attr))
               for attr, column in self.__mapper__.c.items()
               if attr not in self.__not_include__}
        
        if rel:
            for attr, relation in self.__mapper__.relationships.items():
                # Avoid recursive loop between to tables.
                # if backref == relation.table:
                #     continue
                value = getattr(self, attr)
                if value is None and attr not in self.__not_include__:
                    res[relation.key] = None
                elif isinstance(value.__class__, DeclarativeMeta) and attr not in self.__not_include__:
                    res[relation.key] = value.to_dict(backref=self.__table__)
                elif attr not in self.__not_include__:
                    res[relation.key] = [i.to_dict(backref=self.__table__)
                                         for i in value]
        return res

    def to_json(self, rel=None):
        if rel is None:
            rel = self.__RELATIONSHIPS_TO_DICT__
        return json.dumps(self.to_dict(rel), default=_extended_encoder)

    @staticmethod
    def list_to_dict(lst, rel=None, backref=None):
        lst_dict = [el.to_dict(rel, backref) for el in lst]
        return lst_dict

    @staticmethod
    def list_to_json(lst, rel=None):
        lst_json = [el.to_json(rel) for el in lst]
        return lst_json


class BaseModel(Jsonifyable, db.Model):
    __abstract__ = True

    @staticmethod
    def insert(obj_instance):
        db.session.add(obj_instance)
        db.session.commit()
        return obj_instance

    @staticmethod
    def delete(obj_instance):
        db.session.delete(obj_instance)
        db.session.commit()

    @staticmethod
    def update(obj_instance, data):
        for k in data:
            setattr(obj_instance, k, data[k])
        db.session.commit()