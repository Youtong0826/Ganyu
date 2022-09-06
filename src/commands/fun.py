from core.classes import CogExtension
from discord.ext import commands
from command_lib import fun
import discord

class Fun(CogExtension):

    @commands.command()
    async def dice(self, ctx, number: int = None):
        await fun.dice(number,ctx)

    @commands.command()
    async def mora(self,ctx):
        await fun.mora(ctx)

    @commands.command()
    async def luck(self,ctx , member:discord.Member = None):
        await fun.luck(ctx,member)

    @commands.command()
    async def spank(self, ctx, member:discord.Member = None):
        await fun.spank(ctx,member,)

    @commands.command()
    async def gay(self,ctx,member:discord.Member = None):
        await fun.gay(ctx,member)

def setup(bot):
    bot.add_cog(Fun(bot))