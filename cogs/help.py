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
        embed.add_field(name='Misc', value=f"`ping`, `stats`, `Covid`, `Radioadd`, `Radionp`, `Captcha`, `Translate`".replace("<@!732176506297778277> ", "."), inline=False)
        embed.add_field(name='Music', value=f"`Play`, `Skip`, `Pause`, `Resume`, `Stop`, `Volume`, `Radio`".replace("<@!732176506297778277> ", "."), inline=False)
        embed.add_field(name='Owner', value=f"`Eval`, `Reload`, `Restart`".replace("<@!732176506297778277> ", "."), inline=False)
        await ctx.send(embed=embed)


    
    

def setup(bot):
    try:    
        bot.add_cog(Help(bot))
        print("Loaded help.py")
    except Exception as e:
        print(f"Error loading help.py: {e}")