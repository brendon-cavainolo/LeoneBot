# from discord import channel, Client
from discord.ext import commands
from discord.ext.commands import bot, cog
import discord

def valid_channel(ctx):
    allowed_channels = ["class_request", "bot_testing"]
    return ctx.channel.name in allowed_channels

class registerCommand(commands.Cog): #extends
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name= 'register', aliases= ['join', 'registering', 'reg'])
    #async def register(self, ctx, *, course):# self is instance of class
    async def register(self, ctx,  course): #member: discord.Member: self is instance of class
        if not valid_channel(ctx):
            await ctx.send("Wrong channel. Please use this command in #class_request")
            return
        #retrieve ids for channels on server
        #category = discord.utils.get(ctx.guild.categories, name= 'classes')
        #print(category.channels)
        
        #initalize variable to confirm reception of course
        #found = False
        course = course.lower()
        category = "junk"

        if category is None:
            await ctx.channel.send('No classes exist.\n')
        else:
            for channel in ctx.guild.channels:
                if channel.name == course:
                    
                    found = True
                    
                    await channel.set_permissions(ctx.author, read_messages=True,
                                                        send_messages=True)
        if(found):
            await ctx.channel.send('@{} has been registered.'.format(ctx.message.author))
        else: 
            await ctx.channel.send('This class does not exist. Please check your input again or message a mod if you believe there is an error.\n')


    @commands.command(name= 'withdraw', aliases= ['leave','unregister'])
    async def unregister(self, ctx,  course): #member: discord.Member: self is instance of class
        if not valid_channel(ctx):
            await ctx.send("Wrong channel. Please use this command in #class_request")
            return
        #retrieve ids for channels on server
        #category = discord.utils.get(ctx.guild.categories, name= 'classes')
        #print(category.channels)
        
        #initalize variable to confirm reception of course
        #found = False
        category = "junk"

        if category is None:
            await ctx.channel.send('No classes exist.\n')
        else:
            for channel in ctx.guild.channels:
                if channel.name == course:
                    
                    found = True
                    
                    await channel.set_permissions(ctx.author, read_messages=False,
                                                        send_messages=False)
        if(found):
            await ctx.channel.send('@{} has been withdrawn.'.format(ctx.message.author))
        else: 
            await ctx.channel.send('This class does not exist. Please check your input again or message a mod if you believe there is an error.\n')

async def setup(client):
    # needs to be awaited as of version 2.0
	await client.add_cog(registerCommand(client))
# check documentation on kick and class discord.ExpireBehavior
