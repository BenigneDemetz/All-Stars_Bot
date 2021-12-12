import json

import discord
from player import Player as player
import functions


class Game():
    guild: discord.Guild
    players: list[player]
    winners: list[player]

    def __init__(self, guild):
        self.guild = guild

    def __new__(self, *args, **kwargs):
        return self

    async def start_giveaway(self, ctx):
        if not functions.has_perm(ctx):
            return
        print('game start')
        embed = discord.Embed(title="A Giveaway started !", color=0x00ff00)
        await ctx.send(embed=embed)
        g = Game(ctx.guild)
        try:
            await ctx.message.delete()
        except:
            pass

    async def stop_giveaway(self, ctx):
        print('game_stop')
        pass

    def add_player(self, p: player):
        self.players.append(p)

    def has(self, p: player):
        return p in self.players

    def save_players(self):
        with open('players.json', 'w') as f:
            json.dump(self.players, f)