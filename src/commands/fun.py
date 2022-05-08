import random
import discord
import datetime
from discord.ext import commands
from core.classes import Cog_ExtenSion
from lib.bot_config import bot_icon_url

class Fun(Cog_ExtenSion):
    """
    fun command list\n
    g!dice\n
    g!rpg
    """

    @commands.command()
    async def dice(self, ctx, number: int = None):
        if number != None:
            if int(number) > 6 or int(number) < 1:
                embed = discord.Embed(
                    title="...... >:(",
                    description=f"叫你選1~6 你選{number}幹嘛啦!",
                    color=discord.Colour.random()
                )
                await ctx.send(embed=embed)
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
                title="選擇你要猜的號碼!",
                description="輸入 g!dice 1~6",
                color=discord.Colour.random()
            )

        await ctx.send(embed=embed)
        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")

    @commands.command()
    async def rainbow(self,ctx):
        embed = discord.Embed(color=0x5c5c5c)

        embed.set_image(url="https://cdn.discordapp.com/attachments/616315208251605005/616319462349602816/Tw.gif")

        await ctx.send(embed=embed)

    @commands.command()
    async def mora(self,ctx):
        moras = ["剪刀","石頭","布"]
        moraed = random.choice(moras)

        talkings = [
            "你不知道甘雨是猜拳高手嗎?",
            "偷偷告訴你||我出石頭ㄛ||",
            "偷偷告訴你||我出布ㄛ||",
            "偷偷告訴你||我出剪刀ㄛ||",
            "~~給我一瓶椰奶我就投降~~"
        ]
        talking = random.choice(talkings)

        MainEmbed = discord.Embed(
            title = "這次想出什麼呢?",
            description = talking,
            color = discord.Colour.random(),
            timestamp = datetime.datetime.utcnow()
        )

        MainEmbed.set_footer(text="猜拳",icon_url=bot_icon_url)

        MainView = discord.ui.View(timeout=None)
        DefaultView = discord.ui.View()

        ScissorsButton = discord.ui.Button(
            style = discord.ButtonStyle.success,
            label = "剪刀",
            emoji = "✂️"
        )

        RockButton = discord.ui.Button(
            style = discord.ButtonStyle.success,
            label = "石頭",
            emoji = "🪨"
        )

        ClothButton = discord.ui.Button(
            style = discord.ButtonStyle.success,
            label = "布",
            emoji = "📄"
        )

        async def ScissorsButtonCallback(interaction:discord.Interaction):

            if moraed == "剪刀":
                embed = discord.Embed(
                    title = "平手!",
                    description = "你們兩人都出了剪刀XD",
                    color = discord.Colour.random()
                )

            elif moraed == "石頭":
                embed = discord.Embed(
                    title = "你輸了..",
                    description = "甘雨出了石頭...沒關西，你還有下一次機會!",
                    color = discord.Colour.random()
                )

            else:
                embed = discord.Embed(
                    title = "你贏了!!",
                    description = "但是甘雨好像很難過(?",
                    color = discord.Colour.random()
                )

            await interaction.response.edit_message(embed=embed,view=DefaultView)

        async def  RockButtonCallback(interaction:discord.Interaction):

            if moraed == "剪刀":
                embed = discord.Embed(
                    title = "你贏了!!",
                    description = "但是甘雨好像很難過(?",
                    color = discord.Colour.random()
                )

            elif moraed == "石頭":
                embed = discord.Embed(
                    title = "平手!",
                    description = "你們兩人都出了石頭XD",
                    color = discord.Colour.random()
                )

            else:
                embed = discord.Embed(
                    title = "你輸了..",
                    description = "甘雨出了布...沒關西，你還有下一次機會!",
                    color = discord.Colour.random()
                )

            await interaction.response.edit_message(embed=embed,view=DefaultView)

        async def  ClothButtonCallback(interaction:discord.Interaction):

            if moraed == "剪刀":
                embed = discord.Embed(
                    title = "你輸了..",
                    description = "甘雨出了剪刀...沒關西，你還有下一次機會!",
                    color = discord.Colour.random()
                )

            elif moraed == "石頭":
                embed = discord.Embed(
                    title = "你贏了!!",
                    description = "但是甘雨好像很難過(?",
                    color = discord.Colour.random()
                )

            else:
                embed = discord.Embed(
                    title = "平手!",
                    description = "你們兩人都出了布XD",
                    color = discord.Colour.random()
                )

            await interaction.response.edit_message(embed=embed,view=DefaultView)

        
        ScissorsButton.callback = ScissorsButtonCallback
        RockButton.callback = RockButtonCallback
        ClothButton.callback = ClothButtonCallback

        MainView.add_item(ScissorsButton)
        MainView.add_item(RockButton)
        MainView.add_item(ClothButton)

        await ctx.send(embed = MainEmbed, view = MainView)

    @commands.command()
    async def luck(self,ctx):
        luckypoint = random.randint(0,100)

        luckycolor = [
            "紅色","橘色","金色","琥珀色","黃色","檸檬綠色","蔚藍色","綠色","淺藍色","藍綠色","綠松色","道奇藍","洋紅色","鴨綠色","靛色",
            "紫色","奶油色","薰衣草色","蘭花色","粉紅色","灰色","白色","黑色"
        ]
        
        luckystick = [
            "大大吉","大吉","吉",""
        ]

        embed = discord.Embed(
            title=f"{ctx.author.name} 感謝您使用此功能!",
            description="以下為您的測驗結果",
            color=discord.Colour.purple(),
            timestamp=datetime.datetime.utcnow()
        )

        luckform = {
            "🔯 幸運指數":luckypoint,
            "🔷 幸運色" : random.choice(luckycolor),
        }

        for n in luckform:
            embed.add_field(name=n,value=luckform[n])

        embed.set_footer(text="lucktest | 運氣測試",icon_url=bot_icon_url)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Fun(bot))
