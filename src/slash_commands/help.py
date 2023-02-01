import discord
from command_lib import help
from lib.classes import CogExtension
from lib.classes import Log
from lib.bot_config import ganyuCommands

class SlashHelp(CogExtension):
    @discord.application_command(description="查看指令清單")
    async def help(self, ctx):
        await help.help(ctx)

    @discord.application_command(description="娛樂指令清單")
    async def fun(self, ctx):
        await ctx.respond(embed=ganyuCommands["fun"])
        Log(ctx).output()

    @discord.application_command(description="資訊指令清單")
    async def info(self, ctx):
        await ctx.respond(embed=ganyuCommands["info"])
        Log(ctx).output()

    @discord.application_command(description="其他指令清單")
    async def other(self, ctx):
        await ctx.respond(embed=ganyuCommands["other"])
        Log(ctx).output()

    @discord.application_command(description="管理指令清單")
    async def manage(self, ctx):
        await ctx.respond(embed=ganyuCommands["manage"])
        Log(ctx).output()

    @discord.application_command(description="工具指令清單")
    async def tool(self, ctx):
        await ctx.respond(embed=ganyuCommands["tool"])
        Log(ctx).output()


def setup(bot):
    bot.add_cog(SlashHelp(bot))
