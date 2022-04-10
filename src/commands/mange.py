import discord
import datetime
from discord.ext import commands
from core.classes import Cog_ExtenSion

class Mange(Cog_ExtenSion):

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):

        if ctx.author.guild_permissions.kick_members:
            embed = discord.Embed(
                title=f"{member.name} 從這個伺服器消失了!",
                description=f"{member.mention} 遭到 {ctx.author.mention} 使用 `kick` 指令踢出了",
                color=0xff2e2e,
                timestamp=datetime.datetime.utcnow()
            )

            if reason == None:
                reason = "無"

            embed.add_field(
                name="Reason", value=f"```{reason}```"
            )

            embed.set_footer(text=f"{ctx.author.name}",
                             icon_url=ctx.author.avatar)
            await member.kick(reason=reason)

        else:
            embed = discord.Embed(
                title="你沒有權限!",
                description=f"缺少權限 `kick_members` `踢出成員`",
                color=0xff2e2e,
                timestamp=datetime.datetime.utcnow()
            )
            embed.set_footer(text=f"{ctx.author.name}",
                             icon_url=ctx.author.avatar)

        await ctx.send(embed=embed)
        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):

        if ctx.author.guild_permissions.ban_members:
            embed = discord.Embed(
                title=f"{member.name} 從這個伺服器消失了!",
                description=f"{member.mention} 遭到 {ctx.author.mention} 使用 `ban` 指令踢除了",
                color=0xff2e2e,
                timestamp=datetime.datetime.utcnow()
            )

            if reason == None:
                reason = "無"

            embed.add_field(
                name="Reason", value=f"```{reason}```"
            )

            embed.set_footer(text=f"{ctx.author.name}",
                             icon_url=ctx.author.avatar)
            await member.ban(reason=reason)
        else:
            embed = discord.Embed(
                title="你沒有權限!",
                description=f"缺少權限 `ban_members` `對成員停權`",
                color=0xff2e2e,
                timestamp=datetime.datetime.utcnow()
            )
            embed.set_footer(text=f"{ctx.author.name}",
                             icon_url=ctx.author.avatar)

        await ctx.send(embed=embed)

        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")


def setup(bot):
    bot.add_cog(Mange(bot))
