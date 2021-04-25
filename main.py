import discord.ext
from discord.ext import commands, tasks

import asyncio

import json
from typing import Tuple

from schedule_manager import *
from timetable import time_table


# Load bot token and prefix
with open('config.json') as json_file:
    data = json.load(json_file)
    bot_prefix = data['prefix']
    bot_token = data['token']


#intent to get members
intents = discord.Intents.default()
intents.members = True

# Define commands
bot = commands.Bot(command_prefix=bot_prefix, intents=intents)

master_schedule = generate_shedule()


# Bot started
@bot.event
async def on_ready():
    print('Bot online')


@bot.command(name="online", brief="Checks status")
async def online(ctx):
    await ctx.send(f"Time Pocket Bot Online\nPing: {round(bot.latency * 1000)}ms")


# ========================================= COMMANDS =========================================
@bot.command(name="eventAdmin", description="")
async def eventAdmin(ctx, username:str, discriminator:str, day: str, start_time:str, end_time:str, event_name="", priority=-1):
    start = parse_time(start_time)
    end = parse_time(end_time)

    start_hour = start[0]
    start_min = round_nearest(start[1],15)//15

    end_hour = end[0]
    end_min = round_nearest(end[1],15)//15

    day_index = parse_day(day)*24*4

    start_index = start_hour*4 + start_min + day_index
    end_index = end_hour*4 + end_min + day_index

    user = discord.utils.get(bot.get_all_members(), name=username , discriminator=discriminator)

    if(user == None):
        await ctx.send(f"User {username} with discriminator {discrim} not found!")
        return

    userid = discord.utils.get(bot.get_all_members(), name=username , discriminator=discriminator).id

    name = username + "#" + str(userid)

    add_event(master_schedule, start_index, end_index, name, event_name, priority)
    await ctx.send(f"Added {event_name} for {username}")

@bot.command(name="event", description="")
async def event(ctx, day: str, start_time:str, end_time:str, event_name="", priority=-1):
    start = parse_time(start_time)
    end = parse_time(end_time)

    start_hour = start[0]
    start_min = round_nearest(start[1],15)//15

    end_hour = end[0]
    end_min = round_nearest(end[1],15)//15

    day_index = parse_day(day)*24*4

    start_index = start_hour*4 + start_min + day_index
    end_index = end_hour*4 + end_min + day_index

    name = ctx.author.name + "#" + str(ctx.author.id)

    add_event(master_schedule, start_index, end_index, name, event_name, priority)
    await ctx.send(f"Added {event_name} for {ctx.author.name}")
    
#region Command Parsing
def round_nearest(num: int, base=15) -> int:
    return base * round(num/base)


def parse_time(time: str) -> Tuple[int, int]:
    """Returns hour, minute"""
    time_array = time.split(":")
    return int(time_array[0]), int(time_array[1])


def parse_day(day: str) -> int:
    for i in range(len(WEEK_DAYS)):
        if day.lower() == list(WEEK_DAYS.values())[i].lower():
            return i
    # Not found
    return -1
#endregion

@bot.command()
async def schedule(ctx):
    # run typing as user waits
    async with ctx.typing():
        # do expensive stuff here
        await asyncio.sleep(0.1)
    title = "Schedule"
    #print(master_schedule)
    event_data = schedule_to_event_data(master_schedule)
    #print(event_data)
    file_name = time_table(event_data, title=title)
    await ctx.send(file=discord.File(file_name))




@bot.event
async def on_message(message):
    if message.author.bot:
        return
    #await message.channel.send(message.created_at)

    # on_message overrides @client.command events, so this is required
    await bot.process_commands(message)


# Recurring task
@tasks.loop(hours=1)
async def loopTask():
    pass


# bot.load_extension(f'')
bot.run(bot_token)
