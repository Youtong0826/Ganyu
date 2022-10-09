from discord.ext import commands
from lib.bot_config import bot_icon_url
import lib.function as tool
import discord
import datetime

async def translate(ctx,**kwargs):
    google_translate_icon_url = "https://th.bing.com/th/id/R.93d2c8f15964faae1e75331caf7d8fe0?rik=vl9rlcN9fh1oEw&pid=ImgRaw&r=0"
    
    translate_to = {
        "繁中":"zh-TW",
        "簡中":"zh-CN",
        "英語":"en",
        "日語":"ja",
        "印尼語":"id"
    }

    language:str = kwargs.get("language","繁中")
    text:str = kwargs.get("text")
    print(tool.translate("haha",translate_to[language]))
    if text != None:
        translated_text = tool.translate(text,translate_to[language])
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
            name=language,
            value=f"```{translated_text}```",
            inline=False
        )
    
    else:
        embed = discord.Embed(
            title="歡迎使用翻譯小工具!",
            description="此指令可以將各種語言翻譯成你想要的語言\n使用方法:/translate `要翻譯成的語言` `文字`",
            color=discord.Colour.random(),
            timestamp=datetime.datetime.utcnow()
        )
    
    embed.set_thumbnail(url=google_translate_icon_url)
    embed.set_footer(text="translate",icon_url=bot_icon_url)

    if isinstance(ctx,commands.Context):
        await ctx.send(embed=embed)

    elif isinstance(ctx,discord.ApplicationContext):
        await ctx.respond(embed=embed)

    tool.SendBGM(ctx)

async def words(ctx,text):
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
            title="使用 /words 來轉換字數!",
            description="使用方法: /words `句子`"
        )

    embed.color = discord.Colour.random()
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text="字數轉換器",icon_url=bot_icon_url)

    if isinstance(ctx,commands.Context):
        await ctx.send(embed=embed)

    elif isinstance(ctx,discord.ApplicationContext):
        await ctx.respond(embed=embed)

    tool.SendBGM(ctx)

async def bullshit(ctx,topic,minlen):
    if topic and minlen != None:

        try:
            artcle = tool.bullshit(topic,minlen)

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
            title="使用 /bullshit唬爛產生器來生成文章!",
            description="使用方法 /bullshit `主題(如有空格需要用\"包起來)` `字數(上限1000)`"
        )
    
    embed.color = discord.Colour.random()
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text="唬爛產生器",icon_url = bot_icon_url)
    
    if isinstance(ctx,commands.Context):
        await ctx.send(embed=embed)

    elif isinstance(ctx,discord.ApplicationContext):
        await ctx.respond(embed=embed)

    tool.SendBGM(ctx)

