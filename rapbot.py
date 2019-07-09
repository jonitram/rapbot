#!/usr/bin/env python3
import asyncio
import discord
from discord.ext import commands

tokensfile = 'tokens.txt'
discord_token = None

bot = commands.Bot(command_prefix='.rb ')

voice_reference = None

def setup_tokens(filename):
    global discord_token
    tokens = open(filename, "r")
    discord_token = tokens.readline().rstrip()
    tokens.close()
    return

@bot.command()
async def rap(ctx, *args):
    global voice_reference
    # multiprocess -> spin up background generate raps
    # store reference for potentially killing later
    voice_reference = asyncio.create_task(test(ctx))
    return

@bot.command()
async def kill(ctx):
    global voice_reference
    voice_reference.cancel()
    voice_reference = None
    await ctx.send('process has been killed')
    return

async def test(ctx):
    while True:
        await ctx.send('pulse')
        await asyncio.sleep(10)
    return

# @bot.command()
# async def kill(ctx):
    # if raps process reference != None
    #   kill it
    # else
    #   let user know nothing was being generated
    # return
    
# @bot.command()
# async def say(ctx):
    # if check precons:
        # (check precons -> user in voice channel, raps file exists, nothing currently playing -> voice reference == None)
        # set voice reference
        # connect
        # play
        # stop
        # disconnect
    # else
        # let user know what precon they failed
    # return

# should be awaited
# @bot.command()
# async def stop(ctx):
#     if voice reference != None:
#         (follow sbb logic)
#         voice reference stop
#         disconnect
#         voice reference = None
#     else
#         nothing was playing

def main():
    setup_tokens(tokensfile)
    bot.run(discord_token)

if __name__ == "__main__": main()
