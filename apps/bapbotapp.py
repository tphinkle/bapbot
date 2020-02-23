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
from bapbot import REST

## Globals
GET = 'GET'
POST = 'POST'

# Configure the app
app = Flask(__name__, instance_relative_config=True)

# Set up the handlers
bap_engine = BapEngine()

@app.route('/')
def home():
    """
    """
    return 'Testing'

@app.route('/bap', methods=(POST))
def bap():
    if request.method == POST:

        bapper = request.args.get(REST.bap.POST.BAPPER_KEY)
        bappee = request.args.get(REST.bap.POST.BAPPEE_KEY)
        bap_type = request.args.get(REST.bap.POST.BAP_TYPE_KEY)
        timestamp = request.args.get(REST.bap.POST.TIMESTAMP_KEY)

        bap_engine.attempt_bap(bapper, bappee, bap_type, timestamp)

    return 'ok'

@app.route('/player', methods=(GET))
def bap():
    if request.method == GET:
        player_name = request.args.get(REST.player.GET.PLAYER_NAME)
        bap_engine.get_player(request.args)
    return 'ok'

if __name__ == '__main__':
    app.run()
