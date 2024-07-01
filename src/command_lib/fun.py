import discord
import random
import datetime
from discord.ext import commands
from lib.cog import Log
from lib.bot_config import bot_icon_url

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

    Log(ctx).output()

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

    Log(ctx).output()

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

    
