from discord.ext import commands
import traceback
import datetime
import discord
import logger

class Cogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    
    extensions = ['cogs.ping', 'cogs.eval', 'cogs.cogs', 'cogs.help', "cogs.music"]
    
    @commands.group(name='reload', hidden=True, invoke_without_command=True)
    @commands.is_owner()
    async def _reload(self, ctx, *, module):
        """Reloads a module."""
        try:
            self.bot.reload_extension(module)
        except commands.ExtensionError as e:
            await ctx.send(f'{e.__class__.__name__}: {e}')
        else:
            await ctx.send('Cog reloaded')

def setup(bot):
    try:    
        bot.add_cog(Cogs(bot))
        print("Loaded cogs.py")
    except Exception as e:
        print(f"Error loading cogs.py: {e}")