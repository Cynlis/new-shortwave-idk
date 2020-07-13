from discord.ext import commands
import traceback
import datetime
import discord
import logger

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def ping(self, ctx): 
        await ctx.send(f":ping_pong: Ping : `{round(self.bot.latency * 1000)}ms`")

def setup(bot):
    bot.add_cog(Ping(bot))
    print("Loaded ping.py")