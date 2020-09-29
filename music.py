import discord, os
import ffmpeg, youtube_dl
from discord.utils import get, find
from discord.ext import commands

TOKEN = os.environ.get("BOT_TOKEN") or "NzU5MzcyNzkxNjIyNzk1Mjk0.X28jBQ.r1cArCiQRLJMmb2xdCU6Arn4_MM"
bot = commands.Bot(command_prefix="!")

players = {}

#Startup Log
@bot.event
async def on_ready():
    print("Logged on as {0}!".format(bot.user))

@bot.command()
async def join(ctx):
    cnnl =  ctx.message.author.voice
    await cnnl.channel.connect()

@bot.command(pass_context=True)
async def leave(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Bot Desconectat")
    else:
        await ctx.send("El bot no esta a cap canal de veu")

@bot.command()
async def play(ctx, url):
   


bot.run(TOKEN)