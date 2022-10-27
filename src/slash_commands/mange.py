import discord
from lib.classes import CogExtension
from command_lib.manage import mange_member, clean, addrole, autorole


class SlashMange(CogExtension):

    @discord.application_command(description="踢出成員")
    async def kick(self, ctx, member: discord.Option(discord.Member,"選擇成員"), *, reason=None):
        if member != None:
            await mange_member(
                ctx=ctx,
                user=ctx.author,
                member=member,
                type="kick",
                title="從這個伺服器消失了!",
                reason=reason,
            )

        else:
            embed = discord.Embed(
                title="/kick 踢除成員",
                description="用法 /kick `提及/id/名字` `原因(可空)`"
            )

            await ctx.respond(embed=embed)

    @discord.application_command(description="停權成員")
    async def ban(self, ctx, member: discord.Option(discord.Member,"選擇成員"), *, reason=None):
        if member != None:
            await mange_member(
                ctx=ctx,
                user=ctx.author,
                member=member,
                type="ban",
                title="從這個伺服器消失了!",
                reason=reason,
            )

        else:
            embed = discord.Embed(
                title="/ban 停權成員",
                description="用法 /ban `提及/id/名字` `原因(可空)`"
            )

            await ctx.respond(embed=embed)

    @discord.application_command(description="新增身分組至另一名成員!")
    async def addrole(self,ctx,member : discord.Option(discord.Member,"選擇成員")=None,role : discord.Option(discord.Role,"選擇身分組")=None):
        await addrole(ctx,member,role)

    @discord.application_command(description="清理訊息")
    async def clear(self,ctx,limit:discord.Option(int,"您想清除多少個訊息?")=None):
        await clean(ctx,limit)
    
    #@discord.application_command(description="自動給予成員身分組")
    async def autorole(self,ctx,
        channel:discord.Option(discord.TextChannel,description="選擇要發送訊息頻道",name="頻道"),
    ):
        
        await autorole(ctx,channel)

def setup(bot):
    bot.add_cog(SlashMange(bot))
