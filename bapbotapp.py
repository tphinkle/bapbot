## Imports

# Python standard library
import datetime
import json
import os
import time

# Flask
from flask import Flask, request

# Project
import bapbot.handlers as handlers


## Globals
GET = 'GET'
POST = 'POST'

# Configure the app
app = Flask(__name__, instance_relative_config=True)

if __name__ == '__main__':
    # Set up the handlers
    bap_handler = handlers.BapHandler()

    @app.route('/')
    def home():
        return 'Testing'

    @app.route('/bap', methods=(GET, POST))
    def bap():
        if request.method == POST:
            bap_handler.handle_bap_post(request.args)
        return 'ok'

    #@app.route('/bap', methods=(GET, POST))
    #def bap():
    #    if request.method == POST:
    #        bap_handlers.handle_bap_post(request.args)
    #    return 'ok'

    app.run()
