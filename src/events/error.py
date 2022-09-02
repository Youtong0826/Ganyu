import asyncio
from lib.function import translate,ErrorBGM
from core.classes import CogExtension
from discord.ext import commands
import discord

class ErrorEvent(CogExtension):

    @commands.Cog.listener()
    async def on_command_error(self,ctx : discord.ApplicationContext, error):
        zhCN = translate(str(error), "zh-TW")

        if zhCN.endswith("。"):
            zhCN = zhCN[:-1]

        embed = discord.Embed(title="錯誤",description="以下為回報內容",color=discord.Color.red())

        embed.add_field(name="原始內容",value=f"```{error}```",inline=False)

        embed.add_field(name="翻譯後",value=f"```{zhCN}```",inline=False)

        embed.add_field(
            name="應對措施",
            value="如果Bot或是指令發生錯誤的話可使用 `/report` 來回報給作者們!\n或是給個建議也可以喔! 我們非常需要您的建議!",
            inline=False
        )

        await self.bot.get_channel(993540019484622848).send(embed=embed)

        error_msg = await ctx.send(embed=embed)
        await error_msg.delete(delay=5.0)

        ErrorBGM(ctx,error)

    @commands.Cog.listener()
    async def on_application_command_error(self,ctx:discord.ApplicationContext, exception):
        guild = ctx.author.guild
        user = ctx.author
        channel = ctx.channel

        embed = discord.Embed(
            title="Error Message",
            description=f"**User:** `{user.name}` ,**id:** `{user.id}`\
                \n**Guild:** `{guild.name}` ,**id**: `{guild.id}`\
                \n**Channel:** `{channel.name}` ,**id:** `{channel.id}`",
            color=discord.Colour.nitro_pink()
        )

        embed.add_field(name="Exception",value=f"```{exception}```")

        await self.bot.get_channel(993540019484622848).send(embed=embed)
        ErrorBGM(ctx,exception)

def setup(bot):
    bot.add_cog(ErrorEvent(bot))
