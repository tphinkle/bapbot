
ENDPOINT = 'bap'

class POST(object):


    BAPPER_KEY = 'bapper'
    BAPPEE_KEY = 'bappee'
    BAP_TYPE_KEY = 'bap_type'
    TIMESTAMP_KEY = 'timestamp'

    @staticmethod
    def assemble(bapper, bappee, bap_type, timestamp):
        """
        """

        return json.dumps({POST.BAPPER_KEY: bapper,
                POST.BAPPEE_KEY: bappee,
                POST.BAP_TYPE_KEY: bap_type,
                POST.TIMESTAMP_KEY: timestamp})
