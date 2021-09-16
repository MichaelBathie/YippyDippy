#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import discord
import random

from os.path import join, dirname
from dotenv import load_dotenv
from discord.utils import get
from discord.ext import commands
from spicy import get_nhentai_link

# load .env file
dir_path = os.path.dirname(os.path.realpath(__file__))

dotenv_path = join(dir_path, '.env')
load_dotenv(dotenv_path)

DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

JSON_FILE = str(os.path.dirname(os.path.realpath(__file__))) + '/data.json'

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    """ Runs once the bot has established a connection with Discord """

    print(f'{bot.user.name} has connected to Discord')

    # check if bot has connected to guilds
    if len(bot.guilds) > 0:
        print('connected to the following servers:')

        for guild in bot.guilds:
            print(f'* {guild.name}#{guild.id}')

@bot.command(name="h")
async def send_nhentai_link(context):
    #Takes in nhentai numbers and return the link
    channel = context.channel
    message_components = (context.message.content).split()

    await channel.send(get_nhentai_link(message_components))
        

if __name__ == "__main__":
    # launch bot
    bot.run(DISCORD_TOKEN)
