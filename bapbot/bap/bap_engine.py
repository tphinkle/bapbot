## Imports


# Scientific computing
import bokeh

# Project
from .. import database as db
from .. import utils
from .bap import Bap
from .level import Level
from .player import Player



class BapEngine(object):


    def __init__(self):
        """
        """
        self._sql_handle = db.database.SQLHandle.get_create()

    def _check_register_player(self, player_name):
        """
        """
        player = db.functions.get_player(self._sql_handle, player_name)
        if len(player) == 0:
            join_date = utils.get_timestamp()
            new_player = Player.get_new_player(player_name, join_date)
            db.functions.register_new_player(self._sql_handle, new_player.name, new_player.join_date, new_player.level, new_player.experience)

    def _bap_allowed(self, player_name, bap_type, timestamp):
        """
        """
        # Check player can perform bap
        date = timestamp.date()
        baps_today = db.functions.get_baps(
            self._sql_handle, bapper=player_name, bap_type=bap_type, date_dt=date)
        player = Player(*db.functions.get_player(self._sql_handle, player_name))
        level = Level(*db.functions.get_level(self._sql_handle, player.level))

        bap_limit = level.get_daily_bap_limit(bap_type)

        if len(baps_today) >= level.get_daily_bap_limit(bap_type):
            return False
        else:
            return True

    def _execute_bap(self, bap_attempt):
        """
        """
        db.functions.log_bap(self._sql_handle, bap_attempt.bapper, bap_attempt.bappee, bap_attempt.bap_type, bap_attempt.timestamp)


    def attempt_bap(self, bap_attempt):
        """
        """

        if isinstance(bap_attempt.timestamp, str):
            bap_attempt.timestamp = utils.timestamp_str_to_timestamp(bap_attempt.timestamp)

        self._check_register_player(bap_attempt.bapper)
        self._check_register_player(bap_attempt.bappee)

        if self._bap_allowed(bap_attempt.bapper, bap_attempt.bap_type, bap_attempt.timestamp):
            self._execute_bap(bap_attempt.bapper, bap_attempt.bappee, bap_attempt.bap_type, bap_attempt.timestamp)

            baps = [Bap(*bap) for bap in db.functions.get_baps(
                self._sql_handle, bappee=bappee, date_dt=utils.get_today_date())]

            bap_count = {BAP_TYPE: 0 for BAP_TYPE in Bap.BAP_TYPES}

            for bap in baps:
                bap_count[bap.type] += 1



            return {'bap': 'success', 'baps_today': bap_count}

        else:
            return {'bap': 'fail'}

    def get_player(self, bapper, bappee, bap_type, timestamp):
        """
        """
        pass
