## Imports

# Project
from .. import bap
from .. import database as db
from .. import utils


class HTTPHandler(BaseHandler):
    """
    """
    BAPPEE_KEY = 'bappee'
    BAPPER_KEY = 'bapper'
    BAP_TYPE_KEY = 'bap_type'


    def __init__(self):
        """
        """
        pass


    def handle_bap_event(self, request_args):
        """
        """
        # Construct bap
        bapper = request_args.get(BapHandler.BAPPER_KEY, None)
        bappee = request_args.get(BapHandler.BAPPEE_KEY, None)
        bap_type = request_args.get(BapHandler.BAP_TYPE_KEY, None)
        time = utils.get_timestamp()

        bap = Bap(timestamp, bapper, bappee, type)

        self.execute_bap(bap)
