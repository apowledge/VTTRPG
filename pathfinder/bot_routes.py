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

client.run(BOT_TOKEN) # DONT upload token to github. If you screw up Discord will automatically catch and reset it