async def math(ctx,formula):
    if formula != None:
        answer = tool.calculator(formula)
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

        if isinstance(ctx,commands.Context):
            await ctx.send(embed=embed)

        elif isinstance(ctx,discord.ApplicationContext):
            await ctx.respond(embed=embed)

    else:
        default_value = "                                        " #don't edit it!

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
            custom_id="math_1",
            label="1",
            row=1
        )

        button2 = discord.ui.Button(
            style=discord.ButtonStyle.primary,
            custom_id="math_2",
            label="2",
            row=1
        )

        button3 = discord.ui.Button(
            style=discord.ButtonStyle.primary,
            custom_id="math_3",
            label="3",
            row=1
        )

        button4 = discord.ui.Button(
            style=discord.ButtonStyle.primary,
            custom_id="math_4",
            label="4",
            row=2
        )

        button5 = discord.ui.Button(
            style=discord.ButtonStyle.primary,
            custom_id="math_5",
            label="5",
            row=2
        )

        button6 = discord.ui.Button(
            style=discord.ButtonStyle.primary,
            custom_id="math_6",
            label="6",
            row=2
        )

        button7 = discord.ui.Button(
            style=discord.ButtonStyle.primary,
            custom_id="math_7",
            label="7",
            row=3
        )

        button8 = discord.ui.Button(
            style=discord.ButtonStyle.primary,
            custom_id="math_8",
            label="8",
            row=3
        )

        button9 = discord.ui.Button(
            style=discord.ButtonStyle.primary,
            custom_id="math_9",
            label="9",
            row=3
        )

        button0 = discord.ui.Button(
            style=discord.ButtonStyle.primary,
            custom_id="math_0",
            label="0",
            row=4
        )

        dot_button = discord.ui.Button(
            style=discord.ButtonStyle.gray,
            custom_id="math_.",
            label=".",
            row=4
        )

        equal_button = discord.ui.Button(
            style=discord.ButtonStyle.success,
            custom_id="math_=",
            label="=",
            row=4
        )

        plus_button = discord.ui.Button(
            style=discord.ButtonStyle.gray,
            custom_id="math_+",
            label="+",
            row=1
        )

        minus_button = discord.ui.Button(
            style=discord.ButtonStyle.gray,
            custom_id="math_-",
            label="-",
            row=2
        )

        multiply_button = discord.ui.Button(
            style=discord.ButtonStyle.gray,
            custom_id="math_×",
            label="×",
            row=3
        )

        division_button = discord.ui.Button(
            style=discord.ButtonStyle.gray,
            custom_id="math_÷",
            label="÷",
            row=4
        )

        AC_button = discord.ui.Button(
            style=discord.ButtonStyle.danger,
            custom_id="math_AC",
            label="AC",
            row=1
        )

        C_button = discord.ui.Button(
            style=discord.ButtonStyle.danger,
            custom_id="math_C",
            label="C",
            row=2
        )

        buttons = [
            button1, button2, button3, plus_button, AC_button,
            button4, button5, button6, minus_button, C_button,
            button7, button8, button9, multiply_button,
            dot_button, button0, equal_button, division_button,
        ]

        async def callback(interaction:discord.Interaction):
            if interaction.user != ctx.author:
                await interaction.response.send_message("❌非此指令使用者無法操控!",ephemeral=True)

            else:
                nonlocal calculate_value
                if interaction.custom_id[5:] == "=":
                    result = tool.calculator(calculate_value)
                    calculate_value = result if result is not None else ...

                elif interaction.custom_id == "math_AC":calculate_value = " "

                elif interaction.custom_id == "math_C":calculate_value = calculate_value[:-1]

                else:calculate_value += interaction.custom_id[5:]
    
                embed = discord.Embed(
                    title="簡易計算機",
                    description=f"```{calculate_value}{default_value[len(calculate_value):40]}```",
                    color=discord.Colour.blue(),
                    timestamp=datetime.datetime.utcnow()
                )

                embed.set_footer(text="Calculate 計算機",icon_url=bot_icon_url)
                await interaction.response.edit_message(embed=embed,view=view)

        for button in buttons: 
            view.add_item(button)
            button.callback = callback

        if isinstance(ctx,commands.Context):
            await ctx.send(embed=embed,view=view)

        elif isinstance(ctx,discord.ApplicationContext):
            await ctx.respond(embed=embed,view=view)

        tool.SendBGM(ctx)

