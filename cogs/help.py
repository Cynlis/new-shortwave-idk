from discord.ext import commands
import traceback
import datetime
import discord
import logger

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title=f'Help', description=f"", colour=0x2f3136)
        embed.add_field(name='Misc', value=f"`{ctx.prefix}ping`, `{ctx.prefix}stats`", inline=False)
        embed.add_field(name='Music', value=f"`{ctx.prefix}Play`, `{ctx.prefix}Skip`, `{ctx.prefix}Pause`, `{ctx.prefix}Resume`, `{ctx.prefix}Stop`", inline=False)
        embed.add_field(name='Owner', value=f"`{ctx.prefix}Eval`, `{ctx.prefix}Reload`, `{ctx.prefix}Restart`", inline=False)
        await ctx.send(embed=embed)


    
    

def setup(bot):
    try:    
        bot.add_cog(Help(bot))
        print("Loaded help.py")
    except Exception as e:
        print(f"Error loading help.py: {e}")