from flask import Flask, jsonify

import src
import os
from flask_cors import CORS

from config import Config
from src.services.db import init_db
from src.setup import register_blueprints
from src.exceptions.response_exceptions import ResponseBaseException


app = Flask(src.__name__)
CORS(app)
cors = CORS(app, resources = {
    r'/*': {
        'origins': '*'
    }
})


app.config.from_object(Config())

init_db(app)
register_blueprints(app)

