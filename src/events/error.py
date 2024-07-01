import asyncio
from lib.functions import translate
from lib.classes import CogExtension, Log
from discord.ext import commands
import discord

class ErrorEvent(CogExtension):
    async def send_background_message(self, ctx, exception):
        guild = ctx.guild
        user = ctx.author
        channel = ctx.channel
        command = ctx.command

        embed = discord.Embed(
            title="Error Message",
            description=f"**User:** `{user.name}` **id:** `{user.id}`\
                \n**Guild:** `{guild.name}` **id**: `{guild.id}`\
                \n**Channel:** `{channel.name}` **id:** `{channel.id}`\
                \n**Command:** `{command}`",
            color=discord.Colour.nitro_pink(),
        )

        embed.add_field(name="Exception",value=f"```{exception}```")
    
        await self.bot.get_channel(993540019484622848).send(embed=embed)

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

        error_msg = await ctx.send(embed=embed)
        await error_msg.delete(delay=5.0)

        await self.send_background_message(ctx,error)
        Log(ctx).error_output(error)

    @commands.Cog.listener()
    async def on_application_command_error(self,ctx:discord.ApplicationContext, exception:discord.errors.ApplicationCommandInvokeError):
        if isinstance(exception.original,asyncio.TimeoutError):
            if ctx.command == "guess": await ctx.respond(f"`{ctx.author}` **遊戲已逾時**");return

        await self.send_background_message(ctx,exception)
        Log(ctx).error_output(exception)



def setup(bot):
    bot.add_cog(ErrorEvent(bot))
