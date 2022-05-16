import discord
from discord.ext import commands, tasks
import random
import time
import json
from player import Player as Player
from game import Game as Game
import functions
import os
import threading
import datetime

beginnerid = 910196640848158760
intermediateid = 911349839697174559
hunterid = 910196128673312779
luckyid = 911349291367432283
guildid = 909518751194550303
bot = commands.Bot("$")
commande = "0x"
g: Game = None
list_winners = []
with open("data.json", "r") as f:
    data = json.load(f)
    invitesneeded = data[0]
sleepingmessage = []
onvoice = {}
# guildid = 909518751194550303


@bot.event
async def on_ready():
    global allstars
    print('ready')
    for i in bot.guilds:
        print(i)

    global invites
    try:
        # Getting all the guilds our bot is in
        for guild in bot.guilds:
            print(guild)
        # Adding each guild's invites to our dict
            invites[guild.id] = await guild.invites()
    except Exception as e:
        print("error invites", e.args)

    guild = await bot.fetch_guild(guildid)
    allstars = guild
    with open("game.json", "r") as f:
        players = json.load(f)
    print(guild)
    languechann = None
    channels = await guild.fetch_channels()
    # for i in channels:
    #    if i.id == 950792679220985926:
    #        languechann = i
    # await languechann.send(embed=discord.Embed(title="__**International Channels**__", color=discord.Color.blue(), description="**Select your language by reacting with one of the following emojis:**\n:flag_fr: - French\n:flag_es: - Spanish\n:flag_de: - German\n :flag_id: - Indonesian\n:flag_it: - Italian\n:flag_pt: - Portuguese\n:flag_tr: - Turkish"))
    # create language role pick
    if players != {}:
        global g
        g = Game(guild, [], [], [])
        print('Loading . . .')
        for i in players:
            try:
                member = await guild.fetch_member(i)
                p = Player(i, member, member.name, players[i][1], players[i][2], players[i][3])
                g.load_player(p)
                time.sleep(0.5)
            except Exception as e:
                print(e.args)
        print(g)
        print('Done !')


@bot.event
async def on_raw_reaction_remove(reac):
    print(type(reac))
    if reac.message_id == 948215726345441380:
        try:
            global allstars
            role = allstars.get_role(960942978841579600)
            member = await allstars.fetch_member(reac.user_id)
            await member.remove_roles(role)
        except Exception as e:
            print(e.args)
    if reac.message_id == 953361422056841226:
        allstars = bot.get_guild(909518751194550303)
        member = await allstars.fetch_member(reac.user_id)
        if '🇫🇷' in reac.emoji.name:
            role = allstars.get_role(954044129204117544)
            await member.remove_roles(role)
        if '🇪🇸' in reac.emoji.name:
            role = allstars.get_role(954044459031625810)
            await member.remove_roles(role)
        if '🇩🇪' in reac.emoji.name:
            role = allstars.get_role(954044597082947584)
            await member.remove_roles(role)
        if '🇮🇩' in reac.emoji.name:
            role = allstars.get_role(954044664003059712)
            await member.remove_roles(role)
        if '🇮🇹' in reac.emoji.name:
            role = allstars.get_role(954044846950187008)
            await member.remove_roles(role)
        if '🇵🇹' in reac.emoji.name:
            role = allstars.get_role(954044957868556350)
            await member.remove_roles(role)
        if '🇹🇷' in reac.emoji.name:
            role = allstars.get_role(954044996460380210)
            await member.remove_roles(role)


