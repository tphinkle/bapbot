import bapbot.utils as utils

import os
import requests

URL = utils.load_server_config()['url']




if __name__ == '__main__':
    data = {'bapper': 'jon',
            'bappee': 'jon',
            'bap_type': 'ultra'}
    requests.post(url = os.path.join(URL, 'bap'), data = data)
