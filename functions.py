import discord
from discord.ext import commands


def has_perm(ctx: commands.Context):
    author: discord.Member = ctx.author
    for i in author.roles:
        #            role staff                     role artist                  role dev
        if i.id == 909523163786936343 or i.id == 910606167405891634 or i.id == 911352667073286174:
            return True
    return False
