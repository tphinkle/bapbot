# post a message to discord api via a bot
# bot must be added to the server and have write access to the channel
# you may need to connect with a websocket the first time you run the bot
#   use a library like discord.py to do so

## Imports
import json
import os
import requests



CHANNEL_ID = DISCORD_CONFIG['channels']['bapbottest']['id']
TEXT_CHANNEL_ID = DISCORD_CONFIG['channels']['bapbottest']['text_channels']['general']['id']

BOT_TOKEN = DISCORD_CONFIG['bapbot']['token']
BASE_URL = "https://discordapp.com/channels/{}/{}/messages".format(CHANNEL_ID, TEXT_CHANNEL_ID)




HEADERS = { "Content-Type":"application/json", }

message = "hello world"

post_json = json.dumps({"content":message})

r = requests.post(BASE_URL, headers = HEADERS, data = post_json)
