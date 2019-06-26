#!/usr/bin/env python3
import discord

# TODO:
# just copied over sbb logic but
# should use discord api built in command feature
# instead of manually filtering for command_prefix

tokensfile = 'tokens.txt'
discord_token = None

client = discord.Client()

command_prefix = '.rap'

def setup_tokens(filename):
    global discord_token
    tokens = open(filename, "r")
    discord_token = tokens.readline().rstrip()
    tokens.close()
    return

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

def main():
    setup_tokens(tokensfile)
    client.run(discord_token)

if __name__ == "__main__": main()
