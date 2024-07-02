import asyncio
from lib.functions import translate
from lib.cog import CogExtension, Log
from discord.ext import commands


from discord import (
    ApplicationContext as Context,
    Cog,
    Embed,
    EmbedField,
)

import discord

class ErrorEvent(CogExtension):
    async def send_background_message(self, ctx: Context, exception: Exception):
        await self.bot.get_channel(993540019484622848).send(embed=Embed(
            title="Error Message",
            description=f"**User:** `{ctx.author.name}` **id:** `{ctx.author.id}`\
                \n**Guild:** `{ctx.guild.name}` **id**: `{ctx.guild.id}`\
                \n**Channel:** `{ctx.channel.name}` **id:** `{ctx.channel.id}`\
                \n**Command:** `{ctx.command}`",
            color=discord.Colour.nitro_pink(),
            fields=[EmbedField("Exception", f"```{exception}```")]
        ))

    @Cog.listener()
    async def on_command_error(self, ctx: Context, error: Exception):
        self.bot.error(ctx, error)
        msg = await ctx.send(embed=Embed(
            title="錯誤",
            description="以下為回報內容",
            color=discord.Color.red(),
            fields=[
                EmbedField("原始內容", f"```{error}```"),
                EmbedField("翻譯後", f"```{translate(str(error), "zh-TW")}```"),
                EmbedField(
                    name="應對措施",
                    value="如果Bot或是指令發生錯誤的話可使用 `/report` 來回報給作者們!\n或是給個建議也可以喔! 我們非常需要您的建議!",
                )
            ]
        ))
        await msg.delete(delay=5.0)
        await self.send_background_message(ctx, error)
        

    @commands.Cog.listener()
    async def on_application_command_error(self, ctx: Context, error: discord.errors.ApplicationCommandInvokeError):
        if isinstance(error.original, asyncio.TimeoutError):
            if ctx.command == "guess": 
                return await ctx.respond(f"`{ctx.author}` **遊戲已逾時**")

        self.bot.error(ctx, error)
        
        await ctx.response.send_message(embed=Embed(
            title="錯誤",
            description="以下為回報內容",
            color=discord.Color.red(),
            fields=[
                EmbedField("原始內容", f"```{error}```"),
                EmbedField("翻譯後", f"```{translate(str(error), "zh-TW")}```"),
                EmbedField(
                    name="應對措施",
                    value="如果Bot或是指令發生錯誤的話可使用 `/report` 來回報給作者們!\n或是給個建議也可以喔! 我們非常需要您的建議!",
                )
            ]
        ), ephemeral=True)
        
        await self.send_background_message(ctx, error)



def setup(bot):
    bot.add_cog(ErrorEvent(bot))
