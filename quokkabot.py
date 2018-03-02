import discord
from discord.ext import commands
import config

bot = commands.Bot(command_prefix='¿', description=':D')

@bot.event
async def on_ready():
    print('_,.-\'`¯¯`\'-.,_')
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('¯`\'-.,__,.-\'`¯')

@bot.command()
async def hello():
    await bot.say('Hello! :D')

@bot.command()
async def pls():
    await bot.say('Yes? :D')

@bot.command()
async def say(args):
    await bot.say()

bot.run(config.token)