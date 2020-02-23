## Imports

# Project
from .bap import Bap
from .. import database as db


class BapEngine(object):

    def __init__(self):

    self._sql_handle = db.database.SQLHandle.get_create()


    def _bap_allowed(self, bapper, bap_type, timestamp):
        """
        """
        # Check player can perform bap
        baps_today = db.functions.get_num_baps_today(bapper, bap_type)
        max_baps = db.functions.get_max_baps_allowed(bapper, bap_type)

        if baps_today >= max_baps:
            return False

        else:
            return True

    def _execute_bap(self, bapper, bappee, bap_type, timestamp):
        """
        """
        db.functions.log_bap(bapper, bappee, bap_type, timestamp)


    def attempt_bap(bapper, bappee, bap_type, timestamp):
        """
        """
        if self.bap_allowed(bapper, bap_type, timestamp):
            self.execute_bap(bapper, bappee, bap_type, timestamp)

        if bap_allowed:
            self.execute_bap
