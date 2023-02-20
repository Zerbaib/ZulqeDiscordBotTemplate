import discord
from discord.ext import commands, tasks
import random
import os

import config # Your Bot Config File

bot = commands.Bot(command_prefix=config.prefix, description='A bot that does stuff.', intents=discord.Intents.all(), help=None)
bot.remove_command('help')

@bot.event
async def on_ready():
    await load_cogs()
    print('Bot is ready.')
    status_task.start()

# Status Task
@tasks.loop(minutes=0.15)
async def status_task():
    status = ['discord.py', 'with tasks', 'with loops', 'with coroutines', 'with async/await']
    await bot.change_presence(activity=discord.Game(random.choice(status)))

# Load Cogs On Start
async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'Loaded {filename[:-3]}')

# Run Bot
bot.run(config.token)