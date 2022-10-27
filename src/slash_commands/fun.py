import random
import discord
import datetime
from discord.ext import commands
from lib.classes import CogExtension
from lib.bot_config import bot_icon_url
from lib.functions import SendBGM,get_time
from command_lib import fun

class SlashFun(CogExtension):

    @discord.application_command(description="骰骰子")
    async def dice(self, ctx,
        mode: discord.Option(str,"選擇遊玩模式",choices=["賭博模式","自由模式"])=None,
        number: discord.Option(int,"選擇數字",choices=[1,2,3,4,5,6])=None
    ):
        await fun.dice(mode,number,ctx)

    @discord.application_command(description="猜拳")
    async def mora(self,ctx):
        await fun.mora(ctx)

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

    @discord.application_command(description="猜猜看你有多少Gay(?")
    async def gay(self,ctx,member:discord.Option(discord.Member,"選擇成員") = None):
        await fun.gay(ctx,member)

    #@discord.application_command(description="")
    async def guess(self,
        ctx:discord.ApplicationContext,
        range:discord.Option(str,"輸入數字的範圍(起始必須小於結束 以XX~XX表示)",name="範圍",max_length=12),
        number:discord.Option(int,"輸入一個數字",name="數字")
    ):
        range = range.split("~") if "~" in range else range.split("-")
        range_start = int(range[0])
        range_end = int(range[1])

        if not range or len(range) < 2 or range_start > range_end: await ctx.respond("**發生錯誤:**範圍的輸入格式不對!");return

        data = {}
        default_data = {
            "answer":random.randint(range_start,range_end),
            "start_time":get_time(),
            "input_number":number,
            "show_data":False,
            "is_leave":False,
            "end_time":None,
            "times":1
        }

        if ctx.author.id not in data.keys() or data[ctx.author.id] is {}:data[ctx.author.id] = default_data
        else: ctx.respond("您尚未退出當前的遊戲 請先退出您正在進行得遊戲在開始新的遊戲")
        
        async def run_game():
            user_data = data[ctx.author.id]

            await ctx.respond(f"**遊戲已開始** 玩家 `{ctx.author}` 輸入了 `{number}` 範圍為 `{range_start}~{range_end}`\
                \n**遊戲說明:** 閒置超過 `30秒` 或是輸入 `leave` 即可終止")

            while True:
                
                if user_data["input_number"] == user_data["answer"]:
                    await ctx.respond(f"**你猜中了!!** 答案是 `{user_data['answer']}` ")
                    user_data["end_time"] = get_time();break

                else:await ctx.send(f"**提示:** `{ctx.author}` 再大一點") if user_data["input_number"] < user_data["answer"] \
                    else await ctx.send(f"**提示:** `{ctx.author}` 再小一點")

                def check(msg:discord.Message):
                    user_data["times"] += 1

                    if msg.author == ctx.author and msg.channel == ctx.channel:
                        if "/show_data" in msg.content and msg.author.id == 856041155341975582:
                            user_data["show_data"] = True if "true" in msg.content else False; return False

                        elif msg.content == "leave": user_data["is_leave"] = True; return True

                        try:user_data["input_number"] = int(msg.content);return True
                        except:return False
        
                await self.bot.wait_for("message",check=check,timeout=30)
                if user_data["is_leave"]:await ctx.send(f"玩家 `{ctx.author}` **已退出遊戲**");del data[ctx.author.id];break
                if user_data["show_data"]:await ctx.send(f"**警告:**此為密技 僅限特殊人物使用\n```{user_data}```")

            if not user_data["end_time"]:return

            start_time = int(user_data["start_time"].strftime("%M"))*60 + int(user_data["start_time"].strftime("%S"))
            end_time = int(user_data["end_time"].strftime("%M"))*60 + int(user_data["end_time"].strftime("%S"))

            time = end_time - start_time
            min = str(time//60)
            sec = str(time%60)


            if len(sec) != 2: sec = "0" + sec
            time = f"{min}:{sec}"
            
            await ctx.send(f"**遊戲結束** 玩家 `{ctx.author}` 總共猜了 `{user_data['times']}` 次 耗時 `{time}` ")

        await run_game()
        

def setup(bot):
    bot.add_cog(SlashFun(bot))
