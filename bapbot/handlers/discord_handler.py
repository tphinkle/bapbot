## Imports

# Project
from ..bap import Bap
#from .. import database as db

from .. import utils
from .http_handler import HTTPHandler
from .exceptions import BapParseError


class DiscordHandler(object):
    """
    """

    BAPBOT_NAME = 'bapbot'
    BAPBOT_FULL_NAME = 'bapbot#8352'
    BAP_INICATOR = '!'

    def __init__(self):
        """
        """
        self._http_handler = HTTPHandler


    def _parse_bap_message(self, message):
        # Bapper
        bapper = message.author.name

        # Bappee
        mentions = message.mentions
        if len(mentions) > 2:
            raise BapParseError
        for mention in mentions:
            if DiscordHandler.BAPBOT_NAME not in mention.name:
                bappee = mention.name

        # Type
        for bap_type in Bap.BAP_TYPES:
            if '!{}'.format(bap_type) in message.content:
                break
        return bapper, bappee, bap_type


    def receive_bap_event(self, message):
        """
        """

        # Execute the bap
        timestamp = utils.get_timestamp()
        bapper, bappee, bap_type = self._parse_bap_message(message)
        bap_response = self.HTTPHandler.POST_bap(bapper, bappee, bap_type, timestamp)
