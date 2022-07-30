import discord
import datetime
from lib.function import SendBGM,translate,bullshit,calculator,getGenshininfo
from lib.bot_config import bot_icon_url

async def Translate(ctx,text,type=["command","slash"]):
    google_translate_icon_url = "https://th.bing.com/th/id/R.93d2c8f15964faae1e75331caf7d8fe0?rik=vl9rlcN9fh1oEw&pid=ImgRaw&r=0"

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

    if type == "command":
        await ctx.send(embed = embed)

    if type == "slash":
        await ctx.respond(embed = embed)

    SendBGM(ctx)

async def Words(ctx,text,type=["command","slash"]):
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

    if type == "command":
        await ctx.send(embed = embed)

    if type == "slash":
        await ctx.respond(embed = embed)

    SendBGM(ctx)

async def Bullshit(ctx,topic,minlen,type=["command","slash"]):
    if topic and minlen != None:

        try:
            artcle = bullshit(topic,minlen)

        except:
            if type == "command":
                await ctx.send("發生錯誤 請求未受到API回應")

            if type == "slash":
                await ctx.respond("發生錯誤 請求未受到回應")

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
    
    if type == "command":
        await ctx.send(embed = embed)

    if type == "slash":
        await ctx.respond(embed = embed)

    SendBGM(ctx)

async def Math(ctx,formula,type=["command","slash"]):
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

        if type == "command":
            await ctx.send(embed=embed)

        elif type == "slash":
            await ctx.respond(embed=embed) 

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

        if type == "command":
            await ctx.send(embed=embed)

        elif type == "slash":
            await ctx.respond(embed=embed) 

        SendBGM(ctx)

async def GenshinInfo(ctx,uid,server,type=["command","slash"]):

    backbutton = discord.ui.Button(
        style=discord.ButtonStyle.primary,
        label="back",
        emoji="🔙"
    )

    backview = discord.ui.View(timeout=None)
    backview.add_item(backbutton)

    async def backbuttoncallback(interaction : discord.Interaction):
        await interaction.response.edit_message(embed=embed,view=view)

    backbutton.callback = backbuttoncallback
    if uid != None:

        server = "os_" + server
        
        print(server)
    
        data = getGenshininfo(uid,server)#811312758

        server =  {
            'os_usa': '美服',
            'os_euro': '歐服',
            'os_asia': '亞服',
            'os_cht': '台港澳服'
        }

        role = data["role"]
        avatars = data["avatars"]
        city_explorations = data["city_explorations"]
        stats = data["stats"]
        world_explorations = data["world_explorations"]

        info = {}

        info["🔹 等級"] = f'**{role["level"]}**'
        info["📈 活躍天數"] = f'**{stats["active_day_number"]}**'
        info["📜 成就"] = f'**{stats["achievement_number"]}**'
        info["🐬 角色"] = f'**{stats["avatar_number"]}**'
        info["🪄 傳送錨點"] = f"**{stats['way_point_number']}** 已解鎖"
        info["⚖️ 深境螺旋"] = f"**{stats['spiral_abyss']}**"

        embed = discord.Embed(
            title=f"暱稱: {role['nickname']}",
            description=f"伺服器:**{(role['region'][3:7]).upper()}**",#{role['level']}級
            color=discord.Colour.nitro_pink(),
            timestamp=datetime.datetime.utcnow()
        )

        for n in info:
            embed.add_field(name=n,value=info[n])

        view = discord.ui.View(timeout=None)

        chestbutton = discord.ui.Button(
            style=discord.ButtonStyle.success,
            label="獲得的寶箱",
            emoji="🎁",
        )

        view.add_item(chestbutton)

        async def chestbuttoncallback(interaction:discord.Interaction):
            chest_data = {
                "普通的寶箱":stats["common_chest_number"],
                "精緻的寶箱":stats["exquisite_chest_number"],
                "珍貴的寶箱":stats["precious_chest_number"],
                "華麗的寶箱":stats["luxurious_chest_number"],
                "奇饋的寶箱":stats["magic_chest_number"]
            }

            chest_embed = discord.Embed(
                title="獲得的寶箱",
                color=discord.Colour.nitro_pink(),
                timestamp=datetime.datetime.utcnow()
            )

            for n in chest_data:
                chest_embed.add_field(name=n,value=chest_data[n])

            await interaction.response.edit_message(embed=chest_embed,view=backview)
        
        chestbutton.callback = chestbuttoncallback

    else:
        embed = discord.Embed(
            title="使用`genshin`來查詢你的原神帳號!",
            description="用法: `genshin` `uid` `伺服器(關鍵字)`"
        )

        view = discord.ui.View(timeout=None)

        serverkeywordsbutton = discord.ui.Button(
            style=discord.ButtonStyle.success,
            label="查看伺服器對照表",
            emoji="🗄️"
        )

        view.add_item(serverkeywordsbutton)

        async def skbtncallback(interaction:discord.Interaction):
            
            skembed = discord.Embed(
                title="伺服器關鍵字對照表",
                description="\
                    cht : 台港澳服\n\
                    asia : 亞服\n\
                    euro : 歐服\n\
                    usa : 美服\
                "
            )

            await interaction.response.edit_message(embed=skembed,view=backview)

        serverkeywordsbutton.callback = skbtncallback

    
    embed.set_footer(text="Ganyu | 原神帳號查詢",icon_url=bot_icon_url)

    if type == "command":
        await ctx.send(embed = embed,view=view)

    if type == "slash":
        await ctx.respond(embed = embed,view=view)

    SendBGM(ctx)


