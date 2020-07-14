from discord.ext import commands, tasks
from collections import Counter, defaultdict

import pkg_resources
import logging
import discord
import textwrap
import datetime
import traceback
import itertools
import typing
import asyncpg
import asyncio
import pygit2
import psutil
import json
import os
import re
import io
import gc

class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.process = psutil.Process()


    @commands.command()
    async def stats(self, ctx):
        embed = discord.Embed(title=f'', description=f"", colour=0x2f3136)
        embed.add_field(name='🏠 Guilds', value=f"{len(self.bot.guilds)}", inline=False)
        embed.add_field(name='💁 Members', value=f"{len(self.bot.users)}", inline=False)
        embed.add_field(name="💻 CPU Usage", value="{}%".format(round(psutil.cpu_percent())), inline=False)
        embed.add_field(name="💻 RAM usage", value="{}% | {} / {}mb".format(round(psutil.virtual_memory().percent), round(psutil.virtual_memory().used/1048576), round(psutil.virtual_memory().total/1048576)), inline=True)
        await ctx.send(embed=embed)

        

    


def setup(bot):
    try:    
        bot.add_cog(Stats(bot))
        print("Loaded stats.py")
    except Exception as e:
        print(f"Error loading stats.py: {e}")