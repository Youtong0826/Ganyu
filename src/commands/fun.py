from core.classes import Cog_ExtenSion
from discord.ext import commands
from command_lib import fun
import discord

class Fun(Cog_ExtenSion):

    @commands.command()
    async def dice(self, ctx, number: int = None):
        await fun.Dice(number,ctx,"command")

    @commands.command()
    async def mora(self,ctx):
        await fun.Mora(ctx,"command")

    @commands.command()
    async def luck(self,ctx , member:discord.Member = None):
        await fun.Luck(ctx,member,"command")

    @commands.command()
    async def spank(self, ctx, member:discord.Member = None):
        await fun.Spank(ctx,member,"command")

def setup(bot):
    bot.add_cog(Fun(bot))