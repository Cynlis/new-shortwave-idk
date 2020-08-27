from discord.ext import commands
import traceback
import datetime
import discord
import logger
import env
from PIL import Image
from claptcha import Claptcha
import random
import string
import asyncio
from discord import Spotify
import requests



def randomString():
        rndLetters = (random.choice(string.ascii_uppercase) for _ in range(6))
        return "".join(rndLetters)


c = Claptcha(randomString, "Mom.ttf", noise=0.4)


class Cogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    
    
    @commands.group(name='reload', hidden=True, invoke_without_command=True)
    @commands.is_owner()
    async def _reload(self, ctx, *, module=""):
      extensions = env.extensions
      embed2 = discord.Embed(title=f"<a:loading:735927020508414012> Reloading Cog(s)..")
      m = await ctx.send(embed=embed2)
      if module=="":
        try:
            for ext in extensions:
              self.bot.reload_extension(ext)
        except commands.ExtensionError as e:
            embed2 = discord.Embed(title=f'{e.__class__.__name__}: {e}')
            await m.edit(embed=embed2)
        else:
            embed2 = discord.Embed(title=f"Reloaded all cogs")
            await m.edit(embed=embed2)
      else:
        try:
            self.bot.reload_extension(module)
        except commands.ExtensionError as e:
            embed2 = discord.Embed(title=f'{e.__class__.__name__}: {e}')
            await m.edit(embed=embed2)
        else:
            embed2 = discord.Embed(title=f"Cog reloaded")
            await m.edit(embed=embed2)
             
    @commands.command()
    async def captcha(self, ctx):
      try: 
        text, _ = c.write('captcha1.png')
        embed = discord.Embed(title="Here is your captcha", description="You have 1 minute to answer correctly.")
        await ctx.send(embed=embed)
        await ctx.send(file=discord. File("captcha1.png"))

        def check(message):
            return message.content == text and ctx.author.id == message.author.id

        try:
          msg = await self.bot.wait_for("message", timeout=60, check=check)
        except asyncio.TimeoutError:
            embed = discord.Embed(title=f"Ran out of time, {ctx.author.name}.", description=f"The captcha said: `{text}`", colour=0xeb4034)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"You answered correctly, {ctx.author.name}.", description=f"The captcha said: `{text}`", colour=0x40cf36)
            await ctx.send(embed=embed)

      except Exception as e:
          await ctx.send(e)

    @commands.is_owner()
    @commands.command()
    async def act(self, ctx, member:discord.Member = None):
      if not member:
        try:  
          member = member or ctx.author
          for activity in member.activities:
            if isinstance(activity, Spotify):
               embed = discord.Embed(title=f"`{member}'s` Spotify Information", colour=activity.color)
               embed.add_field(name='Song', value=f"`{activity.title}`", inline=False)
               embed.add_field(name='Artist', value=f"`{activity.artist}`", inline=False)
               embed.set_footer(text=f"Track-ID • {activity.track_id}")
               embed.set_thumbnail(url=activity.album_cover_url)
               await ctx.send(embed=embed)

        except:
              embed = discord.Embed(title=f"Error! Are you sure you're using spotify?", colour=activity.color)

              await ctx.send(embed=embed)



      if member:  
        try: 
          member = member or ctx.author
          for activity in member.activities:
            if isinstance(activity, Spotify):
               embed = discord.Embed(title=f"`{member}'s` Spotify Information", colour=activity.color)
               embed.add_field(name='Song', value=f"`{activity.title}`", inline=False)
               embed.add_field(name='Artist', value=f"`{activity.artist}`", inline=False)
               embed.set_footer(text=f"Track-ID • {activity.track_id}")
               embed.set_thumbnail(url=activity.album_cover_url)
               await ctx.send(embed=embed)


        except:
              embed = discord.Embed(title=f"Error! Try again with a member using spotify.", colour=activity.color)

              await ctx.send(embed=embed)

    @commands.command()
    async def npm(self, ctx, *, search):
        r = requests.get(f'http://npmsearch.com/query?q={search}')
        j = r.json()

        msg = j["results"][0]["name"]
        ver = j["results"][0]["version"]
        des = j["results"][0]["description"]

        embed = discord.Embed(title=f"{msg}".replace("']", "").replace("['", ""))
        embed.add_field(name='Version', value=f"`{ver}`".replace("']", "").replace("['", ""), inline=False)
        embed.add_field(name='Description', value=f"`{des}`".replace("']", "").replace("['", "").replace("``", "None"), inline=False)
        await ctx.send(embed=embed)




           


    
def setup(bot):
    try:    
        bot.add_cog(Cogs(bot))
        print("Loaded cogs.py")
    except Exception as e:
        print(f"Error loading cogs.py: {e}")