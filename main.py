import discord.ext
from discord.ext import commands, tasks
import json
from schedule_manager import *

# Load bot token and prefix
with open('config.json') as json_file:
    data = json.load(json_file)
    bot_prefix = data['prefix']
    bot_token = data['token']


# Define commands
bot = commands.Bot(command_prefix=bot_prefix)

schedule = generate_shedule()


# Bot started
@bot.event
async def on_ready():
    print('Bot online')


@bot.command(name="online", brief="Checks status")
async def online(ctx):
    await ctx.send(f"Time Pocket Bot Online\nPing: {round(bot.latency * 1000)}ms")


@bot.command(name="", description="")
async def command_name(ctx):
    pass


@bot.event
async def on_message(message):

    # on_message overrides @client.command events, so this is required
    await bot.process_commands(message)


# Recurring task
@tasks.loop(hours=1)
async def loopTask():
    pass


# bot.load_extension(f'')
bot.run(bot_token)
