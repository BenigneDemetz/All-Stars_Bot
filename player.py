import discord
from discord.ext import commands
import functions

class Player():
    id: int
    profil: discord.Member
    participations: int
    wins = 0
    address: str

    def __init__(self):
        pass

    def create_new_player(self, ctx):
        self.id = ctx.author.id
        self.profil = ctx.author
        self.participations = 1
        address = ctx.content[ctx.content.find("0x"):]
        address = address[:42]
        self.address = address