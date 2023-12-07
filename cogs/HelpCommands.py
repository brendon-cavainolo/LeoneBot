from discord.ext import commands

class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


async def setup(client):
    # needs to be awaited as of version 2.0
	await client.add_cog(HelpCommands(client))