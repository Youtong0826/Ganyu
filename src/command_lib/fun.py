import discord
import random
import datetime
from discord.ext import commands
from lib.functions import SendBGM
from lib.bot_config import bot_icon_url

async def dice(mode,number,ctx):

    mode_dict = {
        "賭博模式" : "limit",
        "自由模式" : "free"
    }

    if mode != None:
        if mode_dict[mode] == "limit":

            if number != None:
                if int(number) > 6 or int(number) < 1:

                    embed = discord.Embed(
                        title="...... >:(",
                        description=f"叫你選1~6 你選{number}幹嘛啦!",
                        color=discord.Colour.random()
                    )

                else:

                    dice = [1, 2, 3, 4, 5, 6]
                    end = random.choice(dice)

                    if end == number:

                        embed = discord.Embed(
                            title="成功!",
                            description=f"恭喜你成功骰到了{number}!",
                            color=discord.Colour.random()
                        )

                    else:

                        embed = discord.Embed(
                            title="很遺憾..",
                            description=f"您骰到了{end}..",
                            color=discord.Colour.random()
                        )

            else:
                embed = discord.Embed(
                    title="/dice 賭博模式",
                    description="賭博模式 顧名思義如果你賭的數字跟選出來的數字不一樣那你就**輸了** 相反的如果一樣那你就**贏了**",
                    color=discord.Colour.random()
                )

        elif mode_dict[mode] == "free":

            dice = [1, 2, 3, 4, 5, 6]
            end = random.choice(dice)

            embed = discord.Embed(
                title=f"您骰到了 {end}",
                color=discord.Colour.random()
            )
        
    else:
        embed = discord.Embed(
            title="/dice 遊戲介紹",
            description="用法:dice `模式` `數字`",
            color=discord.Colour.random()
        )
    
        embed.add_field(
            name="/dice 賭博模式",
            value="顧名思義 如果你賭的數字跟選出來的數字不一樣那你就**輸了** 相反的如果一樣那你就**贏了**",
            inline=False
        )

        embed.add_field(
            name="/dice 自由模式",
            value="沒有任何限制 純粹地骰骰子 #此模式無須輸入數字",
            inline=False
        )

    if isinstance(ctx,commands.Context):
        await ctx.send(embed=embed)

    elif isinstance(ctx,discord.ApplicationContext):
        await ctx.respond(embed=embed)

    SendBGM(ctx)
    
async def rock_paper_scissors(ctx):
    main = discord.Embed(
        title = "這次想出什麼呢?",
        color = discord.Colour.random(),
        timestamp = datetime.datetime.utcnow()
    )

    main.set_footer(text="猜拳",icon_url=bot_icon_url)

    default_view = discord.ui.View()

    scissors = discord.ui.Button(
        style = discord.ButtonStyle.success,
        label = "剪刀",
        emoji = "✂️",
        custom_id="scissors"
    )

    rock = discord.ui.Button(
        style = discord.ButtonStyle.success,
        label = "石頭",
        emoji = "🪨",
        custom_id="rock"
    )

    paper = discord.ui.Button(
        style = discord.ButtonStyle.success,
        label = "布",
        emoji = "🌫️",
        custom_id="paper"
    )

    async def callback(interaction:discord.Interaction):
        details = {
            "win" : ["你輸了..","但你還有下一次機會!"],
            "tie" : ["平手!","看來是勢均力敵呢!"],
            "lose" : ["你贏了!!","你贏了!!"]    
        }
        
        result = random.choice(["win","tie","lose"])

        embed = discord.Embed(
            title = details[result],
            description = details[result],
            color = discord.Colour.random()
        )

        await interaction.response.edit_message(embed=embed,view=default_view)
    
    #map(lambda x:x.callback==callback,[scissors,paper,rock])
    view = discord.ui.View(scissors,rock,paper,timeout=None)

    ctx.respond(embed=main,view=view)

    SendBGM(ctx)

async def luck(ctx,member):
    luckypoint = random.randint(0,100)
    luckybar = ""
    luckycolor = [
        "紅色","橘色","金色","琥珀色","黃色","檸檬綠色","蔚藍色","綠色","淺藍色","藍綠色","綠松色","道奇藍","洋紅色","鴨綠色","靛色",
        "紫色","奶油色","薰衣草色","蘭花色","粉紅色","灰色","白色","黑色"
    ]
    
    user = member if member != None else ctx.author

    embed = discord.Embed(
        title=f"{user.name} 感謝您使用此功能!",
        description="以下為您的測驗結果",
        color=discord.Colour.purple(),
        timestamp=datetime.datetime.utcnow()
    )

    for n in range(round(luckypoint/10)):
        luckybar += "▮"

    while (len(luckybar) != 10):
        luckybar += "▯"

    luckform = {
        "🔯 幸運指數":f"{luckybar} {luckypoint}%",
        "🔷 幸運色" : random.choice(luckycolor),
    }

    for n in luckform:
        embed.add_field(name=n,value=luckform[n],inline=False)

    embed.set_footer(text="lucktest | 運氣測試",icon_url=bot_icon_url)

    if isinstance(ctx,commands.Context):
        await ctx.send(embed=embed)

    elif isinstance(ctx,discord.ApplicationContext):
        await ctx.respond(embed=embed)

    SendBGM(ctx)

async def spank(ctx,member):
    if member != None:
        
        embed = discord.Embed(
            title=f"{member.name} 被 {ctx.author.name} 拍了一下屁股",
            color=discord.Colour.red()
        )

    else:
        embed = discord.Embed(
            title="使用/spank來偷打別人的屁股ww",
            description="用法: /spank `提及/名字/id`"
        )

    if isinstance(ctx,commands.Context):
        await ctx.send(embed=embed)

    elif isinstance(ctx,discord.ApplicationContext):
        await ctx.respond(embed=embed)

    SendBGM(ctx)

async def gay(ctx,member):
    if member != None:
        user = member

    else:
        user = ctx.author

    GayPoint = random.randint(0,100)

    Gaybar = ""

    for n in range(round(GayPoint/10)):
        Gaybar += "▮"

    while (len(Gaybar) != 10):
        Gaybar += "▯"

    embed = discord.Embed(
        title=f"{user.name}",
        description=f"{Gaybar} **{GayPoint}%** Gay",
        color=discord.Colour.random(),
    )

    if isinstance(ctx,commands.Context):
        await ctx.send(embed=embed)

    elif isinstance(ctx,discord.ApplicationContext):
        await ctx.respond(embed=embed)

async def gessNum(ctx,number):
    answer = random.randint(0,100)

    
