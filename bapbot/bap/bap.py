## Imports

## Globals

## Functions
class Bap(object):
    """
    """
    BASIC_BAP = 'basic'
    POWER_BAP = 'power'
    SUPER_BAP = 'super'
    ULTRA_BAP = 'ultra'

    BAP_TYPES = [BASIC_BAP, POWER_BAP, SUPER_BAP, ULTRA_BAP]

    def __init__(self, timestamp, bapper, bappee, type):
        """
        """

        self.timestamp = timestamp
        self.bapper = bapper
        self.bappee = bappee
        self.type = type