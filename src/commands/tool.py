import html
import  discord , datetime , requests , json 
from discord.ext import commands
from core.classes import Cog_ExtenSion
from lib.function import translate,wiki_search,bluffshit,calculator
from commands.rpg import bot_icon_url

google_translate_icon_url = "https://th.bing.com/th/id/R.93d2c8f15964faae1e75331caf7d8fe0?rik=vl9rlcN9fh1oEw&pid=ImgRaw&r=0"
wikipedia_icon_url = "https://www.bing.com/images/search?view=detailV2&ccid=CLnSyWEa&id=E66C2DFADDB113B154BE0073382FBCEF88E51ACB&thid=OIP.CLnSyWEawnaZ8T3saUMfsgHaHa&mediaurl=https%3a%2f%2f3c1703fe8d.site.internapcdn.net%2fnewman%2fgfx%2fnews%2fhires%2f2017%2f58af0228b8aa8.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.08b9d2c9611ac27699f13dec69431fb2%3frik%3dyxrliO%252b8LzhzAA%26pid%3dImgRaw%26r%3d0&exph=1500&expw=1500&q=wikipedia&simid=607995489110011574&FORM=IRPRST&ck=D48A403BD14BEB6F8CABA45AE032EAD4&selectedIndex=4"

class Tool(Cog_ExtenSion):

    @commands.command()
    async def translate(self,ctx,*,text=None):
        if text != None:
            translate_text = translate(str(text),"zh-TW")
            embed = discord.Embed(
                title="成功! 以下為翻譯結果",
                color=discord.Colour.random(),
                timestamp=datetime.datetime.utcnow()
            )

            embed.add_field(
                name="原文",
                value=f"```{text}```"
            )
            embed.add_field(
                name="翻譯",
                value=f"```{translate_text}```",
                inline=False
            )

        else:
            embed = discord.Embed(
                title="歡迎使用翻譯小工具!",
                description="此指令可以將各種語言翻譯成中文\n使用方法 g!translate `文字`",
                color=discord.Colour.random(),
                timestamp=datetime.datetime.utcnow()
            )

        embed.set_thumbnail(url=google_translate_icon_url)
        embed.set_footer(text="translate",icon_url=bot_icon_url)

        await ctx.send(embed = embed)
        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")

    @commands.command()
    async def wiki(self,ctx,text=None):
        article = wiki_search(text=text)

        if len(article) >= 6000:
            article = article[0:1200]+"..."
        
        if text != None:
            embed = discord.Embed(
                title=text,
                description=article,
                color=discord.Colour.random())
        
        else:
            embed = discord.Embed(
                title="歡迎使用維基百科!",
                description="使用方法 g!wiki `text`",
                color=discord.Colour.random()
            )

        embed.set_thumbnail(url=wikipedia_icon_url)
        embed.set_footer(text="wikipedia.org",icon_url=bot_icon_url)        
        await ctx.send(embed = embed)
        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")

    @commands.command()
    async def words(self,ctx,*,text=None):
        if text != None:
            space = 0
            for n in text:
                if n == " ":
                    space += 1

            embed = discord.Embed(
                title="轉換成功!",
                description=f"此段句子一共有**{len(text)}**個字(含有**{space}**個空格)"
            )

        else:
            embed = discord.Embed(
                title="使用 g!words 來轉換字數!",
                description="使用方法: g!words `句子`"
            )

        embed.color = discord.Colour.random()
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text="字數轉換器",icon_url=bot_icon_url)

        await ctx.send(embed=embed)

    @commands.command()
    async def bluff(self,ctx,topic:str = None,minlen:int = None):
        if topic and minlen != None:
            artcle = bluffshit(topic,minlen)

            embed = discord.Embed(
                title=topic,
                description=artcle
            )

        else:
            embed = discord.Embed(
                title="使用g!bluff唬爛產生器來生成文章!",
                description="使用方法 g!bluff `主題(如有空格需要用\"包起來)` `字數(上限1000)`"
            )
        
        embed.color = discord.Colour.random()
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text="唬爛產生器",icon_url = bot_icon_url)
        
        await ctx.send(embed=embed)

    @commands.command()
    async def math(self,ctx):
        default_value = "                                        "

        calculate_value = ""

        embed = discord.Embed(
            title="簡易計算機",
            description=f"```{default_value}```",
            color=discord.Colour.blue(),
            timestamp=datetime.datetime.utcnow()
        )

        embed.set_footer(text="Calculate 計算機",icon_url=bot_icon_url)

        view = discord.ui.View(timeout=None)

        button1 = discord.ui.Button(
            style=discord.ButtonStyle.primary,
            label="1",
            row=1
        )

        button2 = discord.ui.Button(
            style=discord.ButtonStyle.primary,
            label="2",
            row=1
        )

        button3 = discord.ui.Button(
            style=discord.ButtonStyle.primary,
            label="3",
            row=1
        )

        button4 = discord.ui.Button(
            style=discord.ButtonStyle.primary,
            label="4",
            row=2
        )

        button5 = discord.ui.Button(
            style=discord.ButtonStyle.primary,
            label="5",
            row=2
        )

        button6 = discord.ui.Button(
            style=discord.ButtonStyle.primary,
            label="6",
            row=2
        )

        button7 = discord.ui.Button(
            style=discord.ButtonStyle.primary,
            label="7",
            row=3
        )

        button8 = discord.ui.Button(
            style=discord.ButtonStyle.primary,
            label="8",
            row=3
        )

        button9 = discord.ui.Button(
            style=discord.ButtonStyle.primary,
            label="9",
            row=3
        )

        button0 = discord.ui.Button(
            style=discord.ButtonStyle.primary,
            label="0",
            row=4
        )

        dot_button = discord.ui.Button(
            style=discord.ButtonStyle.gray,
            label=".",
            row=4
        )

        equal_button = discord.ui.Button(
            style=discord.ButtonStyle.success,
            label="=",
            row=4
        )

        plus_button = discord.ui.Button(
            style=discord.ButtonStyle.gray,
            label="+",
            row=1
        )

        minus_button = discord.ui.Button(
            style=discord.ButtonStyle.gray,
            label="-",
            row=2
        )

        multiply_button = discord.ui.Button(
            style=discord.ButtonStyle.gray,
            label="×",
            row=3
        )

        division_button = discord.ui.Button(
            style=discord.ButtonStyle.gray,
            label="÷",
            row=4
        )

        AC_button = discord.ui.Button(
            style=discord.ButtonStyle.danger,
            label="AC",
            row=1
        )

        C_button = discord.ui.Button(
            style=discord.ButtonStyle.danger,
            label="C",
            row=2
        )
        
        buttons = [
            button1, button2, button3, plus_button, AC_button,

            button4, button5, button6, minus_button, C_button,

            button7, button8, button9, multiply_button,

            dot_button, button0, equal_button, division_button,
        ]

        for n in buttons: 
            view.add_item(n)
        
        async def button1callback(interaction:discord.Interaction):
            if interaction.user != ctx.author:
                await interaction.response.send_message("❌非此指令使用者無法操控!",ephemeral=True)
            else:
                nonlocal calculate_value
                calculate_value += "1"

                embed = discord.Embed(
                    title="簡易計算機",
                    description=f"```{calculate_value}{default_value[len(calculate_value):40]}```",
                    color=discord.Colour.blue(),
                    timestamp=datetime.datetime.utcnow()
                )

                embed.set_footer(text="Calculate 計算機",icon_url=bot_icon_url)

                await interaction.response.edit_message(embed=embed,view=view)

        async def button2callback(interaction:discord.Interaction):
            if interaction.user != ctx.author:
                await interaction.response.send_message("❌非此指令使用者無法操控!",ephemeral=True)
            else:
                nonlocal calculate_value
                calculate_value += "2"

                embed = discord.Embed(
                    title="簡易計算機",
                    description=f"```{calculate_value}{default_value[len(calculate_value):40]}```",
                    color=discord.Colour.blue(),
                    timestamp=datetime.datetime.utcnow()
                )

                embed.set_footer(text="Calculate 計算機",icon_url=bot_icon_url)

                await interaction.response.edit_message(embed=embed,view=view)

        async def button3callback(interaction:discord.Interaction):
            if interaction.user != ctx.author:
                await interaction.response.send_message("❌非此指令使用者無法操控!",ephemeral=True)
            else:
                nonlocal calculate_value
                calculate_value += "3"

                embed = discord.Embed(
                    title="簡易計算機",
                    description=f"```{calculate_value}{default_value[len(calculate_value):40]}```",
                    color=discord.Colour.blue(),
                    timestamp=datetime.datetime.utcnow()
                )

                embed.set_footer(text="Calculate 計算機",icon_url=bot_icon_url)

                await interaction.response.edit_message(embed=embed,view=view)

        async def button4callback(interaction:discord.Interaction):
            if interaction.user != ctx.author:
                await interaction.response.send_message("❌非此指令使用者無法操控!",ephemeral=True)
            else:
                nonlocal calculate_value
                calculate_value += "4"

                embed = discord.Embed(
                    title="簡易計算機",
                    description=f"```{calculate_value}{default_value[len(calculate_value):40]}```",
                    color=discord.Colour.blue(),
                    timestamp=datetime.datetime.utcnow()
                )

                embed.set_footer(text="Calculate 計算機",icon_url=bot_icon_url)

                await interaction.response.edit_message(embed=embed,view=view)

        async def button5callback(interaction:discord.Interaction):
            if interaction.user != ctx.author:
                await interaction.response.send_message("❌非此指令使用者無法操控!",ephemeral=True)
            else:
                nonlocal calculate_value
                calculate_value += "5"

                embed = discord.Embed(
                    title="簡易計算機",
                    description=f"```{calculate_value}{default_value[len(calculate_value):40]}```",
                    color=discord.Colour.blue(),
                    timestamp=datetime.datetime.utcnow()
                )

                embed.set_footer(text="Calculate 計算機",icon_url=bot_icon_url)

                await interaction.response.edit_message(embed=embed,view=view)

        async def button6callback(interaction:discord.Interaction):
            if interaction.user != ctx.author:
                await interaction.response.send_message("❌非此指令使用者無法操控!",ephemeral=True)
            else:
                nonlocal calculate_value
                calculate_value += "6"

                embed = discord.Embed(
                    title="簡易計算機",
                    description=f"```{calculate_value}{default_value[len(calculate_value):40]}```",
                    color=discord.Colour.blue(),
                    timestamp=datetime.datetime.utcnow()
                )

                embed.set_footer(text="Calculate 計算機",icon_url=bot_icon_url)

                await interaction.response.edit_message(embed=embed,view=view)

        async def button7callback(interaction:discord.Interaction):
            if interaction.user != ctx.author:
                await interaction.response.send_message("❌非此指令使用者無法操控!",ephemeral=True)
            else:
                nonlocal calculate_value
                calculate_value += "7"

                embed = discord.Embed(
                    title="簡易計算機",
                    description=f"```{calculate_value}{default_value[len(calculate_value):40]}```",
                    color=discord.Colour.blue(),
                    timestamp=datetime.datetime.utcnow()
                )

                embed.set_footer(text="Calculate 計算機",icon_url=bot_icon_url)

                await interaction.response.edit_message(embed=embed,view=view)

        async def button8callback(interaction:discord.Interaction):
            if interaction.user != ctx.author:
                await interaction.response.send_message("❌非此指令使用者無法操控!",ephemeral=True)
            else:
                nonlocal calculate_value
                calculate_value += "8"

                embed = discord.Embed(
                    title="簡易計算機",
                    description=f"```{calculate_value}{default_value[len(calculate_value):40]}```",
                    color=discord.Colour.blue(),
                    timestamp=datetime.datetime.utcnow()
                )

                embed.set_footer(text="Calculate 計算機",icon_url=bot_icon_url)

            await interaction.response.edit_message(embed=embed,view=view)

        async def button9callback(interaction:discord.Interaction):
            if interaction.user != ctx.author:
                await interaction.response.send_message("❌非此指令使用者無法操控!",ephemeral=True)
            else:
                nonlocal calculate_value
                calculate_value += "9"

                embed = discord.Embed(
                    title="簡易計算機",
                    description=f"```{calculate_value}{default_value[len(calculate_value):40]}```",
                    color=discord.Colour.blue(),
                    timestamp=datetime.datetime.utcnow()
                )

                embed.set_footer(text="Calculate 計算機",icon_url=bot_icon_url)

                await interaction.response.edit_message(embed=embed,view=view)

        async def button0callback(interaction:discord.Interaction):
            if interaction.user != ctx.author:
                await interaction.response.send_message("❌非此指令使用者無法操控!",ephemeral=True)
            else:
                nonlocal calculate_value
                calculate_value += "0"

                embed = discord.Embed(
                    title="簡易計算機",
                    description=f"```{calculate_value}{default_value[len(calculate_value):40]}```",
                    color=discord.Colour.blue(),
                    timestamp=datetime.datetime.utcnow()
                )

                embed.set_footer(text="Calculate 計算機",icon_url=bot_icon_url)

                await interaction.response.edit_message(embed=embed,view=view)

        async def dotbuttoncallback(interaction:discord.Interaction):
            if interaction.user != ctx.author:
                await interaction.response.send_message("❌非此指令使用者無法操控!",ephemeral=True)
            else:
                nonlocal calculate_value
                calculate_value += "."

                embed = discord.Embed(
                    title="簡易計算機",
                    description=f"```{calculate_value}{default_value[len(calculate_value):40]}```",
                    color=discord.Colour.blue(),
                    timestamp=datetime.datetime.utcnow()
                )

                embed.set_footer(text="Calculate 計算機",icon_url=bot_icon_url)

                await interaction.response.edit_message(embed=embed,view=view)

        async def equal_buttoncallback(interaction:discord.Interaction):
            if interaction.user != ctx.author:
                await interaction.response.send_message("❌非此指令使用者無法操控!",ephemeral=True)
            else:
                nonlocal calculate_value

                answer = calculator(calculate_value)

                if answer == None or calculate_value:
                    answer = calculate_value
                
                else:
                    calculate_value = ""

                embed = discord.Embed(
                    title="**簡易計算機**",
                    description=f"```{answer}{default_value[len(answer):40]}```",
                    color=discord.Colour.blue(),
                    timestamp=datetime.datetime.utcnow()
                )

                embed.set_footer(text="Calculate 計算機",icon_url=bot_icon_url)

                await interaction.response.edit_message(embed=embed,view=view)
        
        async def plusbuttoncallback(interaction:discord.Interaction):
            if interaction.user != ctx.author:
                await interaction.response.send_message("❌非此指令使用者無法操控!",ephemeral=True)
            else:
                nonlocal calculate_value
                calculate_value += "+"

                embed = discord.Embed(
                    title="簡易計算機",
                    description=f"```{calculate_value}{default_value[len(calculate_value):40]}```",
                    color=discord.Colour.blue(),
                    timestamp=datetime.datetime.utcnow()
                )

                embed.set_footer(text="Calculate 計算機",icon_url=bot_icon_url)

                await interaction.response.edit_message(embed=embed,view=view)

        async def minusbuttoncallback(interaction:discord.Interaction):
            if interaction.user != ctx.author:
                await interaction.response.send_message("❌非此指令使用者無法操控!",ephemeral=True)
            else:
                nonlocal calculate_value
                calculate_value += "-"

                embed = discord.Embed(
                    title="簡易計算機",
                    description=f"```{calculate_value}{default_value[len(calculate_value):40]}```",
                    color=discord.Colour.blue(),
                    timestamp=datetime.datetime.utcnow()
                )

                embed.set_footer(text="Calculate 計算機",icon_url=bot_icon_url)

                await interaction.response.edit_message(embed=embed,view=view)

        async def multiplybuttoncallback(interaction:discord.Interaction):
            if interaction.user != ctx.author:
                await interaction.response.send_message("❌非此指令使用者無法操控!",ephemeral=True)
            else:
                nonlocal calculate_value
                calculate_value += "×"

                embed = discord.Embed(
                    title="簡易計算機",
                    description=f"```{calculate_value}{default_value[len(calculate_value):40]}```",
                    color=discord.Colour.blue(),
                    timestamp=datetime.datetime.utcnow()
                )

                embed.set_footer(text="Calculate 計算機",icon_url=bot_icon_url)

                await interaction.response.edit_message(embed=embed,view=view)

        async def divisionbuttoncallback(interaction:discord.Interaction):
            if interaction.user != ctx.author:
                await interaction.response.send_message("❌非此指令使用者無法操控!",ephemeral=True)
            else:
                nonlocal calculate_value
                calculate_value += "÷"

                embed = discord.Embed(
                    title="簡易計算機",
                    description=f"```{calculate_value}{default_value[len(calculate_value):40]}```",
                    color=discord.Colour.blue(),
                    timestamp=datetime.datetime.utcnow()
                )

                embed.set_footer(text="Calculate 計算機",icon_url=bot_icon_url)

                await interaction.response.edit_message(embed=embed,view=view)

        async def ACbuttoncallback(interaction:discord.Interaction):
            if interaction.user != ctx.author:
                await interaction.response.send_message("❌非此指令使用者無法操控!",ephemeral=True)
            else:
                nonlocal calculate_value
                calculate_value = " "

                embed = discord.Embed(
                    title="簡易計算機",
                    description=f"```{calculate_value}{default_value[len(calculate_value):40]}```",
                    color=discord.Colour.blue(),
                    timestamp=datetime.datetime.utcnow()
                )

                embed.set_footer(text="Calculate 計算機",icon_url=bot_icon_url)

                await interaction.response.edit_message(embed=embed,view=view)

        async def Cbuttoncallback(interaction:discord.Interaction):
            if interaction.user != ctx.author:
                await interaction.response.send_message("❌非此指令使用者無法操控!",ephemeral=True)
            else:
                nonlocal calculate_value
                calculate_value = calculate_value[:1]

                embed = discord.Embed(
                    title="簡易計算機",
                    description=f"```{calculate_value}{default_value[len(calculate_value):40]}```",
                    color=discord.Colour.blue(),
                    timestamp=datetime.datetime.utcnow()
                )

                embed.set_footer(text="Calculate 計算機",icon_url=bot_icon_url)

                await interaction.response.edit_message(embed=embed,view=view)

        button0.callback = button0callback
        button1.callback = button1callback
        button2.callback = button2callback
        button3.callback = button3callback
        button4.callback = button4callback
        button5.callback = button5callback
        button6.callback = button6callback
        button7.callback = button7callback
        button8.callback = button8callback
        button9.callback = button9callback
        dot_button.callback = dotbuttoncallback
        equal_button.callback = equal_buttoncallback
        plus_button.callback = plusbuttoncallback
        minus_button.callback = minusbuttoncallback
        multiply_button.callback = multiplybuttoncallback
        division_button.callback = divisionbuttoncallback
        AC_button.callback = ACbuttoncallback
        C_button.callback = Cbuttoncallback

        await ctx.send(embed=embed,view=view)

def setup(bot):
    bot.add_cog(Tool(bot))