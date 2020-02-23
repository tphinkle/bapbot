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
import bapbot.handlers as handlers


## Globals
GET = 'GET'
POST = 'POST'

# Configure the app
app = Flask(__name__, instance_relative_config=True)

# Set up the handlers
bap_handler = handlers.BapHandler()

@app.route('/')
def home():
    """
    """
    return 'Testing'

@app.route('/bap', methods=(GET, POST))
def bap():
    print('asdf')
    if request.method == POST:
        bap_handler.handle_bap_post(request.args)
    return 'ok'

if __name__ == '__main__':


    #@app.route('/bap', methods=(GET, POST))
    #def bap():
    #    if request.method == POST:
    #        bap_handlers.handle_bap_post(request.args)
    #    return 'ok'

    app.run()
