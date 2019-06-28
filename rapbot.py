#!/usr/bin/env python3
import asyncio
import discord
from discord.ext import commands

tokensfile = 'tokens.txt'
discord_token = None

bot = commands.Bot(command_prefix='.rb ')

def setup_tokens(filename):
    global discord_token
    tokens = open(filename, "r")
    discord_token = tokens.readline().rstrip()
    tokens.close()
    return

@bot.command()
async def rap(ctx, *args):
    return

def main():
    setup_tokens(tokensfile)
    bot.run(discord_token)

if __name__ == "__main__": main()
