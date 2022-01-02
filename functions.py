import json
from player import Player
import discord
from discord.ext import commands


def has_perm(ctx):
    author: discord.Member = ctx.author
    for i in author.roles:
        #            role staff                     role artist                  role dev
        if i.id == 909523163786936343 or i.id == 910606167405891634 or i.id == 911352667073286174:
            return True
    return True


def load_players():
    with open('players.json', 'r') as f:
        return json.load(f)

def create_player(ctx):
    id = ctx.author.id
    profil = ctx.author
    address = ctx.content[ctx.content.find("0x"):]
    address = address[:42]
    name = ctx.author.name

    p = Player(id, profil, name, 1, 0, address)
    return p