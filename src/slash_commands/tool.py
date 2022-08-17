from lib.function import translate, SendBGM, bullshit, calculator
from lib.bot_config import bot_icon_url 
from core.classes import Cog_ExtenSion
from command_lib import tool
import datetime
import discord

class SlashTool(Cog_ExtenSion):
    
    @discord.application_command(description = "將任何語言翻譯成中文!")
    async def translate(self,ctx,language : discord.Option(str,"選擇要翻譯成的語言",choices=["繁中","簡中","英語","日語","印尼語"]),*,text=None):
        await tool.Translate(ctx,language,text,"slash")

    @discord.application_command(description="字數轉換器")
    async def words(self,ctx: discord.ApplicationContext,*,text : discord.Option(str,"輸入您要轉換的句子")):
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

        await ctx.respond(embed=embed)
        SendBGM(ctx)

    @discord.application_command(description="唬爛產生器")
    async def bullshit(self,ctx:discord.ApplicationContext,topic:discord.Option(str,"主題")=None,minlen:discord.Option(int,"字數(上限1000)")=None):
        await tool.Bullshit(ctx,topic,minlen,"slash")

    @discord.application_command(description="計算機")
    async def math(self,ctx:discord.ApplicationContext,formula:discord.Option(str,"算式")=None):
        if formula != None:
            answer = calculator(formula)
            embed = discord.Embed(
                title="計算機",
                description="結果如下",
                color=discord.Colour.random(),
                timestamp=datetime.datetime.utcnow()
            )

            embed.set_footer(text="Calculate 計算機",icon_url=bot_icon_url)

            embed.add_field(
                name="原始算式",
                value=f"```{formula}```",
                inline=False
            )

            embed.add_field(
                name="計算結果",
                value=f"```{answer}```",
                inline=False
            )

            await ctx.respond(embed = embed)

        else:
            default_value = "                                        "#don't edit!

            calculate_value = ""

            embed = discord.Embed(
                title="計算機",
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

                    if answer == None:
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
                    calculate_value = calculate_value[:-1]

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

            await ctx.send_response(embed=embed,view=view)
            SendBGM(ctx)

def setup(bot):
    bot.add_cog(SlashTool(bot))