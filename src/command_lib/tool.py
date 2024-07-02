from discord.ext import commands
import lib.functions as tool
import discord
import datetime

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

            chest_embed.set_footer(text="Ganyu | 原神帳號查詢",icon_url=...)

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

            recembed.set_footer(text="Ganyu | 疑難排解",icon_url=...)

            await interaction.response.edit_message(embed=recembed,view=backview)

        serverkeywordsbutton.callback = skbtncallback
        recipebutton.callback = recipebuttoncallnack
    
    embed.set_footer(text="Ganyu | 原神帳號查詢",icon_url=...)

    if isinstance(ctx,commands.Context):
        await ctx.send(embed=embed,view=view)

    elif isinstance(ctx,discord.ApplicationContext):
        await ctx.respond(embed=embed,view=view)