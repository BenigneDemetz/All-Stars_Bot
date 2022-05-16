from dataclasses import dataclass, field
import discord
from discord.ext import commands


@dataclass
class Player:
    id: int
    profil: discord.Member = field(repr=False)
    name: str
    participations: int
    wins: int
    address: str

    def getAddress(self):
        return self.address

    def getProfil(self):
        return self.profil