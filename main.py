import discord
from discord.ext import commands, tasks
import random
import time
import json
from player import Player as Player
from game import Game as Game
import functions

beginnerid = 910196640848158760
intermediateid = 911349839697174559
hunterid = 910196128673312779
luckyid = 911349291367432283
guildid = 909518751194550303
bot = commands.Bot("!")
commande = "0x"

g: Game = None


@bot.event
async def on_ready():
    print('ready')

@bot.command()
async def startgiveaway(ctx: commands.Context, arg = 1):
    global g
    author: discord.Member = ctx.author
    if not functions.has_perm(ctx):
        return
    if g != None:
        try:
            await ctx.add_reaction("❌")
        except Exception as e:
            print('error : \n' + str(e))
        return
    embed = discord.Embed(title="A Giveaway started !", color=0x00ff00)
    await ctx.send(embed=embed)
    g = Game(ctx.guild)
    try:
        await ctx.message.delete()
    except:
        pass

@bot.command()
async def stopgiveaway():
    global g
    pass

@bot.event
async def on_message_(ctx: commands.Context):
    global g
    if g == None:
        return
    if commande in ctx.message.content:
        p: Player = Player(ctx)
        if g.has(p):
            await ctx.add_reaction("❌")
            time.sleep(5)
            await ctx.message.delete()
            await bot.process_commands(ctx) #activer les commandes
            return
        g.add_player(p, ctx)