@bot.event
async def on_raw_reaction_add(reac):
    print(type(reac))
    if reac.message_id == 948215726345441380:
        try:
            role = reac.member.guild.get_role(960942978841579600)
            await reac.member.add_roles(role)
        except Exception as e:
            print(e.args)
    if reac.message_id == 953361422056841226:

        guild = bot.get_guild(909518751194550303)
        channel = guild.get_channel(948215110990716968)
        # print(channel)
        # histo = await channel.history(limit=1).flatten()
        # role = guild.get_role(948209795851247677)
        # for j in histo:
        #    for i in j.reactions:
        #        for k in await i.users().flatten():
        #            try:
        #                print(k, k.id)
        #                userr = await guild.fetch_member(k.id)
        #                print(userr)
        #                time.sleep(0.5)
        #                await k.add_roles(userr)
        #            except:
        #                pass
        #        try:
        #            print('e')
        #            await j.add_reaction(i)
        #        except Exception as e:
        #            print(e.args)
        print(reac.emoji.name)
        if '🇫🇷' in reac.emoji.name:
            role = reac.member.guild.get_role(954044129204117544)
            await reac.member.add_roles(role)
        if '🇪🇸' in reac.emoji.name:
            role = reac.member.guild.get_role(954044459031625810)
            await reac.member.add_roles(role)
        if '🇩🇪' in reac.emoji.name:
            role = reac.member.guild.get_role(954044597082947584)
            await reac.member.add_roles(role)
        if '🇮🇩' in reac.emoji.name:
            role = reac.member.guild.get_role(954044664003059712)
            await reac.member.add_roles(role)
        if '🇮🇹' in reac.emoji.name:
            role = reac.member.guild.get_role(954044846950187008)
            await reac.member.add_roles(role)
        if '🇵🇹' in reac.emoji.name:
            role = reac.member.guild.get_role(954044957868556350)
            await reac.member.add_roles(role)
        if '🇹🇷' in reac.emoji.name:
            role = reac.member.guild.get_role(954044996460380210)
            await reac.member.add_roles(role)


@bot.event
async def on_guild_channel_update(before, after):
    if "ticket" in before.name and "closed" in after.name:
        category = discord.utils.get(after.guild.categories, name="Closed tickets")
        print(category)
        await after.move(end=True, category=category)


@bot.event
async def on_member_join(member):
    #if member.joined_at
    pass


@bot.command()
async def reorder_closed_tickets(ctx):
    guild = ctx.guild
    cat = discord.utils.get(guild.categories, name="Closed tickets")
    liste = cat.channels
    names = []
    for i in liste:
        names.append(i.name)
    names.sort()
    names.reverse()
    for i in names:
        channel = discord.utils.get(guild.channels, name=i)
        await channel.move(beginning=True, category=cat)
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

def find_invite_by_code(invite_list, code):
    
    # Simply looping through each invite in an
    # invite list which we will get using guild.invites()
    
    for inv in invite_list:
        
        # Check if the invite code in this element
        # of the list is the one we're looking for
        
        if inv.code == code:
            
            # If it is, we return it.
            
            return inv

@bot.event
async def on_member_remove(member):
    
    # Updates the cache when a user leaves to make sure
    # everything is up to date
    
    invites[member.guild.id] = await member.guild.invites()

@bot.event
async def on_member_join(member):

    # Getting the invites before the user joining
    # from our cache for this specific guild

    invites_before_join = invites[member.guild.id]

    # Getting the invites after the user joining
    # so we can compare it with the first one, and
    # see which invite uses number increased

    invites_after_join = await member.guild.invites()

    # Loops for each invite we have for the guild
    # the user joined.

    for invite in invites_before_join:

        # Now, we're using the function we created just
        # before to check which invite count is bigger
        # than it was before the user joined.
        
        if invite.uses < find_invite_by_code(invites_after_join, invite.code).uses:
            
            # Now that we found which link was used,
            # we will print a couple things in our console:
            # the name, invite code used the the person
            # who created the invite code, or the inviter.
            print("Member {member.name} Joined\nInvite Code: {invite.code}\nInviter: {invite.inviter}")
            chann = await bot.fetch_channel(968260753733853265)
            await chann.send("Member {member.name} Joined\nInvite Code: {invite.code}\nInviter: {invite.inviter}")
            
            # We will now update our cache so it's ready
            # for the next user that joins the guild

            invites[member.guild.id] = invites_after_join
            
            # We return here since we already found which 
            # one was used and there is no point in
            # looping when we already got what we wanted
            return

@bot.command()
async def invites(ctx, usr: discord.Member = None):
    if usr == None:
        user = ctx.author
    else:
        user = usr
    total_invites = 0
    for i in await ctx.guild.invites():
        if i.inviter == user:
            total_invites += i.uses
    await ctx.send(f"{user.name} has invited {total_invites} member{'' if total_invites == 1 else 's'} !")


@bot.command()
async def privategiveaway(ctx, arg):
    global invitesneeded
    invitesneeded = arg
    global data
    data[0] = arg
    with open("data.json", "w") as f:
        json.dump(data, f)


