class GET(object):

    PLAYER_NAME_KEY = 'player_name'

    @staticmethod
    def assemble_player_GET_data(player_name):
        """
        """
        return {GET.PLAYER_NAME_KEY: player_name}
