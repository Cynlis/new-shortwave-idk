from discord.ext import commands
import traceback
import datetime
import discord
import logger
import requests

class Shortener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def graph(self, ctx, option=""):
      embed = discord.Embed(title=f'<a:loading:735927020508414012> Please Wait...', description=f"", colour=0x2f3136)
      m = await ctx.send(embed=embed)
      try:
          if option == "":
            embed = discord.Embed(title=f'Please choose.', description=f"`graph members`\n`graph guilds`", colour=0x2f3136)
            await m.edit(embed=embed)
          if option == "members":
            embed = discord.Embed(title=f'', description=f"", colour=0x2f3136)
            embed.set_image(url="https://quickchart.io/chart?bkg=white&c={type:%27bar%27,data:{labels:['Members'],datasets:[{label:%27Users%27,data:["+ f"{len(self.bot.users)}" +"]}]}}")
            await m.edit(embed=embed)
          if option == "guilds":
            embed = discord.Embed(title=f'', description=f"", colour=0x2f3136)
            embed.set_image(url="https://quickchart.io/chart?bkg=white&c={type:%27bar%27,data:{labels:['Guilds'],datasets:[{label:%27Users%27,data:["+ f"{len(self.bot.guilds)}" +"]}]}}")
            await m.edit(embed=embed)
      except Exception as e:
            embed = discord.Embed(title=f'', description=f"Error", colour=0x2f3136)
            await m.edit(embed=embed)
            print(e)




def setup(bot):
    try:
        bot.add_cog(Shortener(bot))
        print("Loaded shortener.py")
    except Exception as e:
        print(f"Error loading shortener.py: {e}")