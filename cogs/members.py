from discord.ext import commands
import traceback
import datetime
import discord
import logger

class Members(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['members'])
    async def membercount(self, ctx):
        await ctx.send(embed=discord.Embed(
            color=0x2f3136
        ).set_author(
            name=ctx.guild.name,
            icon_url=str(ctx.guild.icon_url)
        ).add_field(
            name='Total',
            value=format(len(ctx.guild.members), ',d'),
            inline=False
        ).add_field(
            name='Humans',
            value=format(len([m for m in ctx.guild.members if not m.bot]), ',d'),
            inline=False
        ).add_field(
            name='Bots',
            value=format(len([m for m in ctx.guild.members if m.bot]), ',d'),
            inline=False
        ))


    



        


def setup(bot):
    try:    
        bot.add_cog(Members(bot))
        print("Loaded members.py")
    except Exception as e:
        print(f"Error loading members.py: {e}")