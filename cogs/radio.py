from discord.ext import commands
import asyncio
import traceback
import discord
from discord.ext.commands import Cog
from discord.ext.commands import CheckFailure
from discord.ext.commands import command, has_permissions
import inspect
from discord.utils import get
from discord import FFmpegPCMAudio
import textwrap
import importlib
from contextlib import redirect_stdout
import io
import os
import re
import sys
import copy
import time
import subprocess
from typing import Union, Optional
import traceback
import datetime
import discord
import logger

class Radio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




    @commands.command(aliases=["radios"])
    async def radio(self, ctx, choice: str = ""):


        if choice == "":
            embed = discord.Embed(title=f'Pick a radio station!', description=f"", colour=0x2f3136)
            embed.add_field(name='Stations', value="1: `Dual`\n2: `Upbeat Radio`\n3: `KeyFM`\n4: `KissFM`\n5: `BBC One`\n6: `HeartUK`\n7: `OnlyHitUS`\n8: `CloudX`", inline=False)
            embed.set_footer(text=f"do '{ctx.prefix}radio <number>' to pick a station")

            m = await ctx.send(embed=embed)




        elif choice == "1":
            embed = discord.Embed(title=f'Selected `Dual`', description=f"", colour=0x2f3136)

            m = await ctx.send(embed=embed)


            try:
                channel = ctx.message.author.voice.channel
                voice = get(self.bot.voice_clients, guild=ctx.guild)
                if voice and voice.is_connected():
                    await voice.move_to(channel)
                else:
                    voice = await channel.connect()  

                voice.play(discord.FFmpegPCMAudio("https://radio.dual.pw/stream320.mp3"))
                embed = discord.Embed(title=f'🎵 Now Playing :', description=f"[Dual](https://dual.pw)", colour=0x2f3136)
                embed.add_field(name='Requested by', value=f"{ctx.author.mention}", inline=True)
                embed.add_field(name='Duration', value=f"`🔴 LIVE`", inline=True)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/747146010936999936/748266168351064204/logo-boxed.png")
                await m.edit(embed=embed)
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.99
                voice.is_playing()
            except Exception as e:
                embed = discord.Embed(title=f"Error: `{e}`".replace('Error: `Already playing audio.`', 'Already playing audio, type `"stop` to stop the radio.').replace("Error: `'NoneType' object has no attribute 'channel'`", "Join a voice channel."))
                await ctx.send(embed=embed)






        elif choice == "2":
            embed = discord.Embed(title=f'Selected `Upbeat Radio`', description=f"", colour=0x2f3136)

            m = await ctx.send(embed=embed)


            try:
                channel = ctx.message.author.voice.channel
                voice = get(self.bot.voice_clients, guild=ctx.guild)
                if voice and voice.is_connected():
                    await voice.move_to(channel)
                else:
                    voice = await channel.connect()  

                voice.play(discord.FFmpegPCMAudio("http://live.upbeat.pw/"))
                embed = discord.Embed(title=f'🎵 Now Playing :', description=f"[Upbeat Radio](https://upbeatradio.net/)", colour=0x2f3136)
                embed.add_field(name='Requested by', value=f"{ctx.author.mention}", inline=True)
                embed.add_field(name='Duration', value=f"`🔴 LIVE`", inline=True)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/349499975333576704/744929207460692091/favicon-96x96.png")
                await m.edit(embed=embed)
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.99
                voice.is_playing()
            except Exception as e:
                embed = discord.Embed(title=f"Error: `{e}`".replace('Error: `Already playing audio.`', 'Already playing audio, type `"stop` to stop the radio.').replace("Error: `'NoneType' object has no attribute 'channel'`", "Join a voice channel."))
                await ctx.send(embed=embed)





        elif choice == "3":
            embed = discord.Embed(title=f'Selected `KeyFM`', description=f"", colour=0x2f3136)

            m = await ctx.send(embed=embed)


            try:
                channel = ctx.message.author.voice.channel
                voice = get(self.bot.voice_clients, guild=ctx.guild)
                if voice and voice.is_connected():
                    await voice.move_to(channel)
                else:
                    voice = await channel.connect()  

                voice.play(discord.FFmpegPCMAudio("https://radio.keyfm.net/"))
                embed = discord.Embed(title=f'🎵 Now Playing :', description=f"[KeyFM](https://keyfm.net/)", colour=0x2f3136)
                embed.add_field(name='Requested by', value=f"{ctx.author.mention}", inline=True)
                embed.add_field(name='Duration', value=f"`🔴 LIVE`", inline=True)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/349499975333576704/744932056051482644/square.png")
                await m.edit(embed=embed)
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.99
                voice.is_playing()
            except Exception as e:
                embed = discord.Embed(title=f"Error: `{e}`".replace('Error: `Already playing audio.`', 'Already playing audio, type `"stop` to stop the radio.').replace("Error: `'NoneType' object has no attribute 'channel'`", "Join a voice channel."))
                await ctx.send(embed=embed)


        elif choice == "4":
            embed = discord.Embed(title=f'Selected `KissFM`', description=f"", colour=0x2f3136)

            m = await ctx.send(embed=embed)


            try:
                channel = ctx.message.author.voice.channel
                voice = get(self.bot.voice_clients, guild=ctx.guild)
                if voice and voice.is_connected():
                    await voice.move_to(channel)
                else:
                    voice = await channel.connect()  

                voice.play(discord.FFmpegPCMAudio("https://stream-kiss.planetradio.co.uk/kissfresh.mp3?direct=true"))
                embed = discord.Embed(title=f'🎵 Now Playing :', description=f"[Upbeat Radio](https://upbeatradio.net/)", colour=0x2f3136)
                embed.add_field(name='Requested by', value=f"{ctx.author.mention}", inline=True)
                embed.add_field(name='Duration', value=f"`🔴 LIVE`", inline=True)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/349499975333576704/744929615130263561/c175.png")
                await m.edit(embed=embed)
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.99
                voice.is_playing()
            except Exception as e:
                embed = discord.Embed(title=f"Error: `{e}`".replace('Error: `Already playing audio.`', 'Already playing audio, type `"stop` to stop the radio.').replace("Error: `'NoneType' object has no attribute 'channel'`", "Join a voice channel."))
                await ctx.send(embed=embed)

            
        elif choice == "5":
            embed = discord.Embed(title=f'Selected `BBC One`', description=f"", colour=0x2f3136)

            m = await ctx.send(embed=embed)


            try:
                channel = ctx.message.author.voice.channel
                voice = get(self.bot.voice_clients, guild=ctx.guild)
                if voice and voice.is_connected():
                    await voice.move_to(channel)
                else:
                    voice = await channel.connect()  

                voice.play(discord.FFmpegPCMAudio("http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1_mf_p"))
                embed = discord.Embed(title=f'🎵 Now Playing :', description=f"[BBC One](https://www.bbc.co.uk/sounds/play/live:bbc_radio_one)", colour=0x2f3136)
                embed.add_field(name='Requested by', value=f"{ctx.author.mention}", inline=True)
                embed.add_field(name='Duration', value=f"`🔴 LIVE`", inline=True)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/349499975333576704/744930191616507904/Zy2vTRSq_400x400.jpg")
                await m.edit(embed=embed)
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.99
                voice.is_playing()
            except Exception as e:
                embed = discord.Embed(title=f"Error: `{e}`".replace('Error: `Already playing audio.`', 'Already playing audio, type `"stop` to stop the radio.').replace("Error: `'NoneType' object has no attribute 'channel'`", "Join a voice channel."))
                await ctx.send(embed=embed)

        elif choice == "6":
            embed = discord.Embed(title=f'Selected `HeartUK`', description=f"", colour=0x2f3136)

            m = await ctx.send(embed=embed)


            try:
                channel = ctx.message.author.voice.channel
                voice = get(self.bot.voice_clients, guild=ctx.guild)
                if voice and voice.is_connected():
                    await voice.move_to(channel)
                else:
                    voice = await channel.connect()  

                voice.play(discord.FFmpegPCMAudio("https://media-ssl.musicradio.com/HeartUK"))
                embed = discord.Embed(title=f'🎵 Now Playing :', description=f"[HeartUK](https://www.heart.co.uk/)", colour=0x2f3136)
                embed.add_field(name='Requested by', value=f"{ctx.author.mention}", inline=True)
                embed.add_field(name='Duration', value=f"`🔴 LIVE`", inline=True)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/349499975333576704/744930638330593370/unnamed.png")
                await m.edit(embed=embed)
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.99
                voice.is_playing()
            except Exception as e:
                embed = discord.Embed(title=f"Error: `{e}`".replace('Error: `Already playing audio.`', 'Already playing audio, type `"stop` to stop the radio.').replace("Error: `'NoneType' object has no attribute 'channel'`", "Join a voice channel."))
                await ctx.send(embed=embed)


        elif choice == "7":
            embed = discord.Embed(title=f'Selected `OnlyHitUS`', description=f"", colour=0x2f3136)

            m = await ctx.send(embed=embed)


            try:
                channel = ctx.message.author.voice.channel
                voice = get(self.bot.voice_clients, guild=ctx.guild)
                if voice and voice.is_connected():
                    await voice.move_to(channel)
                else:
                    voice = await channel.connect()  

                voice.play(discord.FFmpegPCMAudio("https://api.onlyhit.us/play"))
                embed = discord.Embed(title=f'🎵 Now Playing :', description=f"[OnlyHitUS](https://onlyhit.us/)", colour=0x2f3136)
                embed.add_field(name='Requested by', value=f"{ctx.author.mention}", inline=True)
                embed.add_field(name='Duration', value=f"`🔴 LIVE`", inline=True)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/349499975333576704/744930917222711457/TtZZoRPM.jpg")
                await m.edit(embed=embed)
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.99
                voice.is_playing()
            except Exception as e:
                embed = discord.Embed(title=f"Error: `{e}`".replace('Error: `Already playing audio.`', 'Already playing audio, type `"stop` to stop the radio.').replace("Error: `'NoneType' object has no attribute 'channel'`", "Join a voice channel."))
                await ctx.send(embed=embed)

        elif choice == "8":
            embed = discord.Embed(title=f'Selected `CloudX`', description=f"", colour=0x2f3136)

            m = await ctx.send(embed=embed)


            try:
                channel = ctx.message.author.voice.channel
                voice = get(self.bot.voice_clients, guild=ctx.guild)
                if voice and voice.is_connected():
                    await voice.move_to(channel)
                else:
                    voice = await channel.connect()  

                voice.play(discord.FFmpegPCMAudio("https://panel.thisiscloudx.com/radio/8000/radio.mp3"))
                embed = discord.Embed(title=f'🎵 Now Playing :', description=f"[CloudX](https://thisiscloudx.com/)", colour=0x2f3136)
                embed.add_field(name='Requested by', value=f"{ctx.author.mention}", inline=True)
                embed.add_field(name='Duration', value=f"`🔴 LIVE`", inline=True)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/747146010936999936/748555499242389555/Artboard_1_copy_242x.png")
                await m.edit(embed=embed)
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.99
                voice.is_playing()
            except Exception as e:
                embed = discord.Embed(title=f"Error: `{e}`".replace('Error: `Already playing audio.`', 'Already playing audio, type `"stop` to stop the radio.').replace("Error: `'NoneType' object has no attribute 'channel'`", "Join a voice channel."))
                await ctx.send(embed=embed)


        elif choice == "9":
            embed = discord.Embed(title=f'Selected `Truck Stop Radio`', description=f"", colour=0x2f3136)

            m = await ctx.send(embed=embed)


            try:
                channel = ctx.message.author.voice.channel
                voice = get(self.bot.voice_clients, guild=ctx.guild)
                if voice and voice.is_connected():
                    await voice.move_to(channel)
                else:
                    voice = await channel.connect()  

                voice.play(discord.FFmpegPCMAudio("https://truckstopradio.radioca.st/stream"))
                embed = discord.Embed(title=f'🎵 Now Playing :', description=f"[Truck Stop Radio](https://truckstopradio.co.uk/)", colour=0x2f3136)
                embed.add_field(name='Requested by', value=f"{ctx.author.mention}", inline=True)
                embed.add_field(name='Duration', value=f"`🔴 LIVE`", inline=True)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/747146010936999936/748582130619252936/unknown-album.png")
                await m.edit(embed=embed)
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.99
                voice.is_playing()
            except Exception as e:
                embed = discord.Embed(title=f"Error: `{e}`".replace('Error: `Already playing audio.`', 'Already playing audio, type `"stop` to stop the radio.').replace("Error: `'NoneType' object has no attribute 'channel'`", "Join a voice channel."))
                await ctx.send(embed=embed)






    @commands.command(pass_context=True, aliases=['v', 'vol'])
    async def volume(self, ctx, volume: int):
    
        if ctx.voice_client is None:
            return await ctx.send("Not connected to voice channel")


        print(volume/100)

        ctx.voice_client.source.volume = volume / 100
        await ctx.send(f"Changed volume to {volume}%")
    
    @commands.is_owner()
    @commands.command()
    async def news(self, ctx):
            embed = discord.Embed(title=f'Please wait..', description=f"", colour=0x2f3136)

            m = await ctx.send(embed=embed)


            try:
                channel = ctx.message.author.voice.channel
                voice = get(self.bot.voice_clients, guild=ctx.guild)
                if voice and voice.is_connected():
                    await voice.move_to(channel)
                else:
                    voice = await channel.connect()  

                voice.play(discord.FFmpegPCMAudio("https://video.news.sky.com/snr/news/snrnews.mp3"))
                embed = discord.Embed(title=f'🎵 Now Playing :', description=f"Sky News Radio", colour=0x2f3136)

                await m.edit(embed=embed)
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.99
                voice.is_playing()
                await asyncio.sleep(140)
                await voice.disconnect()
                await m.delete()
            except Exception as e:
                embed = discord.Embed(title=f"Error: `{e}`".replace('Error: `Already playing audio.`', 'Already playing audio, type `"stop` to stop the news.').replace("Error: `'NoneType' object has no attribute 'channel'`", "Join a voice channel."))
                await ctx.send(embed=embed)


        

        



        

        











def setup(bot):
    try:    
        bot.add_cog(Radio(bot))
        print("Loaded radio.py")
    except Exception as e:
        print(f"Error loading radio.py: {e}")