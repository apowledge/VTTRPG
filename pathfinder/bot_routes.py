import discord
#from ..SECRETS.SECRETS import BOT_TOKEN

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

client.run('MTA2NzkwMjY0ODM0ODU3MzgxNg.GKfd5e.m9a4N6xIcqFrnhmXeIj4sIpf3gsGQ4gfQILGmU')