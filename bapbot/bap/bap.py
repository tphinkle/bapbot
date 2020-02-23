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

    def __init__(self, bapper, bappee, type, timestamp):
        """
        """


        self.bapper = bapper
        self.bappee = bappee
        self.type = type
        self.timestamp = timestamp


class BapResult(object):
    def __init__(self, attempted_bap):
        """
        """
        self.attempted_bap = attempted_bap
        pass

    @property
    def success(self):
        """
        """
        return (len(failures) == 0)

    @property
    def fail(self):
        """
        """
        return (len(failures) > 0)

    def add_failed_bap_on_cooldown():
        """
        """
        pass
