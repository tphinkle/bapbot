## Imports

# Project
from . bap import Bap
from . import database as db
from . import utils


class BapHandler(object):
    """
    """
    BAPPEE_KEY = 'bappee'
    BAPPER_KEY = 'bapper'
    BAP_TYPE_KEY = 'bap_type'


    def __init__(self):
        """
        """
        self.__sql_handler = db.database.SQLHandle.get_create()


    def handle_post(self, request_args):
        """
        """
        # Construct bap
        bapper = request_args.get(BapHandler.BAPPER_KEY)
        bappee = request_args.get(BapHandler.BAPPEE_KEY)
        bap_type = request_args.get(BapHandler.BAP_TYPE_KEY)
        time = utils.get_timestamp()

        try:
        bap = Bap(timestamp, bapper, bappee, type)

        # Log bap
        result = db.functions.log_bap(self.__sql_handle, bap)
        return result