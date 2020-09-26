import os, discord
from discord.utils import get, find
from discord.ext import commands

TOKEN = "NzU5MzcyNzkxNjIyNzk1Mjk0.X28jBQ.r1cArCiQRLJMmb2xdCU6Arn4_MM"
bot = commands.Bot(command_prefix="!")


#Utilities
def check_if_role(roles:list, user):
    for r in roles:
        if get(user.roles, name=r):
            return True
            


#Startup Log
@bot.event
async def on_ready():
    print("Logged on as {0}!".format(bot.user))


#Commandos
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def grup(ctx, arg):
    grups = ["Grup 1", "Grup 2", "Grup 3", "Grup 4"]
    member = ctx.message.author

    GRUP = "Grup {0}".format(arg)
    ROLE = get(member.guild.roles, name=GRUP)

    if check_if_role(grups, member):
        for _ in grups:
            r = get(member.guild.roles, name=_)
            await member.remove_roles(r)
    
    await member.add_roles(ROLE)


#Error Handling
@test.error
async def test_error(ctx, error):
    await ctx.send("<@{0.author.id}> ets puto retrassat o no saps que s'han de posar arguments als commandos?".format(ctx))


bot.run(TOKEN)

