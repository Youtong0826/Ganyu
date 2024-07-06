import discord

from random import (
    choice,
    randint
)

from discord import (
    ApplicationContext as Context,
    Colour,
    Embed,
    EmbedField,
    EmbedFooter,
    Member,
    option,
    slash_command
)

from discord.ui import (
    View,
    Button,
)

from lib.timing import get_now_time
from core import (
    Bot,
    CogExtension
)

class SlashFun(CogExtension):
    @slash_command(description="骰骰子")
    @option("模式", str, parameter_name="mode", description="選擇遊玩模式", choices=["競猜模式", "自由模式"], required=False)
    @option("數字", int, parameter_name="number", description="選擇數字", choices=[1, 2, 3, 4, 5, 6], required=False)
    async def dice(self, ctx: Context, mode: str = None, number: int = None):
        self.bot.log(ctx)
        if not mode:
            return await ctx.respond(embed=Embed(
                title="/dice 遊戲介紹",
                description="用法:dice `模式` `數字`",
                color=Colour.random(),
                fields=[
                    EmbedField(
                        "/dice 競猜模式",
                        "顧名思義 如果你賭的數字跟選出來的數字不一樣那你就**輸了** 相反的如果一樣那你就**贏了**",
                        False
                    ),
                    EmbedField(
                        "/dice 自由模式",
                        "沒有任何限制 純粹地骰骰子 #此模式無須輸入數字",
                        False
                    ),
                ]
            ))
            
        result = choice([1, 2, 3, 4, 5, 6])
        
        if mode == "競猜模式":
            if not number:
                return await ctx.respond("請選擇一個數字!")
                
            if int(number) > 6 or int(number) < 1:
                return await ctx.respond(f"叫你選1~6 你選 {number} 幹嘛啦!")
                
            if result == number:
                return await ctx.respond(f"恭喜你成功骰到了 {number} !")
                    
            return await ctx.respond(f"你骰到了 {result} ..")
                    
        else:
            return await ctx.respond(f"你骰到了 {result} !")

    @slash_command(name="rps", description="剪刀石頭布")
    async def rock_paper_scissors(self, ctx: Context):
        self.bot.log(ctx)
        await ctx.respond(
            "這次想出什麼呢?",
            view=View(
                Button(
                    style = discord.ButtonStyle.success,
                    label = "剪刀",
                    emoji = "✂️",
                    custom_id="rpc_punch_s"
                ),
                Button(
                    style = discord.ButtonStyle.success,
                    label = "石頭",
                    emoji = "🪨",
                    custom_id="rpc_punch_r"
                ),
                Button(
                    style = discord.ButtonStyle.success,
                    label = "布",
                    emoji = "🌫️",
                    custom_id="rpc_punch_p"
                )
            )
        )

    @slash_command(description="測試你的運氣")
    @option("成員", Member, parameter_name="member", description="選擇成員", required=False)
    async def luck(self, ctx: Context, member: Member = None):
        self.bot.log(ctx)
        user = member if member else ctx.author
        color = [
            "紅色", "橘色", "金色","琥珀色","黃色","檸檬綠色","蔚藍色","綠色","淺藍色",
            "藍綠色", "綠松色","道奇藍","洋紅色","鴨綠色","靛色","紫色","奶油色",
            "薰衣草色", "蘭花色","粉紅色","灰色","白色","黑色"
        ]
        point = randint(0, 100)
    
        await ctx.respond(embed=Embed(
            title=f"{user.name} 感謝您使用此功能!",
            description="以下為您的測驗結果",
            color=Colour.purple(),
            timestamp=get_now_time(),
            fields=[EmbedField(k, v, False) for k, v in {
                "🔯 幸運指數": f"{"▮"*round(point/10) + "▯"*(10-round(point/10))} {point}%",
                "🔷 幸運色" : choice(color),
            }.items()],
            footer=EmbedFooter("/luck | 運氣測試", self.bot.icon_url)
        ))
        

    @slash_command(description="偷拍他人的屁股")
    @option("成員", Member, parameter_name="member", description="選擇成員", required=False)
    async def spank(self, ctx: Context, member: discord.Member = None):
        self.bot.log(ctx)
        if member:
            return await ctx.respond(f"{member.mention} 被 {ctx.author.mention} 拍了一下屁股")
        
        return await ctx.respond(embed=Embed(
            title="使用 /spank 來偷打別人的屁股ww",
            description="用法: /spank `提及/名字/id`"
        ))

    @slash_command(description="猜猜看你有多少Gay(?")
    @option("成員", Member, parameter_name="member", description="選擇成員", required=False)
    async def gay(self, ctx: Context, member: discord.Member = None):
        self.bot.log(ctx)
        user = member if member else ctx.author
        point = randint(0, 100)
        
        await ctx.respond(embed=Embed(
            title=f"{user.name}",
            description=f"{"▮"*round(point/10) + "▯"*(10-round(point/10))} **{point}%** Gay",
            color=discord.Colour.random(),
        ))

    # @slash_command(description="")
    # @option("range", str, desciption="輸入數字的範圍(起始必須小於結束 以XX~XX表示)", max_length=12, required=False)
    # @option("number", int, desciption="輸入一個數字", required=False)
    # async def guess(self, ctx: Context, range: str, number: int):
    #     range = range.split("~") if "~" in range else range.split("-")
    #     range_start = int(range[0])
    #     range_end = int(range[1])

    #     if not range or len(range) < 2 or range_start > range_end: 
    #         return await ctx.respond("**發生錯誤:** 範圍的輸入格式不對!");

    #     data = {}
    #     default_data = {
    #         "answer": randint(range_start,range_end),
    #         "start_time": get_now_time(),
    #         "input_number": number,
    #         "show_data": False,
    #         "is_leave": False,
    #         "end_time":None,
    #         "times": 1
    #     }

    #     if ctx.author.id not in data.keys() or data[ctx.author.id] is {}:
    #         data[ctx.author.id] = default_data
            
    #     else: 
    #         ctx.respond("您尚未退出當前的遊戲 請先退出您正在進行得遊戲在開始新的遊戲")
        
    #     async def run_game():
    #         user_data = data[ctx.author.id]

    #         await ctx.respond(f"**遊戲已開始** 玩家 `{ctx.author}` 輸入了 `{number}` 範圍為 `{range_start}~{range_end}`\
    #             \n**遊戲說明:** 閒置超過 `30秒` 或是輸入 `leave` 即可終止")

    #         while True:
                
    #             if user_data["input_number"] == user_data["answer"]:
    #                 await ctx.respond(f"**你猜中了!!** 答案是 `{user_data['answer']}` ")
    #                 user_data["end_time"] = get_now_time() 
    #                 break

    #             else:await ctx.send(f"**提示:** `{ctx.author}` 再大一點") if user_data["input_number"] < user_data["answer"] \
    #                 else await ctx.send(f"**提示:** `{ctx.author}` 再小一點")

    #             def check(msg:discord.Message):
    #                 user_data["times"] += 1

    #                 if msg.author == ctx.author and msg.channel == ctx.channel:
    #                     if "/show_data" in msg.content and msg.author.id == 856041155341975582:
    #                         user_data["show_data"] = True if "true" in msg.content else False; return False

    #                     elif msg.content == "leave": user_data["is_leave"] = True; return True

    #                     try:user_data["input_number"] = int(msg.content);return True
    #                     except:return False
        
    #             await self.bot.wait_for("message",check=check,timeout=30)
    #             if user_data["is_leave"]:await ctx.send(f"玩家 `{ctx.author}` **已退出遊戲**");del data[ctx.author.id];break
    #             if user_data["show_data"]:await ctx.send(f"**警告:**此為密技 僅限特殊人物使用\n```{user_data}```")

    #         if not user_data["end_time"]:return

    #         start_time = int(user_data["start_time"].strftime("%M"))*60 + int(user_data["start_time"].strftime("%S"))
    #         end_time = int(user_data["end_time"].strftime("%M"))*60 + int(user_data["end_time"].strftime("%S"))

    #         time = end_time - start_time
    #         min = str(time//60)
    #         sec = str(time%60)


    #         if len(sec) != 2: sec = "0" + sec
    #         time = f"{min}:{sec}"
            
    #         await ctx.send(f"**遊戲結束** 玩家 `{ctx.author}` 總共猜了 `{user_data['times']}` 次 耗時 `{time}` ")

    #     await run_game()
        

def setup(bot: Bot):
    bot.add_cog(SlashFun(bot))
