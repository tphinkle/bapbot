## Imports

# Python standard library
import datetime
import json
import os
import time

# Flask
from flask import Flask, request

# Project
from .bap import Bap
from . import database as db
from . import handlers


## Globals
GET = 'GET'
POST = 'POST'


## Functions
def create_app(test_config=None):

    # Set up handlers
    bap_handler = handlers.BapHandler()


    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)



    @app.route('/bap', methods=(GET, POST))
    def bap():
        if request.method == POST:
            bap_handlers.handle_bap_post(request.args)
        return 'ok'


    return app
