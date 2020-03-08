## Imports

# Project
from .bap import Bap, BapAttempt
from .bap_engine import BapEngine


## Globals


class BapGateway(object):

    @staticmethod
    def _get_request_arg(data, key, error=True):
        """
        """
        arg = data.get(key)
        if arg is None and error:
            raise ValueError('Required arg is missing from data ({}), {}'.format(key, data))
        return arg


    def __init__(self):
        self._bap_engine = bap_engine
        bap_engine.attempt_bap(bapper, bappee, bap_type, timestamp)


    def bap_post(self, data):
        """
        """

        # Deserialize the request


        # Perform the reequest
        bap_attempt = REST.bap.deserialize(data)BapAttempt(bapper, bappee, bap_type, timestamp)

        bap_attempt_result = bap_engine.attempt_bap(bap_attempt)

        # Serialize the request
        data = bap_attempt_result

        return data

    def bap_get(self, data):
        """
        """

        # Deserialize the request
        bapper = _get_request_arg(data, REST.bap.POST.BAPPER_KEY)
        bappee = _get_request_arg(data, REST.bap.POST.BAPPEE_KEY)
        bap_type = _get_request_arg(data, REST.bap.POST.BAP_TYPE_KEY)
        timestamp = _get_request_arg(data, REST.bap.POST.TIMESTAMP_KEY, error=False)
        if timestamp is None:
            timestamp = utils.get_timestamp()

        # Perform the request
        bap_attempt = BapAttempt(**data)
        bap_result = bap_engine.attempt_bap(bap_attempt)

        # Serialize the request
        data = bap_attempt_result

        return data
