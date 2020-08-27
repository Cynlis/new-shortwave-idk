import discord
import env
from discord.ext import commands
import random
import time
import os
import datetime
import json 
import requests
from collections import Counter
from discord.ext.commands import when_mentioned_or
import googletrans
from googletrans import Translator
import asyncio

def get_prefix(client, message):
  try:
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    e = prefixes[str(message.guild.id)]

    return prefixes[str(message.guild.id)]
  except:
    prefixes = ['"']

    return commands.when_mentioned_or(*prefixes)(client, message)

client=discord.Client(shard_count=1,shard_id=1)
client = commands.Bot(command_prefix=get_prefix, case_insensitive=True)
client.remove_command('help')





@client.command(aliases=["coronavirus", "corona","covid"])
async def cov(ctx: commands.Context):	

      
      embed = discord.Embed(title="Please wait..")
      m = await ctx.send(embed=embed)
      await asyncio.sleep(1)
			
		

      try:	
						
  					
        r = requests.get(f'https://api.covid19api.com/summary')
        j = r.json()	
	
        total = "{:,}".format(j['Global']['TotalConfirmed'])
        TotalD = "{:,}".format(j['Global']['TotalDeaths'])
        TotalR = "{:,}".format(j['Global']['TotalRecovered'])
        
        new = "{:,}".format(j['Global']['NewConfirmed'])
        newD = "{:,}".format(j['Global']['NewDeaths'])
        NewR = "{:,}".format(j['Global']['NewRecovered'])


        embed = discord.Embed(title=f"Covid-19 Stats")
        embed.add_field(name="Total", value=f"Total Confirmed: `{total}`\nTotal Deaths: `{TotalD}`\nTotal Recovered: `{TotalR}`", inline=False)
        embed.add_field(name="New", value=f"New Confirmed: `{new}`\nNew Deaths: `{newD}`\nNew Recovered: `{NewR}`", inline=False)
							   


        await m.edit(embed=embed)
      except Exception as e:
        embed = discord.Embed(title=f"Error: `{e}`")
        await m.edit(embed=embed)





@client.command(aliases=["setprefix"])
async def changeprefix(ctx, *, prefix):
  if ctx.author.id == 229016449593769984 or ctx.author.id == 286591003794604034 or commands.has_permissions(manage_messages=True):
    try:
        embed = discord.Embed(
        title=f'Prefix was changed to `{prefix}` successfully.', description='' , colour=0x2f3136)

        msg = await ctx.send(embed = embed)
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)


        prefixes[str(ctx.guild.id)] = prefix

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)

    except:
        embed = discord.Embed(
        title=f'There was a error changing the prefix. ', description='' , colour=0x2f3136)

        msg = await ctx.send(embed = embed)
  else:
    await ctx.send("You need manage messages perms.")



@client.event
async def on_guild_remove(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)


    prefixes.pop(str(guild.id))

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)




@client.event
async def on_message(message):
  try:
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    e = prefixes[str(message.guild.id)]
    if message.author.bot:
        return
    if client.user in message.mentions: 
        embed = discord.Embed(
        title='', description=f'Prefix: `{e}`' , colour=discord.Colour.blurple())



        await message.channel.send(embed = embed)
  except:
    if message.author.bot:
        return
    if client.user in message.mentions: 
        embed = discord.Embed(
        title='', description=f'Prefix: `"`' , colour=discord.Colour.blurple())



        await message.channel.send(embed = embed)

    
  await client.process_commands(message)


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



@client.command()
@commands.is_owner()
async def message(ctx, member: discord.Member="", *, text=""):
  try:
    if text == "" and member == "":
      await ctx.send(f"Format: `{ctx.prefix}message @user [message]`")
    else:
      await member.send(text)
      await ctx.send(f"Message `{text}` was sent to `{member.name}#{member.discriminator}`")
  except Exception as e:
    await ctx.send(e)



extensions = env.extensions


if __name__ == '__main__':
    for ext in extensions:
        client.load_extension(ext)


client.run(env.TOKEN)