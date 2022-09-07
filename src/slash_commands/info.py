import discord 
from core.classes import CogExtension
from lib.function import SendBGM
from command_lib import info

class SlashInfo(CogExtension):

    @discord.application_command(description="查看所有的資訊!")
    async def allinfo(self, ctx):
        await info.allinfo(ctx,self.bot)

    @discord.application_command(description="查看伺服器資訊!")
    async def serinfo(self, ctx):

        setting = info.server_data(guild=ctx.author.guild)

        await ctx.send_response(
            embed=setting["Embed"],
            view=setting["View"]
        )
        
        SendBGM(ctx)

    @discord.application_command(description="查看機器人資訊!")
    async def botinfo(self, ctx):
        setting = info.bot_data(bot=self.bot)

        await ctx.send_response(embed=setting["Embed"],view=setting["View"])

        SendBGM(ctx)

    @discord.application_command(description="查看用戶資訊!")
    async def userinfo(self, ctx, member: discord.Member = None):

        setting = info.user_data(member) if member != None else info.user_data(ctx.author)

        await ctx.send_response(embed=setting["Embed"],view=setting["View"])

        SendBGM(ctx)

    @discord.application_command(description="邀請機器人")
    async def invite(self, ctx):
        await info.invite(ctx)

    @discord.application_command(description="查看邀請排行榜!")
    async def invites(self, ctx: discord.ApplicationContext):
        await info.invites(ctx)

    @discord.application_command(description="查看身分組資訊!")
    async def roleinfo(self,ctx : discord.ApplicationContext,*,role : discord.Option(discord.Role,"選擇身分組") = None ):
        await info.roleinfo(ctx,role)

def setup(bot):
    bot.add_cog(SlashInfo(bot))
