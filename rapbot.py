#!/usr/bin/env python3
import asyncio
import discord
from discord.ext import commands

# TODO:
# just copied over sbb logic but
# should use discord api built in command feature
# instead of manually filtering for command_prefix

tokensfile = 'tokens.txt'
discord_token = None

# client = discord.Client()

bot = commands.Bot(command_prefix='.rb ')

def setup_tokens(filename):
    global discord_token
    tokens = open(filename, "r")
    discord_token = tokens.readline().rstrip()
    tokens.close()
    return

@bot.command()
async def rap(ctx, *args):
    await ctx.send('-'.join(args))
    return

# @client.event
# async def on_ready():
#     print('Logged in as')
#     print(client.user.name)
#     print(client.user.id)
#     print('------')

# @client.event
# async1 def on_message(message):
    # if message.content.startswith(command_prefix):
        # do shit
        # this is old way of filtering but should really
        # just use discord command feature instead
        # will have to look into that
    # return  

def main():
    setup_tokens(tokensfile)
    bot.run(discord_token)
    # client.run(discord_token)

if __name__ == "__main__": main()
