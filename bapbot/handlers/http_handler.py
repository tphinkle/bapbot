## Imports

# Python standard library
import requests

# Project
import requests
from .. import utils


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
        data = {'bapper': bapper,
                'bappee': bappee,
                'bap_type': bap_type,
                'timestamp': timestamp}
        requests.post(SERVER_URL, data=data)
        
    def receive_bap_event(self):
        """
        """
        raise NotImplementedError()
