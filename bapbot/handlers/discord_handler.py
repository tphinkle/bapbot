## Imports

# Python standard library
import regex as re

# Project
from .. import utils
from .http_handler import HTTPHandler
from .exceptions import BapParseError




class DiscordHandler(object):
    """
    """

    BAPBOT_NAME = 'bapbot'
    BAPBOT_FULL_NAME = 'bapbot#8352'
    BAP_INDICATOR = '#'

    def __init__(self):
        """
        """
        self._http_handler = HTTPHandler()


    def _extract_bap_type(self, message):
        """
        """

        pattern = '(?={})(.*?)(?= )'.format("\\" + DiscordHandler.BAP_INDICATOR)
        matches = re.search(pattern, message.content)
        print(pattern, message, matches)

        if matches is None:
            bap_type = None
        else:
            bap_type = matches[0].replace(DiscordHandler.BAP_INDICATOR, '')
        return bap_type

    def _is_bap_message(self, message):
        """
        """
        return self._extract_bap_type(message) is not None


    def process_message(self, message):
        """
        """
        if self._is_bap_message(message):
            return self.process_bap_message(message)

        else:
            return None


    def _parse_bap_message(self, message):
        """
        """
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
        bap_type = self._extract_bap_type(message)

        return bapper, bappee, bap_type


    def process_bap_message(self, message):
        """
        """

        # Execute the bap
        timestamp = str(utils.get_timestamp())
        bapper, bappee, bap_type = self._parse_bap_message(message)
        bap_response = self._http_handler.POST_bap(bapper, bappee, bap_type, timestamp)

        return bap_response
