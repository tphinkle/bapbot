## Imports

# Project
from . bap import Bap
from . import database as db
from . import utils


class IndexHandler(object):
    """
    """

    def __init__(self):
        """
        """
        self.__sql_handler = db.database.SQLHandle.get_create()

    def handle_get(self):
        """
        """
        last_n_baps = db.functions.get_last_n_baps(self.__sql_handle)
        user_bap_summary = db.functions.get_user_bap_summary(self.__sql_handle)
        return last_n_baps, user_bap_summary

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
        bapper = request_args.get(BapHandler.BAPPER_KEY, None)
        bappee = request_args.get(BapHandler.BAPPEE_KEY, None)
        bap_type = request_args.get(BapHandler.BAP_TYPE_KEY, None)
        time = utils.get_timestamp()

        if bapper is None or bappee is None or bap_type is None:
            return


        bap = Bap(timestamp, bapper, bappee, type)


        # Log bap
        result = db.functions.log_bap(self.__sql_handle, bap)
        return result