@bot.command()
async def debuge(ctx):
    print(ctx.author.created_at)
    print((datetime.datetime.now()-ctx.author.created_at).days)
    return
    msg = await bot.fetch_channel(909526463798202369)
    msg = await msg.history(limit=22).flatten()
    for i in msg:
        player = i.author
        print(player)
        p = Player(player.id, player, player.name, 1, 0, i.content)
        g.add_player(p)
    g.save_players()
    return
    stars = 910196640848158760
    superstars = 911349291367432283
    ultrastars = 910196128673312779

    with open("players.json", "r") as f:
        liste = json.load(f)
    guild = await bot.fetch_guild(guildid)
    roles = await guild.fetch_roles()
    for j in roles:
        if j.id == stars:
            stars = j
        if j.id == superstars:
            superstars = j
        if j.id == ultrastars:
            ultrastars = j
    for i in liste:
        try:
            print(i, liste[i][0], liste[i][2])
            member = await guild.fetch_member(i)
            time.sleep(0.5)
            if liste[i][2] >= 10:
                print('10 win')
                try:
                    await member.add_roles(ultrastars)
                except Exception as e:
                    print(e.args)
                try:
                    await member.remove_roles(superstars, stars)
                except Exception as e:
                    print(e.args)
            elif liste[i][2] >= 5:
                print('5 win')
                try:
                    await member.add_roles(superstars)
                except Exception as e:
                    print(e.args)
                try:
                    await member.remove_roles(stars)
                except Exception as e:
                    print(e.args)
            elif liste[i][2] >= 1:
                print('1 win')
                try:
                    await member.add_roles(stars)
                except Exception as e:
                    print(e.args)
        except Exception as e:
            print(e.args)


@bot.command()
async def stopgiveaway(ctx, args=1):
    global g
    global list_winners
    if not functions.has_perm(ctx):
        print('e')
        return
    try:
        guild = await bot.fetch_guild(guildid)
        chann: discord.TextChannel = await bot.fetch_channel(909526463798202369)
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        overwrite.read_messages = True
        for i in guild.members:
            await chann.set_permissions(i, overwrite=overwrite)
    except:
        pass
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
            await ctx.send(msg)
            msg = ""
    await ctx.send(msg)


@bot.command()
async def addplayer(ctx, player, address):
    player = await g.guild.fetch_member(player.replace("<@", "").replace(">", ""))
    print(player)
    p = Player(player.id, player, player.name, 1, 0, address)
    g.add_player(p)


@bot.command()
async def listplayers(ctx):
    msg = ""
    for i in g.players:
        msg += "\n" + str(i.name) + " : " + str(i.address) + " - **" + str(i.participations) + "** - **" + str(
            i.wins) + "**"
        if len(msg) > 1500:
            await ctx.send(msg)
            msg = ""
    await ctx.send(msg)


@bot.command()
async def sendmessage(ctx):
    msg = await bot.fetch_channel(923587019614081154)
    msg = await msg.history(limit=1).flatten()
    print(msg)
    await ctx.channel.send(msg[0].content)


@bot.command()
async def setmoney(ctx, member, money):
    with open("xp.json", "r") as f:
            users = json.load(f)
    users[member.replace("<@!", "").replace(">", "")] = int(money)
    with open("xp.json", "w") as f:
        json.dump(users, f)
    await ctx.message.add_reaction("✅")


@bot.command()
async def addmoney(ctx, member, money):
    with open("xp.json", "r") as f:
            users = json.load(f)
    users[member.replace("<@!", "").replace(">", "")] += int(money)
    with open("xp.json", "w") as f:
        json.dump(users, f)
    await ctx.message.add_reaction("✅")


@bot.command()
async def delmoney(ctx, member, money):
    with open("xp.json", "r") as f:
            users = json.load(f)
    users[member.replace("<@!", "").replace(">", "")] -= int(money)
    with open("xp.json", "w") as f:
        json.dump(users, f)
    await ctx.message.add_reaction("✅")


@bot.command()
async def money(ctx, member=None):
    with open("xp.json", "r") as f:
            users = json.load(f)
    print(users)
    if member != None:
        id = member.replace("<@!", "").replace(">", "")
        member = await ctx.guild.fetch_member(int(id))
        print(member)
        if str(id) not in users:
            await ctx.channel.send(member.nick + " doesn't have any nanoCoins")
            return
        if member.nick == None:
            member.nick = member.name
        await ctx.channel.send(member.nick + " has got " + str(users[str(member.id)]) + " nanoCoins")
        return
    if str(ctx.author.id) not in users:
        await ctx.channel.send("You don't have any nanoCoins")
        return
    await ctx.channel.send("You've got " + str(users[str(ctx.author.id)]) + " nanoCoins")


