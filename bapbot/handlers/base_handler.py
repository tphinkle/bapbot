## Imports

# Python standard library
import requests

# Project
from ..bap import bap, bap_engine, bap_response, player
from .. import database as db
from .. import utils


class BaseHandler(object):
    """
    """

    def __init__(self):
        """
        """
        pass

    def handle_bap(self, bapper, bappee, bap_type, timestamp = None):
        """
        """
        # Bapper
        if timestamp is None:
            utils.get_timestamp()

        attempted_bap = bap.Bap(bapper, bappee, bap_type, time_stamp)
        bap_response = bap_engine.execute_bap(attempted_bap)


    def receive_bap_event(self):
        """
        """
        raise NotImplementedError()
