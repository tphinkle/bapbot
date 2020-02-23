## Imports

# Python standard library
import datetime
import json
import os
import sys
import time

# Flask
sys.path.append('/var/www/html/bapbot/env/lib/python3.6/site-packages/')
sys.path.append('/var/www/html/bapbot/env/lib/python3.6/site-packages')
from flask import Flask, request

# Project
from bapbot.bap import BapEngine
from bapbot import REST, utils

## Globals
GET = 'GET'
POST = 'POST'

# Configure the app
app = Flask(__name__, instance_relative_config=True)

# Set up the handlers
bap_engine = BapEngine()

def _get_request_arg(request, key, error=True):
    """
    """
    arg = request.args.get(key)
    if arg is None and error:
        raise ValueError('Required arg is missing ({}), {}'.format(key, request.args))
    return arg

@app.route('/')
def home():
    """
    """
    return 'Testing'

@app.route('/bap', methods=[POST])
def bap():
    if request.method == POST:

        bapper = _get_request_arg(request, REST.bap.POST.BAPPER_KEY)
        bappee = _get_request_arg(request, REST.bap.POST.BAPPEE_KEY)
        bap_type = _get_request_arg(request, REST.bap.POST.BAP_TYPE_KEY)
        timestamp = _get_request_arg(request, REST.bap.POST.TIMESTAMP_KEY, error=False)
        if timestamp is None:
            timestamp = utils.get_timestamp()

        bap_engine.attempt_bap(bapper, bappee, bap_type, timestamp)

    return 'ok'

@app.route('/player', methods=[GET])
def player():
    if request.method == GET:
        player_name = request.args.get(REST.player.GET.PLAYER_NAME)
        bap_engine.get_player(request.args)
    return 'ok'

if __name__ == '__main__':
    app.run()
