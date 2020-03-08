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
from bapbot.bap import BapGateway
from bapbot import REST, utils

## Globals
GET = 'GET'
POST = 'POST'

# Configure the app
app = Flask(__name__, instance_relative_config=True)

# Set up the handlers
bap_gateway = BapGateway()

@app.route('/')
def home():
    """
    """
    return 'Testing'

@app.route('/bap', methods=[POST])
def bap():
    if request.method == POST:

        data = request.get_json()
        if isinstance(data, str):
            data = json.loads(data)
        response = bap_gateway.bap_post(data)
        return json.dumps(response)


@app.route('/player', methods=[GET])
def player():
    if request.method == GET:
        player_name = request.args.get(REST.player.GET.PLAYER_NAME)
        bap_engine.get_player(request.args)
    return 'ok'

@app.route('/stats', methods=[GET])
def stats():
    if request.method == GET:
        html = bap_engine.get_stats_plot()
        return html

if __name__ == '__main__':
    app.run()
