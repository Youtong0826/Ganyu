from discord import (
    ApplicationContext as Context,
    SelectOption,
    slash_command
)

from discord.ui import (
    Button,
    Select,
    View
)

from core import (
    Bot,
    CogExtension
)

class SlashHelp(CogExtension):
    @slash_command(description="查看指令清單")
    async def help(self, ctx: Context):
        self.bot.log(ctx)
        await ctx.respond(embed=self.bot.commands_list["ganyu"], view=View(
            Select(
                placeholder="選擇要查看的指令清單",
                options=[
                    SelectOption(
                        label=" Ganyu help ", value="ganyu", description="查看指令清單", emoji="🤖"
                    ),
                    SelectOption(
                        label=" Fun ", value="fun", description="查看 Fun 指令清單", emoji="🎉"
                    ),
                    SelectOption(
                        label=" Info ", value="info", description="查看 Info 指令清單", emoji="📘"
                    ),
                    SelectOption(
                        label=" Manage ",
                        value="manage",
                        description="查看 Manage 指令清單",
                        emoji="⚙️",
                    ),
                    SelectOption(
                        label=" Tool ", value="tool", description="查看 Tool 指令清單", emoji="🛠️"
                    ),
                    # discord.SelectOption(
                    #    label=" 音樂 ",
                    #    value="music",
                    #    description="查看 Music 指令清單",
                    #    emoji="🎶"
                    # ),
                    SelectOption(
                        label=" Other ", value="other", description="查看 Other 指令清單", emoji="📰"
                    ),
                ],
                custom_id="help_select"
            ), 
            Button(
                label="Invite me!",
                emoji="🔗",
                url="https://discord.com/api/oauth2/authorize?client_id=921673886049910795&permissions=12145977687&scope=bot%20applications.commands",
            ), 
            Button(
                label="Support", emoji="❓", url="https://discord.gg/AVCWGuuUex"
            ),
            timeout=None
        ))

    @slash_command(description="娛樂指令清單")
    async def fun(self, ctx: Context):
        self.bot.log(ctx)
        await ctx.respond(embed=self.bot.commands_list["fun"])

    @slash_command(description="資訊指令清單")
    async def info(self, ctx: Context):
        self.bot.log(ctx)
        await ctx.respond(embed=self.bot.commands_list["info"])

    @slash_command(description="其他指令清單")
    async def other(self, ctx: Context):
        self.bot.log(ctx)
        await ctx.respond(embed=self.bot.commands_list["other"])

    @slash_command(description="管理指令清單")
    async def manage(self, ctx: Context):
        self.bot.log(ctx)
        await ctx.respond(embed=self.bot.commands_list["manage"])

    @slash_command(description="工具指令清單")
    async def tool(self, ctx: Context):
       self.bot.log(ctx)
       await ctx.respond(embed=self.bot.commands_list["tool"])


def setup(bot: Bot):
    bot.add_cog(SlashHelp(bot))
