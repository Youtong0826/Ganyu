import discord
from command_lib import help
from core.classes import CogExtension
from lib.function import SendBGM
from lib.bot_config import ganyuCommands

class SlashHelp(CogExtension):

    @discord.application_command(description="查看指令清單")
    async def help(self, ctx):
        await help.Help(ctx,"slash")

    @discord.application_command(description="娛樂指令清單")
    async def fun(self, ctx):
        await ctx.respond(embed=ganyuCommands["fun"])
        SendBGM(ctx)

    @discord.application_command(description="資訊指令清單")
    async def info(self, ctx):
        await ctx.respond(embed=ganyuCommands["info"])
        SendBGM(ctx)

    @discord.application_command(description="常用指令清單")
    async def cucmd(self, ctx):
        await ctx.respond(embed=ganyuCommands["cmd"])
        SendBGM(ctx)

    @discord.application_command(description="管理指令清單")
    async def manage(self, ctx):
        await ctx.respond(embed=ganyuCommands["manage"])
        SendBGM(ctx)

    @discord.application_command(description="工具指令清單")
    async def tool(self, ctx):
        await ctx.respond(embed=ganyuCommands["tool"])
        SendBGM(ctx)

def setup(bot):
    bot.add_cog(SlashHelp(bot))