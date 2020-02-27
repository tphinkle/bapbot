## Imports

# Python standard library
import json


ENDPOINT = 'bap'

class BapRequest_(object):

    """
    """
    BAPPER_KEY = 'bapper'
    BAPPEE_KEY = 'bappee'
    BAP_TYPE_KEY = 'bap_type'
    TIMESTAMP_KEY = 'timestamp'

    def __init__(self):
        pass



class POST(object):

    # Request
    obj = BapRequest_

    def deserialize():
        """
        """
        bapper = _get_request_arg(data, REST.bap.POST.BAPPER_KEY)
        bappee = _get_request_arg(data, REST.bap.POST.BAPPEE_KEY)
        bap_type = _get_request_arg(data, REST.bap.POST.BAP_TYPE_KEY)
        timestamp = _get_request_arg(data, REST.bap.POST.TIMESTAMP_KEY, error=False)
        if timestamp is None:
            timestamp = utils.get_timestamp()
