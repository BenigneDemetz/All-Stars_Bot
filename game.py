import json
import random
from dataclasses import dataclass
import discord
from player import Player as player
import functions

@dataclass
class Game():
    guild: discord.Guild
    players: list
    winners: list
    addresses: list

    def start_giveaway(self, ctx):
        pass

    def stop_giveaway(self, ctx, arg):
        i = 0
        if arg > len(self.players):
            self.winners = self.players[:]
        msg = "The winner"
        if arg > 1:
            msg += "s are "
        else:
            msg += " is "
        while i < arg:
            winner = random.randint(0, len(self.players)-1)
            self.winners.append(self.players[winner])
            msg += f'<@{self.players[winner].id}> '
            self.players.pop(winner)
            i += 1
        list_winners = []
        for i in self.winners:
            list_winners.append([i.id, i.address, i.name])
        return list_winners, ":tada: " + msg + " :tada:"

    def add_player(self, p: player):
        self.players.append(p)
        self.addresses.append(p.getAddress())
        self.save_players()

    def load_player(self, p: player):
        self.players.append(p)
        self.addresses.append(p.getAddress())

    def has(self, p):
        for i in self.players:
            if p.getAddress() == i.getAddress():
                return True
        if p.getAddress in self.players or p.getAddress() in self.addresses:
            return True
        return False

    def update_or_add_player(self, p):

        #players.json
        players = functions.load_players()
        if str(p.id) in players:
            players[str(p.id)][1] += 1
            players[str(p.id)][3] = p.address
            with open("players.json", "w") as f:
                json.dump(players, f)
            return
        players[str(p.id)] = [p.name, p.participations, p.wins, p.address]
        with open("players.json", "w") as f:
            json.dump(players, f)

    def save_players(self):

        #game.json
        liste = {}
        print(self.players)
        for i in self.players:
            liste[str(i.id)] = [i.name, i.participations, i.wins, i.address]
            self.update_or_add_player(i)
        with open("game.json", "w") as f:
            json.dump(liste, f)
