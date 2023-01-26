import discord
from dotenv import load_dotenv
import os
import re
import random


load_dotenv(dotenv_path='secrets.env')

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hi'):
        await message.channel.send(f"Hello, I'm {client.user}!")

    pattern = re.compile(r"/(\d*)(D\d*)((?:[+*-](?:\d+|\([A-Z]*\)))*)(?:\+(D\d*))?/i")
    if re.search(pattern, message.content):
        await message.channel.send('you want ME to roll for that?')



client.run(os.environ.get('BOT_TOKEN')) # DONT upload token to github. If you screw up Discord will automatically catch and reset it
