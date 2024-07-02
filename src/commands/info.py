import discord 
from lib.cog import CogExtension
from lib.cog import Log
from command_lib import info

from discord import (
    ApplicationContext as Context,
    Colour,
    Embed,
    Invite,
    Member,
    SelectOption,
    option,
    slash_command
)

from discord.ui import (
    View,
    Button,
    Select,
)

class SlashInfo(CogExtension):

    @slash_command(description="查看所有的資訊!")
    async def allinfo(self, ctx: Context):
        self.bot.log(ctx)
        await ctx.respond(
            embed=Embed(
                title="一次查看所有資訊!",
                color=discord.Colour.random(),
            ), 
            view=View(
                Select(
                    options=[
                        SelectOption(
                            label="UserInfo",
                            value="user",
                            description="查看用戶資訊",
                            emoji="📰"
                        ),
                        SelectOption(
                            label="BotInfo",
                            value="bot",
                            description="查看Ganyu甘雨的資訊",
                            emoji="🤖"
                        ),
                        SelectOption(
                            label="ServerInfo",
                            value="server",
                            description="查看有關伺服器的資訊",
                            emoji="📘"
                        )
                    ],
                    placeholder="選擇你要查看的資訊",
                    custom_id="allinfo_select"
                ), 
            timeout=None
        )
    )

    @slash_command(description="查看伺服器資訊!")
    async def serinfo(self, ctx: Context):
        self.bot.log(ctx)
        await ctx.respond(**self.bot.get_guild_data(ctx.guild))

    @slash_command(description="查看機器人資訊!")
    async def botinfo(self, ctx: Context):
        self.bot.log(ctx)
        await ctx.respond(**self.bot.get_bot_data(ctx.guild))

    @slash_command(description="查看用戶資訊!")
    async def userinfo(self, ctx: Context, member: Member = None):
        self.bot.log(ctx)
        await ctx.respond(**self.bot.get_user_data(member if member else ctx.author))

    @slash_command(description="邀請機器人")
    async def invite(self, ctx: Context):
        self.bot.log(ctx)
        await ctx.respond(embed=Embed(
            title="邀請我至你的伺服器!",
            description=f"                                                                                                                              \
                [邀請連結 | invite link](https://discord.com/oauth2/authorize?client_id=921673886049910795&permissions=8&integration_type=0&scope=bot)\n \
                [支援伺服器 | Support Server](https://discord.gg/AVCWGuuUex)",
            color=discord.Colour.random(),
        ))

    @slash_command(description="查看邀請排行榜!")
    async def invites(self, ctx: discord.ApplicationContext):
        self.bot.log(ctx)
        data = {}
        for i in await ctx.guild.invites():
            data[i.inviter] = data.get(i.inviter, 0) + i.uses

        rank = [
            ":one: ",
            ":two: ",
            ":three: ",
            ":four: ",
            ":five: ",
            ":six: ",
            ":seven: ",
            ":eight: ",
            ":nine: ",
            ":keycap_ten: "
        ]

        data = list(map(lambda x: f"{rank[x[0]]} {x[1][0]}邀請 {x[1][1]} 人", enumerate(sorted(data.items(), key=lambda x: x[1]))))        

        await ctx.respond(embed=Embed(
            title=f"{ctx.guild.name} 的邀請榜", 
            color=Colour.blue(),
            description="\n\n".join(data)
        ))


    @slash_command(description="查看身分組資訊!")
    async def roleinfo(self,ctx : discord.ApplicationContext,*,role : discord.Option(discord.Role,"選擇身分組") = None ):
        await info.roleinfo(ctx, role)

def setup(bot):
    bot.add_cog(SlashInfo(bot))
