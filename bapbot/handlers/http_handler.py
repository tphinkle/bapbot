## Imports

# Python standard library
import requests

# Project
import requests
from .. import utils
from . import REST


SERVER_URL = utils.load_server_config()

class HTTPHandler(object):
    """
    """

    def __init__(self):
        """
        """
        pass

    def POST_bap(self, bapper, bappee, bap_type, timestamp):
        """
        """
        # Bapper
        data = REST.assemble_bap_POST(bapper, bappee, bap_type, timestamp)
        requests.post(SERVER_URL, data=data)

    def receive_bap_event(self):
        """
        """
        raise NotImplementedError()
