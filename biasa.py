import discord
from discord.ext import commands
import asyncio

TOKEN = 'NTU2NDQzODE4NDM0NjI1NTU0.D3Mrbw.yb4pzCNfEzWUCddHNUOdH-PUFsA'

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def ping():
    await client.say('Pong!')

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

client.run(TOKEN)
