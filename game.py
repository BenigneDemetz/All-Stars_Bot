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

    def start_giveaway(self, ctx):
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