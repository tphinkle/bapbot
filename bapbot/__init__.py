## Imports

# Python standard library
import datetime
import json
import os
import time

# Flask
from flask import Flask, request

# Project
from . import constants
from . import database as db


def _get_time():
    """
    """
    return time.time()

def _get_timestamp():
    """
    """
    return datetime.datetime.now()

def create_app(test_config=None):
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

    @app.route('/bap', methods=('GET', 'POST'))
    def bap():
        if request.method == 'POST':

            # Get bapper
            bapper = request.args.get(constants.bapper_key, DEFAULT_BAPPER)
            bapped = request.args.get(constants.bappee_key, DEFAULT_BAPPEE)
            bap_type = request.args.get(constants.bap_type_key, DEFAULT_BAP_TYPE)
            time = _get_time()

            # Update DB
            db.update_db(bapper, bapped, bap_type, time)

            #
            return str((bapper, bapped))

    return app
