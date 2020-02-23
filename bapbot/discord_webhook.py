# post a message to discord api via a bot
# bot must be added to the server and have write access to the channel
# you may need to connect with a websocket the first time you run the bot
#   use a library like discord.py to do so

## Imports
import json
import os
import requests

curr_path = os.path.abspath(__file__)
discord_config_file_path = os.path.join(curr_path.split('bapbot')[0], 'bapbot', 'tmp', 'discord.json')
with open(discord_config_file_path, 'r') as file_handle:
    DISCORD_CONFIG = json.load(file_handle)

CHANNEL_ID = DISCORD_CONFIG['channels']['bapbottest']['id']
TEXT_CHANNEL_ID = DISCORD_CONFIG['channels']['bapbottest']['text_channels']['general']['id']

BOT_TOKEN = DISCORD_CONFIG['bapbot']['token']
BASE_URL = "https://discordapp.com/channels/{}/{}/messages".format(CHANNEL_ID, TEXT_CHANNEL_ID)




HEADERS = { "Content-Type":"application/json", }

message = "hello world"

post_json = json.dumps({"content":message})

r = requests.post(BASE_URL, headers = HEADERS, data = post_json)


print(r)
print(dir(r))
print(r.text)
