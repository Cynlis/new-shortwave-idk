from discord.ext import commands
import traceback
import datetime
import discord
import logger

class Radioadd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def radioadd(self, ctx, url = ""):
        if url == "":
            embed = discord.Embed(
              title='Want to add a radio station? Just do `"radioadd <url>`', description=f'')
            await ctx.send(embed = embed)
            return



        channel=self.bot.get_channel(733047365535137852)
        embed = discord.Embed(title='Radio Request', description=f'Sent by `{ctx.author.name}#{ctx.author.discriminator}`')
        embed.add_field(name='Radio URL', value=f'{url}', inline=False)
        await channel.send(embed = embed)
        embed = discord.Embed(title='Sent.', description=f'')
        await ctx.send(embed = embed)
      
        



def setup(bot):
    try:    
        bot.add_cog(Radioadd(bot))
        print("Loaded radioadd.py")
    except Exception as e:
        print(f"Error loading radioadd.py: {e}")