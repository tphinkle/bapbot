## Imports

# Python standard library
import requests

# Project
import requests
from .. import utils
from .. import REST


SERVER_URL = utils.load_server_config()

class HTTPHandler(object):
    """
    """

    def POST_bap(self, bapper, bappee, bap_type, timestamp):
        """
        """
        # Bapper
        data = REST.bap.POST.assemble(bapper, bappee, bap_type, timestamp)
        response = requests.post('http://127.0.0.1/{}'.format(REST.bap.ENDPOINT), json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError('HTTP request failed ({}, {})'.format(response.status_code, data))

    @staticmethod
    def receive_bap_event(self):
        """
        """
        raise NotImplementedError()
