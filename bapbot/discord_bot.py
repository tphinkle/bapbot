# post a message to discord api via a bot
# bot must be added to the server and have write access to the channel
# you may need to connect with a websocket the first time you run the bot
#   use a library like discord.py to do so

## Imports

# Python standard library
import json
import os
import requests

import discord

# Package
import utils

client = discord.Client()

DISCORD_CONFIG = utils.load_discord_config()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    print('asdf')
    if message.author == client.user:
        return

    if '!bap' in message.content:
        await message.channel.send('bap!!!')

client.run(DISCORD_CONFIG['bapbot']['token'])
