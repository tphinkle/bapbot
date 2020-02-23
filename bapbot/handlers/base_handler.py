## Imports

# Project
from .. import bap
from .. import database as db
from .. import utils


class BaseHandler(object):
    """
    """

    def __init__(self):
        """
        """
        self.__sql_handle = db.database.SQLHandle.get_create()

    def execute_bap(self, bap):
        """
        """
        # Log bap
        bap_response = db.functions.log_bap(self.__sql_handle, bap)
        return bap_response

    def handle_bap_event(self):
        """
        """
        raise NotImplementedError()
