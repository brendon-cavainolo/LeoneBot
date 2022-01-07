# from discord import channel, Client
from discord.ext import commands
from discord.ext.commands import bot, cog
import discord


class registerCommand(commands.Cog): #extends
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name= 'register', aliases= ['join', 'registering', 'reg'])
    #async def register(self, ctx, *, course):# self is instance of class
    async def register(self, ctx,  course): #member: discord.Member: self is instance of class

        #retrieve ids for channels on server
        category = discord.utils.get(ctx.guild.categories, name= 'classes')
        print(category.channels)
        
        found = False
        
        if category is None:
            await ctx.channel.send('No classes exist.\n')

        else:
            for channel in category.channels:
                print(channel.name)
                print(course)
                if channel.name == course:
                    found = True
                    # channel_info = discord.get.utils(server.channels, name=ch, type="ChannelType.voice")
                    # gives privilages to user and add them to the requested channel
                    # print(channel.name)
                    print("made it here")
                    # overwrites = {
                    #     ctx.guild.default_role: discord.PermissionOverwrite(read_messages= False), 
                    #     ctx.guild.me: discord.PermissionOverwrite(read_messages= True), 
                    #     ctx.author: discord.PermissionOverwrite(read_messages= True),         
                    # }
                    await channel.set_permissions(ctx.author, read_messages=True,
                                                        send_messages=True)
        if(found):
            await ctx.channel.send('@{} has been registered.'.format(ctx.message.author))
        else: 
            await ctx.channel.send('This class does not exist. Please check your input again or message a mod if you believe there is an error.\n')


        #new_channel = self.bot.get_channel(channel_id)
        # member = ctx.message.author
        # await member.move_to(new_channel) # only works for voice channels
        
        #await ctx.channel.send('Member have been registered')

def setup(bot):#required
    bot.add_cog(registerCommand(bot))


# check documentation on kick and class discord.ExpireBehavior