async def genshininfo(ctx,uid,server):

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
    
        data = tool.getGenshininfo(uid,server)#811312758

        serverkw =  {
            'os_usa': '美服',
            'os_euro': '歐服',
            'os_asia': '亞服',
            'os_cht': '台港澳服'
        }

        avatars_id = {
            "10000002":"神里綾華",
            "10000003":"琴",
            "10000005":"空",
            "10000006":"麗莎",
            "10000007":"瑩",
            "100000014":"芭芭拉",
            "100000015":"凱亞",
            "100000016":"迪盧克",
            "100000020":"雷澤",
            "100000021":"安柏",
            "100000022":"溫迪",
            "100000023":"香菱",
            "100000024":"北斗",
            "100000025":"魈",
            "100000026":"行秋",
            "100000027":"凝光",
            "100000029":"可莉",
            "100000030":"鍾離",
            "100000031":"菲謝爾", 
            "100000032":"班尼特",
            "100000033":"達達利亞",
            "100000034":"諾艾爾",
            "100000035":"七七",
            "100000036":"重雲",
            "100000037":"甘雨",
            "100000038":"阿貝多",
            "100000039":"迪奧娜",
            "100000041":"莫娜",
            "100000042":"刻晴",
            "100000043":"砂糖",
            "100000044":"辛焱",
            "100000045":"羅莎莉亞",
            "100000046":"胡桃",
            "100000047":"楓原萬葉",
            "100000048":"煙緋",
            "100000049":"宵宮",
            "100000050":"托馬",
            "100000051":"優菈",
            "100000052":"雷電將軍",
            "100000053":"早柚",
            "100000054":"珊瑚宮心海",
            "100000055":"五郎",
            "100000056":"九條紗羅",
            "100000057":"荒龍一斗",
            "100000058":"八重神子",
            "100000062":"亞羅伊",
            "100000063":"申鶴",
            "100000064":"雲堇",
            "100000066":"神里綾人"
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
            description=f"伺服器:**{(serverkw[role['region']]).upper()}**",#{role['level']}級
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

            chest_embed.set_footer(text="Ganyu | 原神帳號查詢",icon_url=bot_icon_url)

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

        recipebutton = discord.ui.Button(
            style=discord.ButtonStyle.primary,
            label="使用詳細說明 | 為什麼會出現錯誤?",
            emoji="📕"
        )

        view.add_item(serverkeywordsbutton)
        view.add_item(recipebutton)

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
        
        async def recipebuttoncallnack(interaction:discord.Interaction):
            recembed = discord.Embed(
                title="使用詳細說明 | 為什麼會出現錯誤?",
                description="此指令是採用來自HoYoLab的API 如果看不到內容可能是因為您的戰績並沒有對外公布 前往HoYoLab設定後即可看到您的帳號資訊了 若使中出現錯誤的話請連絡我或是使用`report`功能",
                color=discord.Colour.nitro_pink(),
            )

            recembed.set_footer(text="Ganyu | 疑難排解",icon_url=bot_icon_url)

            await interaction.response.edit_message(embed=recembed,view=backview)

        serverkeywordsbutton.callback = skbtncallback
        recipebutton.callback = recipebuttoncallnack
    
    embed.set_footer(text="Ganyu | 原神帳號查詢",icon_url=bot_icon_url)

    if isinstance(ctx,commands.Context):
        await ctx.send(embed=embed,view=view)

    elif isinstance(ctx,discord.ApplicationContext):
        await ctx.respond(embed=embed,view=view)

    tool.SendBGM(ctx)

async def wikiInfo(ctx,keywords:str,bot=None):
    keywords_split = keywords.split()
    results = tool.wiki_search(tuple(keywords_split))
    if results == None: await ctx.respond(f"{bot.mention} 徹徹底底地搜索了一遍 但還是找不到結果..")

    emojis = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟"]
    options = []
    for index in range(len(results)):
        options.append(discord.SelectOption(
            label=results[index],
            value=f"wiki_{results[index]}",
            emoji=emojis[index]
        ))

    select = discord.ui.Select(
        placeholder="選擇相關的搜索結果",
        options=options,
        custom_id="Wiki_Select"
    )

    view = discord.ui.View(timeout=None)
    view.add_item(select)

    async def select_response(interaction:discord.Interaction):
        if interaction.custom_id == "Wiki_Select":
            info = {}
            for result in results:
                if select.values[0] == "wiki_" + result:
                    info["description"] = tool.wiki_info(result,3)
                    info["title"] = result
                    break

            embed= discord.Embed(
                url=f"https://zh.wikipedia.org/wiki/{info['title']}",
                title=info["title"],
                description=info["description"],
                color=discord.Colour.nitro_pink(),
                timestamp=datetime.datetime.utcnow()
            )

            wikipedia_icon = "https://th.bing.com/th/id/R.d451e7b1661d71fc68ca02b19137497b?rik=MjNkZivLBibrOQ&pid=ImgRaw&r=0"

            embed.set_thumbnail(url=wikipedia_icon)

            embed.set_footer(text="Wikipedia.org",icon_url=bot_icon_url)

            await interaction.response.edit_message(embed=embed,view=view)

    select.callback = select_response
    
    embed = discord.Embed(
        title=f"以下為有關\"{keywords}\"的搜索結果",
        color=discord.Colour.nitro_pink()
    )

    if isinstance(ctx,commands.Context):
        await ctx.send(embed=embed,view=view)

    elif isinstance(ctx,discord.ApplicationContext):
        await ctx.respond(embed=embed,view=view)


