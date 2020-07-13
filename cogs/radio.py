from discord.ext import commands
import traceback
import datetime
import discord
import asyncio
import logger
from discord.utils import get
from discord import FFmpegPCMAudio

queuelist = []

class Radio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True, aliases=["nextlevelradio", "nextlevel", "nlradio", "nextlr", "nlevel"])
    async def nlr(self, ctx):
      try:
        embed = discord.Embed(title=f"Please wait..")
        m = await ctx.send(embed=embed)
        await asyncio.sleep(1)
        channel = ctx.message.author.voice.channel
        if not channel:
            await ctx.send("I wanted to put that before, but there's no connection to a channel.")
            return
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
        }
        voice.play(discord.FFmpegPCMAudio("https://nlradio.xyz/radio/8010/nlr.mp3?1593986701"))
        voice.volume = 100
        voice.is_playing()
        await m.delete()
        embed = discord.Embed(title=f"Now playing: `Next Level Radio`")
        await ctx.send(embed=embed)
      except Exception as e:
        embed = discord.Embed(title=f"Error: `{e}`".replace("Error: `Already playing audio.`", f"Already playing audio, type `{ctx.prefix}stop` to stop the audio"))
        await ctx.send(embed=embed)


    @commands.command(pass_context=True, aliases=['quit', 'stop'])
    async def leave(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.disconnect()
            embed = discord.Embed(title=f"I've stopped the audio and left the channel")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"I'm not in a voice channel?")
            await ctx.send(embed=embed)


    

def setup(bot):
    try:    
        bot.add_cog(Radio(bot))
        print("Loaded radio.py")
    except Exception as e:
        print(f"Error loading radio.py: {e}")