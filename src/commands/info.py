import discord , datetime
from discord.ext import commands
from core.classes import CogExtension
from lib.bot_config import bot_icon_url
from lib.function import SendBGM
from command_lib import info
"""
g!allinfo
g!serinfo
g!botinfo
g!userinfo
g!update
g!invite
"""

class Info(CogExtension):
    @commands.command()
    async def allinfo(self, ctx):
        await info.Allinfo(ctx,self.bot,"command")

    @commands.command()
    async def serinfo(self, ctx):

        Setting = info.ServerDict(guild=ctx.author.guild)

        await ctx.send(
            embed=Setting["Embed"],
            view=Setting["View"]
        )
        
        SendBGM(ctx)

    @commands.command()
    async def botinfo(self, ctx):
        Setting = info.BotDict(bot=self.bot)

        await ctx.send(embed=Setting["Embed"],view=Setting["View"])

        SendBGM(ctx)

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):
        if member != None:
            setting = info.UserDict(member)

        else:
            setting = info.UserDict(ctx.author)

        await ctx.send(embed=setting["Embed"],view=setting["View"])

        SendBGM(ctx)

    @commands.command()
    async def invite(self, ctx):
        await info.Invite(ctx,"command")

    @commands.command()
    async def invites(self, ctx: discord.ApplicationContext):
        await info.Invites(ctx,"command")

    @commands.command()
    async def getuser(self, ctx, id: int):
        embed = discord.Embed(
            title="成功!",
            description=f"id為 {id} 的用戶是 {self.bot.get_user(id).name} !",
            color=discord.Colour.random(),
            timestamp=datetime.datetime.utcnow()
        )

        embed.set_footer(
            text=f"{ctx.author.name}",
            icon_url=ctx.author.avatar
        )

        await ctx.send(embed=embed)
        SendBGM(ctx)

    @commands.command()
    async def getid(self, ctx, name: discord.Member):

        embed = discord.Embed(
            title="成功!",
            description=f"用戶名為 {name.name} 的id是 {name.id} !",
            color=discord.Colour.random(),
            timestamp=datetime.datetime.utcnow()
        )

        embed.set_footer(
            text=f"{ctx.author.name}",
            icon_url=ctx.author.avatar
        )

        await ctx.send(embed=embed)
        SendBGM(ctx)

    @commands.command()
    async def roleinfo(self,ctx : discord.ApplicationContext,*,role : discord.Role = None ):
        await info.Roleinfo(ctx,role,type="command")
        
            
def setup(bot):
    bot.add_cog(Info(bot))