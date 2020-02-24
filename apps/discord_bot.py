# post a message to discord api via a bot
# bot must be added to the server and have write access to the channel
# you may need to connect with a websocket the first time you run the bot
#   use a library like discord.py to do so

## Imports

# Python standard library
import json
import os
import requests

# Discord
import discord

# Package
from bapbot import utils
from bapbot.handlers.discord_handler import DiscordHandler


if __name__ == '__main__':
    client = discord.Client()

    DISCORD_CONFIG = utils.load_discord_config()
    handler = DiscordHandler()

    VALID_CHANNELS = ['general', 'bapbot_test']


    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):

        # Only valid channels
        channel = message.channel
        print('channel', channel, dir(channel), channel.name)
        if channel.name not in VALID_CHANNELS:
            return

        # Avoid infinite looop
        if message.author == client.user:
            return

        # Actual content
        response = handler.process_message(message)
        if response is None:
            return

        response = json.dumps(response)

        print('going to send response', response)
        await message.channel.send(response)

    client.run(DISCORD_CONFIG['bapbot']['token'])
