import discord
from discord.ext import commands
import functions

class Player():
    id: int
    profil: discord.Member
    participations: int
    wins: int
    address: str

    def __init__(self, ctx: commands.Context):
        pass
