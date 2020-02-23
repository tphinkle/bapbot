## Imports

# Project
from .. import database as db
from .. import utils


class BapEngine(object):


    def __init__(self):
        """
        """
        self._sql_handle = db.database.SQLHandle.get_create()

    def _check_register_player(self, player_name):
        """
        """
        player = db.functions.get_player(self._sql_handle, player_name)
        if player is None:
            join_date = utils.get_timestamp()
            new_player = player.get_new_player(player_name, join_date)
            db.functions.register_new_player(self._sql_handle, new_player)

    def _bap_allowed(self, bapper, bap_type, timestamp):
        """
        """
        # Check player can perform bap
        date = timestamp.date()
        baps_today = db.functions.get_player_num_baps_on_date(
            self._sql_handle, bapper, bap_type, date)
        player = db.functions.get_player(self._sql_handle, bapper))
        level = db.functions.get_level(self._sql_handle, player.level)



        if baps_today >= max_baps:
            return False

        else:
            return True

    def _execute_bap(self, bapper, bappee, bap_type, timestamp):
        """
        """
        db.functions.log_bap(bapper, bappee, bap_type, timestamp)

    def attempt_bap(self, bapper, bappee, bap_type, timestamp):
        """
        """

        if isinstance(timestamp, str):
            timestamp = utils.timestamp_str_to_timestamp(timestamp)

        self._check_register_player(bapper)
        self._check_register_player(bappee)




        if self._bap_allowed(bapper, bap_type, timestamp):
            self._execute_bap(bapper, bappee, bap_type, timestamp)

    def get_player(self, bapper, bappee, bap_type, timestamp):
        """
        """
        pass
