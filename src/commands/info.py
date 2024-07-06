from discord import (
    ApplicationContext as Context,
    ButtonStyle,
    Colour,
    Embed,
    EmbedField,
    EmbedFooter,
    Member,
    Role,
    SelectOption,
    option,
    slash_command
)

from discord.ui import (
    View,
    Button,
    Select,
)

from lib.cog import CogExtension
from lib.functions import get_now_time
from core import Bot

class SlashInfo(CogExtension):
    @slash_command(description="查看所有的資訊!")
    async def allinfo(self, ctx: Context):
        self.bot.log(ctx)
        await ctx.respond(
            embed=Embed(
                title="一次查看所有資訊!",
                color=Colour.random(),
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
        await ctx.respond(**self.bot.get_bot_data())

    @slash_command(description="查看用戶資訊!")
    @option("成員", Member, parameter_name="member", description="選擇成員", required=False)
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
            color=Colour.random(),
        ))

    @slash_command(description="查看邀請排行榜!")
    async def invites(self, ctx: Context):
        self.bot.log(ctx)
        data = {}
        for i in await ctx.guild.invites():
            if i.inviter: 
                data[i.inviter.mention] = data.get(i.inviter.mention, 0) + i.uses

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
        
        
        data = list(map(lambda x: f"{x[0]} {x[1][0]} 邀請 {x[1][1]} 人", zip(rank, reversed(sorted(data.items(), key=lambda x: x[1])))))       

        await ctx.respond(embed=Embed(
            title=f"{ctx.guild.name} 的邀請榜", 
            color=Colour.blue(),
            description="\n\n".join(data)
        ))

    @slash_command(description="查看身分組資訊!")
    @option("role", Role, description="選擇身分組", required = False)
    async def roleinfo(self, ctx: Context, role: Role):
        self.bot.log(ctx)
        if not role:
            return await ctx.respond(embed=Embed(
                title="使用 g!roleinfo 取得身分組資訊!",
                description="使用方法❓ g!roleinfo `標註身分組/身分組名稱/身分組id`",
                color=Colour.random(),
                footer=EmbedFooter("rolenfo | 身分組資訊", self.bot.icon_url)
            ))
        
        return await ctx.respond(
            embed=Embed(
                title=f'有關 {role.name} 身分組的資訊',
                color=role.color,
                timestamp=get_now_time(),
                fields=[
                    EmbedField(**i) for i in [
                        {"name": "🗒️ 名字", "value": role.mention},
                        {"name": "💳 id", "value": role.id},
                        {"name": "📊 人數", "value": len(role.members)},
                        {"name": "🗓️ 創建時間", "value": role.created_at.strftime('%Y/%m/%d')},
                        {"name": "👾 貼圖", "value": role.unicode_emoji if role.unicode_emoji else "無"},
                    ]
                ]
            ),
            view=View(
                Button(
                    style=ButtonStyle.success,
                    label="擁有者",
                    emoji="📊",
                    custom_id=f"roleinfo_owner_{role.id}"
                ),
                timeout=None
            )
        )


def setup(bot: Bot):
    bot.add_cog(SlashInfo(bot))
