## Imports

# Project
from . import bap

class Level(object):
    """
    """

    def __init__(self, level, exp_needed, daily_baps, daily_baps_power, daily_baps_super, daily_baps_ultra):
        """
        """

        self.level = level
        self.exp_needed = exp_needed
        self.daily_baps = daily_baps
        self.daily_baps_power = daily_baps_power
        self.daily_baps_super = daily_baps_super
        self.daily_baps_ultra = daily_baps_ultra

    def get_daily_bap_limit(self, bap_type):
        """
        """
        if bap_type == bap.BASIC_BAP:
            return self.daily_baps
        elif bap_type == bap.POWER_BAP:
            return self.daily_baps_power
        elif bap_type == bap.SUPER_BAP:
            return self.daily_baps_super
        elif bap_type == bap.ULTRA_BAP:
            return self.daily_baps_ultra
        else:
            return 0
