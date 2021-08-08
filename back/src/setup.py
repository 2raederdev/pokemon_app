# -*- coding: utf-8 -*-

import os
import logging
import importlib

import flask


def register_blueprints(app: flask.Flask):
    try:
        for root, dirs, files in os.walk("./src/blueprints"):
            for filename in files:
                if not filename.startswith('__') and filename.endswith('.py'):
                    bp_name = filename.replace('.py', '')
                    bp = importlib.import_module(f'src.blueprints.{bp_name}')
                    app.register_blueprint(getattr(bp, f'{bp_name}_bp'))
    except Exception as e:
        logging.error(e)
