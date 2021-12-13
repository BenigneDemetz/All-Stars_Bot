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
async def startgiveaway(ctx):
    global g
    if g != None:
        try:
            await ctx.message.add_reaction("❌")
        except Exception as e:
            print('error : \n' + str(e))
        return
    g = Game(ctx.guild)

    if not functions.has_perm(ctx):
        return
    print('game start')
    embed = discord.Embed(title="A Giveaway started !", color=0x00ff00)
    await ctx.send(embed=embed)
    try:
        await ctx.delete()
    except:
        pass


@bot.command()
async def stopgiveaway(ctx):
    global g
    if g == None:
        try:
            await ctx.add_reaction("❌")
        except Exception as e:
            print('error : \n' + str(e))
        return
    await g.stop_giveaway(ctx)


@bot.event
async def on_message(ctx):
    await bot.process_commands(ctx)  # activer les commandes
    global g
    if g == None:
        return
    if commande in ctx.content:
        p: Player = Player(ctx.author)
        if g.has(p):
            await ctx.add_reaction("❌")
            time.sleep(5)
            await ctx.message.delete()
            return
        g.add_player(p, ctx)
        await ctx.add_reaction("✅")




bot.run(os.getenv('KEY_A_S'))