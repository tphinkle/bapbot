## Imports


## Globals

STARTING_LEVEL = 0
STARTING_EXPERIENCE = 0

## Functions

class Player(object):
    """
    """

    def __init__(self, name, join_date, level, experience):
        """
        """
        self.name = name
        self.join_date = join_date
        self.level = level
        self.experience = experience

    @staticmethod
    def get_new_player(player_name, join_date):
        """
        """
        return Player(player_name, join_date, STARTING_LEVEL, STARTING_EXPERIENCE)