@bot.event
async def on_voice_state_update(member, before, after):
    print(member)
    print(before)
    print(after)
    global onvoice
    if (before.channel == None or before.channel == 909903819423510579) and after.channel != before.channel and after.channel != None:
        onvoice[member.id] = datetime.datetime.now()
    if before.channel != None and after.channel != before.channel and (after.channel == None or after.channel.id == 909903819423510579):
        onvoice[member.id] = datetime.datetime.now() - onvoice[member.id]
        onvoice[member.id] = onvoice[member.id].total_seconds()
        timeonvoc = onvoice[member.id]/(60*2)
        print(timeonvoc)

        users = {}
        with open("xp.json", "r") as f:
            users = json.load(f)
        if str(member.id) not in users:
            users[str(member.id)] = 0
        users[str(member.id)] += int(timeonvoc)
        print(users)
        with open("xp.json", "w") as f:
            json.dump(users, f)


def sleep5snd(author):
    global sleepingmessage
    sleepingmessage.remove(author)


async def xp(ctx):
    users = {}
    global sleepingmessage
    if ctx.author.id in sleepingmessage:
        return
    sleepingmessage.append(ctx.author.id)
    with open("xp.json", "r") as f:
        users = json.load(f)
    if str(ctx.author.id) not in users:
        users[str(ctx.author.id)] = 0
    users[str(ctx.author.id)] += 1
    print(users)
    print(sleepingmessage)
    with open("xp.json", "w") as f:
        json.dump(users, f)
    print("thread")
    fiveseconds = threading.Timer(10, sleep5snd, args=[ctx.author.id])
    fiveseconds.start()


@bot.event
async def on_message(ctx):
    await bot.process_commands(ctx)  # activer les commandes

    if ctx.author.bot or ctx.content.startswith("$"):
        return
    # turkish             portugues            italiano            indonesian          deutsh                    spanish         french                      chat        trading chat      premium chat
    listechannelstotalk = [948664587824300052, 948569568329203742, 948569445360615424, 948569326074617886,
                           948569168674971659, 948568981919391764, 948568253838549073, 909518751819513939,
                           942097767470354493, 922441936634253342, 913072436713496627]
    if (ctx.channel.id in listechannelstotalk or ctx.channel.id == 957735832112992326) and "discord.gg" in ctx.content:
        await ctx.delete()
        return
    try:
        if ctx.channel.id in listechannelstotalk and not ctx.content.startswith("$"):
            await xp(ctx)
    except Exception as e:
        print(e.args)
    if ctx.channel.id in listechannelstotalk:
        users = {}
        with open("chating.json", "r") as f:
            users = json.load(f)
        if str(ctx.author.id) not in users:
            users[str(ctx.author.id)] = 0
        users[str(ctx.author.id)] += 1
        with open("chating.json", "w") as f:
            json.dump(users, f)
        print(users)
        if users[str(ctx.author.id)] == 30:
            try:
                guild = bot.get_guild(909518751194550303)
                role = guild.get_role(954011898880331818)
                await ctx.author.add_roles(role)
            except:
                pass
    #if ctx.author.bot or ctx.content.startswith("$"):
    #    return
    global g

    if g == None:
        return

    if commande in ctx.content and ctx.channel.id == 909526463798202369:
        user = ctx.author
        total_invites = 0
        for i in await ctx.guild.invites():
            if i.inviter == user:
                total_invites += i.uses
        try:
            global invitesneeded
            if total_invites < int(invitesneeded):
                await ctx.add_reaction("❌")
                sayno = await ctx.channel.send(
                    "You haven't invited enough people, you need **" + str(invitesneeded) + " invitations** !")
                time.sleep(10)
                await sayno.delete()
                await ctx.delete()
                return

            p = functions.create_player(ctx)

            if g.has(p):
                await ctx.add_reaction("❌")
                sayno = await ctx.channel.send("You can't participate **twice**")
                time.sleep(10)
                await sayno.delete()
                await ctx.delete()
                return
        except Exception as e:
            print(e.args)

        g.add_player(p)
        await ctx.add_reaction("✅")


with open('key', 'r') as f:
    key = f.read()
print(key)
bot.run(key)
