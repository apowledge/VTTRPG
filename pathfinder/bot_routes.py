import discord
from dotenv import load_dotenv
import os

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
        await message.channel.send('Hello!')

client.run(os.environ.get('BOT_TOKEN')) # DONT upload token to github. If you screw up Discord will automatically catch and reset it
