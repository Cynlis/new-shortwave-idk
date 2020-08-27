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
import googletrans
from googletrans import Translator

from uptime import uptime

translator = Translator()


print(str(datetime.timedelta(seconds=uptime())))

class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.process = psutil.Process()


    @commands.command()
    async def stats(self, ctx):
        embed = discord.Embed(title=f'', description=f"", colour=0x2f3136)
        embed.add_field(name='🏠 Guilds', value=f"{len(self.bot.guilds)}", inline=False)
        embed.add_field(name='💁 Members', value=f"{len(self.bot.users)}", inline=False)
        embed.add_field(name='💎 Shards', value=f"{self.bot.shard_count}".replace("None", "1"), inline=False)
        embed.add_field(name='🎶 Voice Connections', value=f"{len(self.bot.voice_clients)}", inline=False)
        embed.add_field(name='💻 OS Uptime', value=f"{str(datetime.timedelta(seconds=uptime()))}", inline=False)
        embed.add_field(name="💻 CPU Usage", value="{}%".format(round(psutil.cpu_percent())), inline=False)
        embed.add_field(name="💻 RAM usage", value="{}% | {} / {}mb".format(round(psutil.virtual_memory().percent), round(psutil.virtual_memory().used/1048576), round(psutil.virtual_memory().total/1048576)), inline=True)
        await ctx.send(embed=embed)
        
        
        
    @commands.guild_only()
    @commands.command()
    async def translate(self, ctx, *, translation):
      try:
        translator = Translator()
        result = translator.translate(translation)

        embed = discord.Embed(title=f"", description=f"")
        embed.add_field(name=f"Translation | :flag_{result.src}:".replace(":flag_en:", ":england:"), value=f"```{result.text}```", inline=False)
    
        await ctx.send(embed=embed)
      except Exception as e:
        embed = discord.Embed(title=f"Error: `{e}`")
        await ctx.send(embed=embed)

        

    


def setup(bot):
    try:    
        bot.add_cog(Stats(bot))
        print("Loaded stats.py")
    except Exception as e:
        print(f"Error loading stats.py: {e}")