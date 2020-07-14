import discord
import env
from discord.ext import commands
import random
import time
import os
import datetime
from collections import Counter

client=discord.AutoShardedClient(shard_count=1)
client = commands.Bot(command_prefix="sw!", case_insensitive=True)
client.remove_command('help')

@client.event
async def on_ready():
    print("Bot is ready!")

@client.command()
@commands.is_owner()
async def restart(ctx):
    embed = discord.Embed(
      title='Restarting..', description='', colour=random.randint(0, 0xFFFFFF))
  
    m = await ctx.send(embed=embed)
    os.system("python restart.py")
    
    time.sleep(0.2) # 200ms to CTR+C twice





extensions = ['cogs.ping', 'cogs.eval', 'cogs.cogs', 'cogs.help', "cogs.music", "cogs.stats"]


if __name__ == '__main__':
    for ext in extensions:
        client.load_extension(ext)


client.run(env.TOKEN)