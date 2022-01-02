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
list_winners = []
guildid = 894350161222971392


@bot.event
async def on_ready():
    print('ready')
    with open("game.json", "r") as f:
        players = json.load(f)
    if players != {}:
        global g
        guild = await bot.fetch_guild(guildid)
        g = Game(guild, [], [], [])
        print(players.items())
        for i, j in players.items():
            member = await guild.fetch_member(i)
            p = Player(i, member, member.name, j[1], j[2], j[3])
            g.load_player(p)
            time.sleep(0.5)


@bot.command()
async def startgiveaway(ctx):
    global g
    if g != None:
        try:
            await ctx.message.add_reaction("❌")
        except Exception as e:
            print('error : \n' + str(e))
        return

    if not functions.has_perm(ctx):
        return

    g = Game(ctx.guild, [], [], [])
    print('game start')
    embed = discord.Embed(title="A Giveaway started !", color=0x00ff00)
    await ctx.send(embed=embed)
    try:
        await ctx.delete()
    except:
        pass

@bot.command()
async def reloadbot(ctx):
    pass

@bot.command()
async def loadgame(ctx):
    messages = await ctx.channel.history(limit=50).flatten()
    print(messages)
    for i in messages:
        print(i)
        if "winner" in i.content or i.content == 924429899597500417:
            return
        # await on_message(i)
        print(i.content)

@bot.command()
async def stopgiveaway(ctx, args=1):
    global g
    global list_winners
    if not functions.has_perm(ctx):
        print('e')
        return
    if g == None:
        try:
            await ctx.message.add_reaction("❌")
        except Exception as e:
            print('error : \n' + str(e))
        return
    await ctx.message.delete()
    try:
        list_winners, msg = g.stop_giveaway(ctx, args)
    except Exception as e:
        print(e.args)
    g = None
    with open("game.json", "w") as f:
        f.write("{}")
    await ctx.channel.send(msg)


@bot.command()
async def winners(ctx):
    msg = ""
    for i in list_winners:
        msg += "\n" + str(i)
        if len(msg) > 1900:
            await ctx.send(list_winners)
            msg = ""
    await ctx.send(list_winners)

@bot.command()
async def addplayer(ctx, player, address):
    player = await g.guild.fetch_member(player.replace("<@!", "").replace(">", ""))
    print(player)
    p = Player(player.id, player, player.name, 1, 0, address)
    g.add_player(p)

@bot.command()
async def listplayers(ctx):
    print(listplayers)

@bot.command()
async def sendmessage(ctx):
    msg = await g.guild.fetch_channels()
    for i in msg:
        if i.id == 894350161222971396:
            await ctx.channel.send(i.last_message.content)

@bot.event
async def on_message(ctx):
    await bot.process_commands(ctx)  # activer les commandes
    if ctx.author.bot or ctx.content.startswith("$"):
        return
    global g

    if g == None:
        return

    if commande in ctx.content:
        p = functions.create_player(ctx)
        if g.has(p):
            await ctx.add_reaction("❌")
            sayno = await ctx.channel.send("You can't participate twice")
            time.sleep(5)
            await sayno.delete()
            await ctx.delete()
            return

        g.add_player(p)
        await ctx.add_reaction("✅")


with open('key', 'r') as f:
    key = f.read()
print(key)
bot.run(key)
