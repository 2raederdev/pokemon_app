# -*- coding: utf-8 -*-
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    db.init_app(app)

def get_db():
    return db