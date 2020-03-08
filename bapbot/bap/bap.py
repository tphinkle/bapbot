## Imports

## Globals
BASIC_BAP = 'bap'
POWER_BAP = 'powerbap'
SUPER_BAP = 'superbap'
ULTRA_BAP = 'ultrabap'
BAP_TYPES = [BASIC_BAP, POWER_BAP, SUPER_BAP, ULTRA_BAP]


## Functions
class BapAttempt(object):
    """
    """
    def __init__(self, timestamp, bapper, bappee, type):
        """
        """
        self.bapper = bapper
        self.bappee = bappee
        self.type = type
        self.timestamp = timestamp

class BapAttemptResult(object):
    """
    """

    def __init__(self, attempted_bap):
        """
        """
        self.attempted_bap = attempted_bap


class BapAttemptSuccess(BapAttemptResult):
    """
    """

    def __init__(self, attempted_bap):
        """
        """
        super(self).__init__(attempted_bap)


class BapAttemptFailure(BapAttemptResult):
    """
    """

    def __init__(self, attempted_bap):
        """
        """
        super(self).__init__(attempted_bap)
