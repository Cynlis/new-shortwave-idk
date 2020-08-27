from discord.ext import commands
import traceback
import datetime
import requests
import json
import discord
import logger
import asyncio
import signal
from contextlib import contextmanager
import dualapi

class Radionp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    
    @commands.command(aliases=["rnp"])
    async def radionp(self, ctx, choice = ""):


        if choice == "":
            embed = discord.Embed(title=f'', description=f"", colour=0x2f3136)
            embed.add_field(name='Available Stations', value="1: `Dual`\n2: `KeyFM`\n3: `OnlyHitUS`\n4: `CloudX`", inline=False)

            m = await ctx.send(embed=embed)


        elif choice == "1":
            embed2 = discord.Embed(title=f"<a:loading:735927020508414012> Please Wait..")
            m = await ctx.send(embed=embed2)
            try:
                r = requests.get(f'https://api.dual.pw/stats')
                j = r.json()



                img = f'https://cdn.discordapp.com/attachments/747146010936999936/748266168351064204/logo-boxed.png'

                embed = discord.Embed(title=f"Dual Nowplaying", colour=0xcf6fcb)
                embed.set_thumbnail(url=f"{img}")
                embed.add_field(name="Now playing", value=f"`[ {j['now']['artist']} - {j['now']['song']} ]`", inline=False)
                embed.add_field(name="DJ", value=f"`[ {j['presenter']['username']} ]`", inline=False)
                embed.add_field(name="Song History", value=f"```py\n1 | {j['history'][0]['artist']} - {j['history'][0]['song']}\n2 | {j['history'][1]['artist']} - {j['history'][1]['song']}\n3 | {j['history'][2]['artist']} - {j['history'][2]['song']}\n```".replace("'", "").replace("\"", ""), inline=False)
                
                embed.set_footer(text=f"Listeners: {j['listeners']['current']}")

       					   


                await m.edit(embed=embed)

            except Exception as e:
                embed2 = discord.Embed(title=f"API Down")
                await m.edit(embed=embed2)
                print(e)

        elif choice == "2":
            embed2 = discord.Embed(title=f"Please Wait..")
            m = await ctx.send(embed=embed2)
            try:

                r = requests.get(f'https://keyapi.damonon.yt/stats')
                j = r.json()
                rk = requests.get(f'https://api.damonon.yt/key/stats/timetable')
                jk = rk.json()






                


                img = f'https://cdn.discordapp.com/attachments/349499975333576704/744932056051482644/square.png'

                embed = discord.Embed(title=f"KeyFM Nowplaying", colour=0x0585ff)
                embed.set_thumbnail(url=f"{img}")
                embed.add_field(name="Now playing", value=f"`[ {j['playing']['artist']} - {j['playing']['song']} ]`", inline=False)
                embed.add_field(name="DJ", value=f"`[ {jk['now']} ]`", inline=False)
                embed.set_footer(text=f"Listeners: {j['listeners']['current']}")

       					   


                await m.edit(embed=embed)
            except:
                embed2 = discord.Embed(title=f"API Down")
                await m.edit(embed=embed2)

        elif choice == "3":
            embed2 = discord.Embed(title=f"Please Wait..")
            m = await ctx.send(embed=embed2)
            try:

                r = requests.get(f'https://api.onlyhit.us/currentsong')
                j = r.text
                rk = requests.get(f'https://api.onlyhit.us/stats/total.php')
                jk = rk.text







                


                img = f'https://cdn.discordapp.com/attachments/349499975333576704/744930917222711457/TtZZoRPM.jpg'

                embed = discord.Embed(title=f"OnlyHitUS Nowplaying", colour=0xc2272d)
                embed.set_thumbnail(url=f"{img}")
                embed.add_field(name="Now playing", value=f"`[ {j} ]`", inline=False)
                embed.set_footer(text=f"Listeners: {jk}")


       					   


                await m.edit(embed=embed)
            except Exception as e:
                embed2 = discord.Embed(title=f"API Down")
                await m.edit(embed=embed2)
                print(e)
        

        elif choice == "4":
            embed2 = discord.Embed(title=f"Please Wait..")
            m = await ctx.send(embed=embed2)
            try:

                r = requests.get(f'https://panel.thisiscloudx.com/api/nowplaying')
                j = r.json()







                


                img = f'https://cdn.discordapp.com/attachments/747146010936999936/748555499242389555/Artboard_1_copy_242x.png'

                embed = discord.Embed(title=f"CloudX Nowplaying", colour=0xe056fd)
                embed.set_thumbnail(url=f"{img}")
                embed.add_field(name="Now playing", value=f"`[ {j[0]['now_playing']['song']['text']} ]`", inline=False)
                embed.set_footer(text=f"Listeners: {j[0]['listeners']['current']}")


       					   


                await m.edit(embed=embed)
            except Exception as e:
                embed2 = discord.Embed(title=f"API Down")
                await m.edit(embed=embed2)
                print(e)


       					   












            

        elif choice == "69" or choice == "420":


                img = f'https://i.redd.it/fxrnqbhjwbr21.png'

                embed = discord.Embed(title=f"")
                embed.set_image(url=f"{img}")

       					   


                await ctx.send(embed=embed)

    @commands.command(aliases=["keyvsdual", "dualvskey", "dvk"])
    async def kvd(self, ctx):
        embed2 = discord.Embed(title=f"<a:loading:735927020508414012> Please wait..")
        m = await ctx.send(embed=embed2)
        r = requests.get(f'https://keyapi.damonon.yt/stats')
        j = r.json()
        dual = dualapi.Listeners.current()
        key = j['listeners']['current']
        
        embed = discord.Embed(title=f"**KeyFM** vs **DualFM**", description=f"KeyFM has: **`{key}` Listeners**\nDualFM has: **`{dual}` Listeners**\nListener difference: **`{key - dual}`**".replace("-", ""))

        await m.edit(embed=embed)
        


    @commands.command()
    async def dual(self, ctx, type=""):
        embed2 = discord.Embed(title=f"<a:loading:735927020508414012> Please wait..")
        m = await ctx.send(embed=embed2)
        if type=="":
            embed = discord.Embed(title=f"Invalid usage", description='`"dual -l`\n`"dual -a` or `"dual -s`\n`"dual -dj` or `"dual -p`\n`"dual -v`')

            await m.edit(embed=embed)
            return

        if type=="-listeners" or type=="-l":
            embed = discord.Embed(title=f"Listeners", description=f"Current: `{dualapi.Listeners.current()}`\nPeak: `{dualapi.Listeners.peak()}`")

            await m.edit(embed=embed)
            return
 

        if type=="-song" or type=="-s" or type=="-artist" or type=="-a":
            embed = discord.Embed(title=f"Song and Artist", description=f"Artist: `{dualapi.Now.artist()}`\nSong: `{dualapi.Now.song()}`\nEncoderError?: `{dualapi.Now.encoderError()}`")

            await m.edit(embed=embed)
            return

        if type=="-dj" or type=="-d" or type=="-presenter" or type=="-p":
            embed = discord.Embed(title=f"Presenter", description=f"DJ Name: `{dualapi.Presenter.username()}`\nAutoDJ?: `{dualapi.Presenter.autodj()}`")

            await m.edit(embed=embed)
            return
        
        if type=="-v" or type=="-version":
            embed = discord.Embed(title=f"Version of DualFM", description=f"Version: `{dualapi.version()}`")

            await m.edit(embed=embed)
            return
        else:
            embed = discord.Embed(title=f"Invalid usage", description='`"dual -l`\n`"dual -a` or `"dual -s`\n`"dual -dj` or `"dual -p`\n`"dual -v`')

            await m.edit(embed=embed)
            return



            
        



def setup(bot):
    try:    
        bot.add_cog(Radionp(bot))
        print("Loaded radionp.py")
    except Exception as e:
        print(f"Error loading radionp.py: {e}")