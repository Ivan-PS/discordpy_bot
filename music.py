import discord, os, youtube_dl
#import ffmpeg, youtube_dl 
from discord.utils import get, find
from discord.ext import commands

TOKEN = os.environ.get("BOT_TOKEN") or "NzU5MzcyNzkxNjIyNzk1Mjk0.X28jBQ.r1cArCiQRLJMmb2xdCU6Arn4_MM"
bot = commands.Bot(command_prefix="!")

players = {}


def search_url(text):
    with youtube_dl.YoutubeDL() as ydl:
        info = ydl.extract_info("ytsearch:{0}".format(text), download=False)
    return info['entries'][0]['webpage_url']


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
async def play(ctx, arg):
    url = search_url(arg)
    await ctx.send("En breus es reproduira: {0}".format(url))

    song_there = os.path.isfile("song.mp3")

    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music end or use the 'stop' command")
        return



    voice = get(bot.voice_clients, guild=ctx.guild)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print(arg + " >>>>>> " + url)
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, 'song.mp3')

    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    voice.volume = 100
    voice.is_playing()
   


bot.run(TOKEN)