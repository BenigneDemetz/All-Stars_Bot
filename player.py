import discord
from discord.ext import commands
import functions


class Player():
    id: int
    profil: discord.Member
    participations: int = 1
    wins = 0
    address: str

    def __init__(self, ctx):
        self.id = ctx.author.id
        if self.id in functions.load_players():
            pass
        self.profil = ctx.author
        address = ctx.content[ctx.content.find("0x"):]
        address = address[:42]
        self.address = address

    def __new__(self, *args, **kwargs):
        return self
