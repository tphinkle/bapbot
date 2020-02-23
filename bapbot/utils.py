## Imports

# Python standard library
import datetime
import json
import os

## Functions
def get_timestamp():
    """
    """
    return datetime.datetime.now()

def get_today_date():
    """
    """
    return datetime.datetime.today().date()

def load_discord_config():
    """
    """
    curr_path = os.path.abspath(__file__)
    discord_config_file_path = os.path.join(curr_path.split('bapbot')[0], 'bapbot', 'tmp', 'discord.json')
    with open(discord_config_file_path, 'r') as file_handle:
        return json.load(file_handle)

def load_server_config():
    """
    """
    curr_path = os.path.abspath(__file__)
    discord_config_file_path = os.path.join(curr_path.split('bapbot')[0], 'bapbot', 'tmp', 'server.json')
    with open(discord_config_file_path, 'r') as file_handle:
        return json.load(file_handle)
