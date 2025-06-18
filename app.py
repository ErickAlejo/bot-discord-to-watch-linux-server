import discord
from discord.ext import commands
from commands import *

global BOT, INTENTS
INTENTS = discord.Intents.default()
INTENTS.message_content = True
BOT = commands.Bot(command_prefix="!", intents=INTENTS)


@BOT.event
async def on_ready():
    print(f'Logged as {BOT.user}\n')

@BOT.command()
async def server(channel:object, message:str, *arg):
    params:tuple = arg
    if 'ls' in message:
        result: str = ls(param=params)
        await channel.send(result)
    
    elif 'ps' in message:
        result: str = ps(param=params)
        await channel.send(result)

    elif 'cat' in message:
        result: str = ps(param=params)
        await channel.send(result)


# Run app
BOT.run('YOUR TOKEN')
