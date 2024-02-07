from discord import channel
from discord.ext import commands
from discord.ext.commands import bot, cog
import random

class CommandEvents(commands.Cog): #extends
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def echo(self, ctx, arg):
        await ctx.channel.send(arg)


async def setup(client):
    # needs to be awaited as of version 2.0
	await client.add_cog(CommandEvents(client))

