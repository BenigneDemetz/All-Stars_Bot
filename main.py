import discord
from discord.ext import commands, tasks
import random
import time
import json
from player import Player as Player
from game import Game as Game
import functions
import os

beginnerid = 910196640848158760
intermediateid = 911349839697174559
hunterid = 910196128673312779
luckyid = 911349291367432283
guildid = 909518751194550303
bot = commands.Bot("$")
commande = "0x"

g: Game = None


@bot.event
async def on_ready():
    print('ready')


@bot.command()
async def startgiveaway(ctx: commands.Context, arg=1):
    print('e')
    global g
    print(g)
    if g != None:
        try:
            await ctx.add_reaction("❌")
        except Exception as e:
            print('error : \n' + str(e))
        return
    g = Game()
    await g.start_giveaway(ctx)



bot.run(os.getenv('KEY_A_S'))