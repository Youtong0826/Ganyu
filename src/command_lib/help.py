import discord
from lib.bot_config import ganyuCommands
from lib.function import SendBGM

async def Help(ctx,type=["command","slash"]): 
    main_select = discord.ui.Select(
        placeholder="選擇要查看的指令清單",
        options=[
            discord.SelectOption(
                label=" Ganyu help ",
                value="ganyu",
                description="查看指令清單",
                emoji="🤖"
            ),
            discord.SelectOption(
                label=" Fun ",
                value="fun",
                description="查看 Fun 指令清單",
                emoji="🎉"
            ),
            discord.SelectOption(
                label=" Info ",
                value="info",
                description="查看 Info 指令清單",
                emoji="📘"
            ),
            discord.SelectOption(
                label=" Manage ",
                value="manage",
                description="查看 Manage 指令清單",
                emoji="⚙️"
            ),
            discord.SelectOption(
                label=" Tool ",
                value="tool",
                description="查看 Tool 指令清單",
                emoji="🛠️"
            ),
            #discord.SelectOption(
            #    label=" 音樂 ",
            #    value="music",
            #    description="查看 Music 指令清單",
            #    emoji="🎶"
            #),
            discord.SelectOption(
                label=" Other ",
                value="other",
                description="查看 Other 指令清單",
                emoji="📰"
            ),
        ]
    )

    InviteButton = discord.ui.Button(
        label="Invite me!",
        emoji="🔗",
        url="https://discord.com/api/oauth2/authorize?client_id=921673886049910795&permissions=12145977687&scope=bot%20applications.commands"
    )

    SupportButton = discord.ui.Button(
        label="Support",
        emoji="❓",
        url="https://discord.gg/AVCWGuuUex"
    )

    main_view = discord.ui.View(timeout=None)

    main_view.add_item(main_select)
    main_view.add_item(InviteButton)
    main_view.add_item(SupportButton)

    async def main_select_callback(interaction):
        await interaction.response.edit_message(
            embed=ganyuCommands[main_select.values[0]],
            view=main_view
        )

    main_select.callback = main_select_callback
    
    if type == "command":
        await ctx.send(
            embed=ganyuCommands["ganyu"],
            view=main_view
        )

    elif type == "slash":
        await ctx.respond(
            embed=ganyuCommands["ganyu"],
            view=main_view
        )

    SendBGM(ctx)