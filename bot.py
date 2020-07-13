import discord
import env
from discord.ext import commands


client = commands.Bot(command_prefix='.', case_insensitive=True)


@client.event
async def on_ready():
    print("Bot is ready!")

@client.command()
async def restart(ctx):
    embed = discord.Embed(
      title='Reloading commands', description='This can take 6 seconds or more', colour=random.randint(0, 0xFFFFFF))
  
    m = await ctx.send(embed=embed)
    os.system("python run.py")
    
    time.sleep(0.2) # 200ms to CTR+C twice

@client.command()
async def ping(ctx):
    await ctx.send(f"{len(client.latency * 1000)}")

client.run(env.TOKEN)