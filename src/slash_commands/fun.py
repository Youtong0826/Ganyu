import random
import discord
import datetime
from discord.ext import commands
from core.classes import CogExtension
from lib.bot_config import bot_icon_url
from lib.function import SendBGM
from command_lib import fun

class SlashFun(CogExtension):

    @discord.application_command(description="骰骰子")
    async def dice(self, ctx,
        mode: discord.Option(str,"選擇遊玩模式",choices=["賭博模式","自由模式"])=None,
        number: discord.Option(int,"選擇數字",choices=[1,2,3,4,5,6])=None
    ):
        await fun.Dice(mode,number,ctx,"slash")

    @discord.application_command(description="猜拳")
    async def mora(self,ctx):
        moras = ["剪刀","石頭","布"]
        moraed = random.choice(moras)

        MainEmbed = discord.Embed(
            title = "這次想出什麼呢?",
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
            emoji = "🌫️"
        )

        async def ScissorsButtonCallback(interaction:discord.Interaction):

            if moraed == "剪刀":
                embed = discord.Embed(
                    title = "平手!",
                    description = "看來是勢均力敵呢!",
                    color = discord.Colour.random()
                )

            elif moraed == "石頭":
                embed = discord.Embed(
                    title = "你輸了..",
                    description = "你還有下一次機會!",
                    color = discord.Colour.random()
                )

            else:
                embed = discord.Embed(
                    title = "你贏了!!",
                    description = "痾..恭喜!",
                    color = discord.Colour.random()
                )

            await interaction.response.edit_message(embed=embed,view=DefaultView)

        async def  RockButtonCallback(interaction:discord.Interaction):

            if moraed == "剪刀":
                embed = discord.Embed(
                    title = "你贏了!!",
                    description = "痾..恭喜!",
                    color = discord.Colour.random()
                )

            elif moraed == "石頭":
                embed = discord.Embed(
                    title = "平手!",
                    description = "看來是勢均力敵呢!",
                    color = discord.Colour.random()
                )

            else:
                embed = discord.Embed(
                    title = "你輸了..",
                    description = "你還有下一次機會!",
                    color = discord.Colour.random()
                )

            await interaction.response.edit_message(embed=embed,view=DefaultView)

        async def  ClothButtonCallback(interaction:discord.Interaction):

            if moraed == "剪刀":
                embed = discord.Embed(
                    title = "你輸了..",
                    description = "你還有下一次機會!",
                    color = discord.Colour.random()
                )

            elif moraed == "石頭":
                embed = discord.Embed(
                    title = "你贏了!!",
                    description = "痾..恭喜!",
                    color = discord.Colour.random()
                )

            else:
                embed = discord.Embed(
                    title = "平手!",
                    description = "勢均力敵呢!",
                    color = discord.Colour.random()
                )

            await interaction.response.edit_message(embed=embed,view=DefaultView)

        
        ScissorsButton.callback = ScissorsButtonCallback
        RockButton.callback = RockButtonCallback
        ClothButton.callback = ClothButtonCallback

        MainView.add_item(ScissorsButton)
        MainView.add_item(RockButton)
        MainView.add_item(ClothButton)

        await ctx.send_response(embed = MainEmbed, view = MainView)
        SendBGM(ctx)

    @discord.application_command(description="測試你的運氣")
    async def luck(self,ctx , member: discord.Option(discord.Member,"選擇成員")= None):
        luckypoint = random.randint(0,100)
        luckybar = ""

        luckycolor = [
            "紅色","橘色","金色","琥珀色","黃色","檸檬綠色","蔚藍色","綠色","淺藍色","藍綠色","綠松色","道奇藍","洋紅色","鴨綠色","靛色",
            "紫色","奶油色","薰衣草色","蘭花色","粉紅色","灰色","白色","黑色"
        ]
        

        if member != None:
            user = member
            
        else: 
            user = ctx.author

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

        await ctx.respond(embed=embed)
        SendBGM(ctx)

    @discord.application_command(description="偷拍他人的屁股")
    async def spank(self, ctx, member:discord.Option(discord.Member,"選擇成員") = None):
        if member != None:
            embed = discord.Embed(
                title=f"{member.name} 被 {ctx.author.name} 拍了一下屁股",
                color=discord.Colour.red()
            )

        else:
            embed = discord.Embed(
                title="使用g!spank來偷打別人的屁股ww",
                description="用法: g!spank `提及/名字/id`"
            )

        await ctx.respond(embed=embed)
        SendBGM(ctx)

    @discord.application_command(description="gay指數")
    async def gay(self,ctx,member:discord.Option(discord.Member,"選擇成員") = None):
        await fun.Gay(ctx,member,"slash")

    @discord.application_command()
    async def guess(self,ctx:discord.ApplicationContext,number:discord.Option(int,"輸入一個數字")):
        times = 0
        leave = False
        answer = random.randint(0,100)
        
        async def run_game():
            nonlocal times
            print(answer)
            await ctx.respond(f"您輸入了{number}遊戲已開始 閒置超過30秒或是輸入leave即可終止")

            while True:
                times += 1
                if number == answer: await ctx.respond(f"你贏了!!答案是{answer} 你總共猜了{times}次");break

                else: await ctx.send("提示:再大一點") if number < answer else await ctx.send("提示:再小一點")

                def check(msg:discord.Message):
                    nonlocal number, leave

                    if msg.author == ctx.author:
                        if msg.content == "leave": leave = True

                        try:number = int(msg.content)
                        except:pass

                        return True
        
                await self.bot.wait_for("message",check=check,timeout=30)
                if leave:break
            
            await ctx.send("遊戲結束")

        await run_game()
        

def setup(bot):
    bot.add_cog(SlashFun(bot))
