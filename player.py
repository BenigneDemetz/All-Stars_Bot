import discord
from discord.ext import commands
import functions

class Player():
    id: int
    profil: discord.Member
    participations: int
    wins = 0
    address: str

    def __init__(self, ctx: commands.Context):
        pass

    def create_new_player(self, msg):
        self.id = msg.author.id
        self.profil = msg.author
        self.participations = 1
        address = msg.content[msg.content.find("0x"):]
        print(address)
        self.address