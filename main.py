import discord
from discord.ext import commands, tasks
# from Data import config
import requests # make http requests and returns .json files
import json
import asyncio
import random, os
from dotenv import load_dotenv


# class Client(discord.Client):
#     async def on_ready(self):
#         print('{0} is logged in !'.format(self.user))
#     async def on_message(self, message):
#         if(message.author == self.user):
#             return
#         if(message.content.startswith(config.prefix)):
#             return

#         if(message.content.startswith(config.prefix+'hi' or config.prefix+'hello')):
#             await message.channel.send('Hello there!')
#         if(message.content.startswith(config.prefix + 'inspire')):
#             await message.channel.send(get_quote())

#@commands.command()
#async def test(ctx):
#    pass

#client = Client()
load_dotenv()
TOKEN=os.getenv("DISCORD_TOKEN")


description='''register for classes'''
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = commands.Bot(command_prefix='!', description=description, intents = intents)
                    #   config.prefix)

@client.event
async def on_ready():
    print('RegistrarBot is logged in !')

extensions= os.listdir('cogs')

print(extensions)

# extensions = 'cogs.CommandEvents'

# if __name__ == '__main__':
#     for ext in extensions:
#         client.load_extension(ext)

async def main():
    for filename in os.listdir('./cogs'):
        if filename.endswith(".py"):
            await client.load_extension(f'cogs.{filename[:-3]}')
    
    async with client:
        await client.start(TOKEN)

asyncio.run(main())
# client.run(process.env.DISCORD_TOKEN)
# client.run(config.token)
