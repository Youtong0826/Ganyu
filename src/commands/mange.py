import discord
from discord.ext import commands
from core.classes import Cog_ExtenSion
from command_lib import manage

class Mange(Cog_ExtenSion):

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if member != None:
            await manage.mange_member(
                ctx=ctx,
                user=ctx.author,
                member=member,
                type="kick",
                title="從這個伺服器消失了!",
                reason=reason
            )
        else:
            embed = discord.Embed(
                title="g!kick 踢除成員",
                description="用法 g!kick `提及/id/名字` `原因(可空)`"
            )

            await ctx.send(embed=embed)

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if member != None:
            await manage.mange_member(
                ctx=ctx,
                user=ctx.author,
                member=member,
                type="ban",
                title="從這個伺服器消失了!",
                reason=reason
            )
        else:
            embed = discord.Embed(
                title="g!ban 停權成員",
                description="用法 g!ban `提及/id/名字` `原因(可空)`"
            )

            await ctx.send(embed=embed)

    @commands.command()
    async def unban(self, ctx, member: discord.Member, *, reason=None):
        await manage.mange_member(
            ctx=ctx,
            user=ctx.author,
            member=member,
            type="unban",
            title="解封了!",
            reason=reason,
            CmdType="command"
        )

    @commands.command()
    async def mute(self,ctx,member:discord.Member,*,reason=None):
        await manage.mange_member(
            ctx=ctx,
            user=ctx.author,
            member=member,
            type="mute",
            title="禁言",
            reason=reason,
            CmdType="command"
        )

    @commands.command()
    async def clear(self,ctx:discord.ApplicationContext,limit:int):
        await manage.Clean(ctx,limit,"command")

    @commands.command()
    async def joinmsg(self, ctx, key = "on"):
        await ctx.send(ctx.author.guild.system_channel.name)

    @commands.command()
    async def addrole(self,ctx,member : discord.Member=None,role : discord.Role=None):
        await manage.Addrole(ctx,member,role)

def setup(bot):
    bot.add_cog(Mange(bot))