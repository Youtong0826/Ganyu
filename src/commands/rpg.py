import random
import discord
import datetime
import json
from discord.ext import commands
from core.classes import Cog_ExtenSion
from lib.bot_config import bot_icon_url

numbers = [
            ":one:",
            ":two:",
            ":three:",
            ":four:",
            ":five:",
            ":six:",
            ":seven:",
            ":eight:",
            ":nine:",
            ":keycap_ten:"
        ]
def addDB(db,file):
    with open(f"res/db/{file}", "w", encoding="utf-8") as f:
        return f.write(
            json.dumps(
                db,
                ensure_ascii=False,
                indent=4,
                separators=(',', ': ')
            )
        )

def getRPGDB():
    with open("res/db/rpg.json", "r", encoding="utf-8") as f:
        return json.loads(f.read())

def addRPGDB(db):
    with open("res/db/rpg.json", "w", encoding="utf-8") as f:
        return f.write(
            json.dumps(
                db,
                ensure_ascii=False,
                indent=4,
                separators=(',', ': ')
            )
        )

def defaultrpg(member:discord.Member,job):
    rpgdb = getRPGDB()
    id = str(member.id)
    rpgdb[id] = {
        "name": member.name,
        "job": job,
        "exp": 0,
        "level": 0,
        "coin": 0,
        "hp": 100,
        "atk": 1,
        "def" : 1
    }
    addRPGDB(rpgdb)  # {f'{id}':f'{job}'})

def addexp(id,exp):
    rpgdb = getRPGDB()
    id = str(id)
    assets = rpgdb[id]
    assets['exp'] += exp
    rpgdb[id] = assets
    addRPGDB(rpgdb)

def addlevel(id,level):
    rpgdb = rpg.getRPGDB()
    id = str(id)
    assets = rpgdb[id]
    assets['level'] += level
    rpgdb[id] = assets
    addRPGDB(rpgdb)

def addcoin(id,coin):
    rpgdb = rpg.getRPGDB()
    id = str(id)
    assets = rpgdb[id]
    assets['coin'] += coin
    rpgdb[id] = assets
    addRPGDB(rpgdb)

def addhp(id,hp):
    rpgdb = rpg.getRPGDB()
    id = str(id)
    assets = rpgdb[id]
    assets['hp'] += hp
    rpgdb[id] = assets
    addRPGDB(rpgdb)

def addatk(id,atk):
    rpgdb = rpg.getRPGDB()
    id = str(id)
    assets = rpgdb[id]
    assets['atk'] += atk
    rpgdb[id] = assets
    addRPGDB(rpgdb)

def adddef(id,dEf):
    rpgdb = rpg.getRPGDB()
    id = str(id)
    assets = rpgdb[id]
    assets['def'] += dEf
    rpgdb[id] = assets
    addRPGDB(rpgdb)

def getrpg_entity():
    with open("res/db/rpg_entity.json", "r", encoding="utf-8") as f:
        return json.loads(f.read())

def getjob(id):
    id = str(id)
    rpgdb = getRPGDB()
    if f"{id}" not in f"{rpgdb}":
        rpgdb[id] = "無"
    return rpgdb[id]

def have_job(id):
    id = str(id)
    rpgdb = getRPGDB()
    if f"{id}" in f"{rpgdb}":
        job =["Knight","Shooter","Mage","Assassin","Tank"]

        for n in job:
            if n in rpgdb[id].get("job"):
                return True

            return False

    else:
        return False

def top(type):  # type=level or coin
    rpgdb = getRPGDB()
    ramtop = {}
    realtop = {}
    time = 0
    for key in rpgdb:
        v = rpgdb[key].get(type)
        name = rpgdb[key].get("name")
        ramtop[name] = v

    top = sorted(ramtop.items(), key=lambda kv: (
        kv[1], kv[0]), reverse=True)
    name = [i[0] for i in top]
    num = [i[1] for i in top]

    for n in range(10):
        realtop[name[n]] = num[n]

    return realtop

def TopEmbed(embed: discord.Embed, namefields: list,valuefields: list ,type) -> discord.Embed:
    if type == "coin":
        for index in range(10):#調整排名的長度
            embed.add_field(
                name=f"{numbers[index]} {namefields[index]}",
                value=f"擁有 **{valuefields[index]}** 冒險幣",
                inline=False
            )
    else:
        for index in range(10):#調整排名的長度
            embed.add_field(
                name=f"{numbers[index]} {namefields[index]}",
                value=f"**LV.{valuefields[index]}** ",
                inline=False
            )

    return embed

class rpg(Cog_ExtenSion):

    have_job = False

    @commands.command()
    async def rpg(self, ctx, key=None):

        user = ctx.author
        id = str(user.id)
        rpgdb = getRPGDB()
        if id in rpgdb:
            default_job = rpgdb[id].get("job")
            default_exp = rpgdb[id].get("exp")
            default_level = rpgdb[id].get("level")
            default_coin = rpgdb[id].get("coin")
            default_name = rpgdb[id].get("name")
            default_atk = rpgdb[id].get("atk")
            default_def = rpgdb[id].get("def")

        if key == "job":
            embed = discord.Embed(
                title="選擇你的職業!",
                color=discord.Colour.random(),
                timestamp=datetime.datetime.utcnow()
            )
            embed.add_field(
                name="**騎士** g!knight",
                value="性能普普沒什麼好講的XD"
            )
            embed.add_field(
                name="**遊俠** g!shooter",
                value="高物傷高敏捷"
            )
            embed.add_field(
                name="**法師** g!mage",
                value=" 沒什麼強的就是法傷超高"
            )
            embed.add_field(
                name="**刺客** g!assassin",
                value="具有較高的敏節度，但是其他屬性不高"
            )
            embed.add_field(
                name="**坦克** g!tank",
                value="不管是物理還是魔法，都具有超高的防禦力"
            )
            embed.add_field(
                name="**隨機職業** g!ranjob",
                value="系統幫你選職業XD"
            )
            embed.set_footer(
                text=f"#職業目前為象徵性的東西 並無實質作用 | Ganyu RPG",
                icon_url=bot_icon_url
            )
            
            main_view = discord.ui.View(timeout=None)

        elif key == "start":
            open = True

            if open:
                if have_job(id):
                    embed = discord.Embed(
                        title="開始你的旅程",
                        description="您目前所在的位置是 凱爾特新手村"
                    )

                    main_view = discord.ui.View(timeout=None)

                    backview = discord.ui.View(timeout=None)

                    profile_button = discord.ui.Button(
                        style=discord.ButtonStyle.primary,
                        label="個資",
                        emoji="📰"
                    )

                    entity_button = discord.ui.Button(
                        style=discord.ButtonStyle.success,
                        label="尋找怪物",
                        emoji="🐍"
                    )

                    back_button = discord.ui.Button(
                        style=discord.ButtonStyle.success,
                        label="back",
                        emoji="🔙"
                    )

                    async def profile_button_callback(interaction : discord.Interaction):

                        user = interaction.user

                        if user.nick == None:
                            nick = user.name

                        else:
                            nick = user.nick

                        if have_job(id):

                            if "Knight" in rpgdb[id].get("job"):
                                job = "騎士"

                            elif "Shooter" in rpgdb[id].get("job"):
                                job = "遊俠"

                            elif "Mage" in rpgdb[id].get("job"):
                                job = "法師"

                            elif "Assassin" in rpgdb[id].get("job"):
                                job = "刺客"

                            elif "Tank" in rpgdb[id].get("job"):
                                job = "坦克"

                            else:
                                job = "無"

                            level = rpgdb[id].get('level')
                            coin = rpgdb[id].get('coin')
                            hp = rpgdb[id].get('hp')
                            atk = rpgdb[id].get('atk')
                            Def = rpgdb[id].get('def')

                        else:
                            job = "無"
                            level = 0
                            coin = 0
                            hp = 0
                            atk = 0
                            Def = 0

                        embed = discord.Embed(
                            title=f"**{nick}的RPG資訊**",
                            color=discord.Colour.random(),
                            timestamp=datetime.datetime.utcnow()
                        )
                        embed.add_field(
                            name="**職業**",
                            value=f"{job}"
                        )
                        embed.add_field(
                            name="**等級**",
                            value=f"Lv.{level}"
                        )
                        embed.add_field(
                            name="**血量**",
                            value=f"{hp}"
                        )
                        embed.add_field(
                            name="**攻擊力**",
                            value=f"{atk}"
                        )
                        embed.add_field(
                            name="**防禦力**",
                            value=f"{Def}"
                        )
                        embed.add_field(
                            name="**冒險幣**",
                            value=f"{coin} $"
                        )
                        embed.set_footer(
                            text=f"RPG Profile",
                            icon_url=bot_icon_url
                        )

                        await interaction.response.edit_message(embed=embed, view=backview)

                    async def back_button_callback(interaction):
                        await interaction.response.edit_message(embed=embed, view=main_view)

                    async def entity_button_callback(interaction:discord.Interaction):
                        entity_place = ["村莊旁邊的草原", "村莊旁邊的湖裡","村莊旁邊的樹林里", "村長老婆的房間裡", "村子的井裡", "村子旁邊的洞窟裡"]
                        entity_Feeling = ["生氣的", "開心的", "沮喪的", "失落的","憤怒的", "興奮的", "難過的", "肚子餓的", "想睡覺的"]

                        entities_db = getrpg_entity()
                        entitys = []
                        user = interaction.user

                        for n in entities_db:
                            entitys.append(n)

                        select_entity = random.choice(entitys)

                        embed = discord.Embed(
                            title=f"成功在 {random.choice(entity_place)} 找到 一隻{random.choice(entity_Feeling)}{entities_db[select_entity].get('name')}",
                        )

                        embed.add_field(
                            name="攻擊力 ATK",
                            value=f"**{entities_db[select_entity].get('atk')}**",
                            inline=False
                        )
                        embed.add_field(
                            name="防禦力 DEF",
                            value=f"**{entities_db[select_entity].get('def')}**",
                            inline=False
                        )
                        embed.add_field(
                            name="血量 HP",
                            value=f"**{entities_db[select_entity].get('hp')}**",
                            inline=False
                        )

                        entity_view = discord.ui.View(timeout=None)

                        run_button = discord.ui.Button(
                            style=discord.ButtonStyle.gray,
                            label="逃跑",
                            emoji="♿"
                        )

                        attack_button = discord.ui.Button(
                            style=discord.ButtonStyle.success,
                            label="攻擊",
                            emoji="🗡️"
                        )

                        async def run_button_callback(interaction):
                            success = random.randint(1, 5)

                            if success == 1:
                                embed = discord.Embed(
                                    title="成功逃跑!",
                                    description="而且沒受到任何傷害!"
                                )
                                embed.add_field(
                                    name="損失",
                                    value="HP -0"
                                )
                                embed.add_field(
                                    name="獲得",
                                    value="EXP +0 #無其他道具"
                                )

                            if success == 2 or 3 or 4:
                                lost_hp = round(
                                    entities_db[select_entity].get('atk')*0.4)

                                
                                embed = discord.Embed(
                                    title="成功逃跑!",
                                    description="但是受到了點小傷害..."
                                )
                                embed.add_field(
                                    name="損失",
                                    value=f"HP -{lost_hp}"
                                )
                                embed.add_field(
                                    name="獲得",
                                    value="EXP +0\n無其他道具"
                                )

                                addhp(id=user.id,hp=-lost_hp)

                            if success == 5:
                                lost_hp = round(
                                    entities_db[select_entity].get('atk')*0.8)
                                

                                embed = discord.Embed(
                                    title="成功逃跑!",
                                    description="但是受到了重傷..."
                                )
                                embed.add_field(
                                    name="損失",
                                    value=f"HP -{lost_hp}"
                                )
                                embed.add_field(
                                    name="獲得",
                                    value="EXP +0\n無其他道具"
                                )
                                addhp(id=user.id,hp=-lost_hp)

                            await interaction.response.edit_message(embed=embed, view=main_view)

                        entity_view.add_item(run_button)
                        run_button.callback = run_button_callback

                        await interaction.response.edit_message(embed=embed, view=entity_view)

                    main_view.add_item(profile_button)
                    main_view.add_item(entity_button)
                    backview.add_item(back_button)

                    back_button.callback = back_button_callback
                    entity_button.callback = entity_button_callback
                    profile_button.callback = profile_button_callback
                
                else:
                    embed = discord.Embed(
                        title="請先選擇職業!"
                    )
                    main_view = discord.ui.View()
            
            else:
                embed = discord.Embed(
                    title="暫未開放",
                    description="基於內部功能尚未開發完畢，此功能暫時關閉，請見諒"
                )
                main_view = discord.ui.View()
                
        elif key == "task":

            if have_job(id):
                embed = discord.Embed(
                    title="**選擇你要前往的副本!**",
                    color=discord.Colour.random()
                )

                embed.add_field(
                    name=""
                )

            else:
                embed = discord.Embed(
                    title="**請先選擇職業!**",
                    color=discord.Colour.random()
                )

            main_view = discord.ui.View(timeout=None)

        elif key == "info":

            if user.nick == None:
                nick = user.name

            else:
                nick = user.nick

            if have_job(id):

                if "Knight" in rpgdb[id].get("job"):
                    job = "騎士"

                elif "Shooter" in rpgdb[id].get("job"):
                    job = "遊俠"

                elif "Mage" in rpgdb[id].get("job"):
                    job = "法師"

                elif "Assassin" in rpgdb[id].get("job"):
                    job = "刺客"

                elif "Tank" in rpgdb[id].get("job"):
                    job = "坦克"

                else:
                    job = "無"

                level = rpgdb[id].get('level')
                coin = rpgdb[id].get('coin')
                hp = rpgdb[id].get('hp')
                atk = rpgdb[id].get('atk')
                Def = rpgdb[id].get('def')

            else:
                job = "無"
                level = 0
                coin = 0
                hp = 0
                atk = 0
                Def = 0

            embed = discord.Embed(
                title=f"**{nick}的RPG資訊**",
                color=discord.Colour.random(),
                timestamp=datetime.datetime.utcnow()
            )
            embed.add_field(
                name="**職業**",
                value=f"{job}"
            )
            embed.add_field(
                name="**等級**",
                value=f"Lv.{level}"
            )
            embed.add_field(
                name="**血量**",
                value=f"{hp}"
            )
            embed.add_field(
                name="**攻擊力**",
                value=f"{atk}"
            )
            embed.add_field(
                name="**防禦力**",
                value=f"{Def}"
            )
            embed.add_field(
                name="**冒險幣**",
                value=f"{coin} $"
            )
            embed.set_footer(
                text=f"{ctx.author.name}",
                icon_url=ctx.author.avatar
            )

            main_view = discord.ui.View(timeout=None)

        elif key == "cointop":
            top_dict = top(type="coin")
            top_name = []
            top_coin = []

            for n in top_dict:
                top_name.append(n)
                top_coin.append(top_dict[n])

            embed = discord.Embed(
                title="冒險幣排名",
                description=f"排名時間:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}",
                color=discord.Colour.random(),
                timestamp=datetime.datetime.utcnow()
            )

            embed = TopEmbed(embed=embed,namefields=top_name,valuefields=top_coin,type="coin")

            embed.set_footer(
                text=f"Coin Top",
                icon_url=bot_icon_url
            )

            main_view = discord.ui.View(timeout=None)

        elif key == "levtop":
            top_dict = top(type="level")
            top_name = []
            top_level = []

            for n in top_dict:
                top_name.append(n)
                top_level.append(top_dict[n])

            embed = discord.Embed(
                title="等級排名",
                description=f"排名時間:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}",
                color=discord.Colour.random(),
                timestamp=datetime.datetime.utcnow()
            )

            embed = TopEmbed(embed=embed,namefields=top_name,valuefields=top_level,type="level")

            embed.set_footer(
                text=f"{ctx.author.name}",
                icon_url=ctx.author.avatar
            )

            main_view = discord.ui.View(timeout=None)

        elif key == "ann":
            embed = discord.Embed(
                title=f"**RPG公告**",
                description="\n**一般#002:**\nRPG系統停滯更新，後續相關資訊將由公告釋出",
                color=discord.Colour.random(),
                timestamp=datetime.datetime.utcnow()
            )
            embed.set_footer(
                text=f"{ctx.author.name}",
                icon_url=ctx.author.avatar
            )

            main_view = discord.ui.View(timeout=None)

        elif key == "kit":
            with open("res/db/DB.json", "r", encoding="utf-8") as f:
                kit_db =  json.loads(f.read())
            open = False
            if open:
                if not id in kit_db:
                    embed = discord.Embed(title=f"**成功領取補償包!**",color=discord.Colour.random())
                    rpg.addrpg(id=f"{id}",job=f"{rpgdb[id].get('job')}",exp=rpgdb[id].get('exp'),level=rpgdb[id].get('level'),name=f"{rpgdb[id].get('name')}",coin=300)
                    kit_db[user.id] = user.name
                    rpg.addDB(kit_db)
                else:
                    embed = discord.Embed(title=f"**您已經領過了!**",color=discord.Colour.random())
            else:
                embed = discord.Embed(
                    title="目前尚無可領取的禮包喔~",
                )
            main_view = discord.ui.View(timeout=None)

        else:
            opening = True

            if opening:
                embed = discord.Embed(
                    title="RPG系統",
                    color=discord.Colour.random()
                )
                embed.add_field(
                    name="g!rpg job",
                    value="選擇你的職業"
                )
                embed.add_field(
                    name="g!rpg start",
                    value="開始你的旅程!"
                )
                embed.add_field(
                    name="g!rpg info",
                    value="查看你的RPG資訊"
                )
                embed.add_field(
                    name="g!rpg ann",
                    value="獲取最新公告"
                )
                embed.add_field(
                    name="g!rpg levtop",
                    value="查看等級排名"
                )
                embed.add_field(
                    name="g!rpg cointop",
                    value="查看冒險幣排名"
                )

            else:
                embed = discord.Embed(
                    title="RPG系統 (暫不開放)",
                    color=discord.Colour.random()
                )

            main_view = discord.ui.View(timeout=None)

        await ctx.send(embed=embed, view=main_view)
        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")
        
    @commands.command()
    async def knight(self, ctx, key=None):
        if key == "y":
            if have_job(ctx.author.id):
                embed = discord.Embed(
                    title="**您已經選過職業了!**",
                    color=discord.Colour.random()
                )
                
            else:
                embed = discord.Embed(
                    title="**成功選擇騎士!**",
                    color=discord.Colour.random()
                    )

                defaultrpg(member=ctx.author,job="Knight")
        else:
            embed = discord.Embed(
                title="騎士 Knight",
                description="作為最基本的職業，騎士擁有強大的攻擊力及優越的防禦，但是他們受到魔法的傷害比其他職業還高．",
                color=discord.Colour.random()
            )

            embed.set_footer(text="輸入g!knight y 來確認選取職業 | Ganyu RPG",icon_url=bot_icon_url)

        await ctx.send(embed=embed)
        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")

    @commands.command()
    async def shooter(self, ctx, key=None):
        if key == "y":
            if have_job(self.author.id):
                embed = discord.Embed(
                title="**您已經選過職業了!**",
                color=discord.Colour.random()
            )

            else:
            
                embed = discord.Embed(
                    title="**成功選擇遊俠!**",
                    color=discord.Colour.random()
                )

                defaultrpg(member=ctx.author,job="Shooter")
        else:
            embed = discord.Embed(
                title="遊俠 Shooter",
                description="遊俠是所有職業裡敏捷度最高的職業，同時也具有較高的物傷，但是其他屬性則相對較低．",
                color=discord.Colour.random()
            )

            embed.set_footer(text="輸入g!shooter y 來確認選取職業 | Ganyu RPG",icon_url=bot_icon_url)

        await ctx.send(embed=embed)
        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")

    @commands.command()
    async def mage(self, ctx, key=None):
        if key == "y":
            if rpg.have_job(ctx.author.id):
                embed = discord.Embed(
                    title="**您已經選過職業了!**",
                    color=discord.Colour.random()
                )

            else:
            
                embed = discord.Embed(
                    title="**成功選擇法師!**",
                    color=discord.Colour.random()
                )

                defaultrpg(member=ctx.author,job="Mage")
        else:
            embed = discord.Embed(
                title="法師 Mage",
                description="法師是所有職業裡法傷最高的職業，如果說刺客是物傷天花板，那法師就是法傷天花板，除此之外其他屬性就普普而已．",
                color=discord.Colour.random()
            )
            
            embed.set_footer(text="輸入g!mage y 來確認選取職業 | Ganyu RPG",icon_url=bot_icon_url)

        await ctx.send(embed=embed)
        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")

    @commands.command()
    async def assassin(self, ctx, key=None):
        if key == "y":
            if rpg.have_job(ctx.author.id):
                embed = discord.Embed(
                    title="**您已經選過職業了!**",
                    color=discord.Colour.random()
                )
            else:
            
                embed = discord.Embed(
                    title="**成功選擇刺客!**",
                    color=discord.Colour.random()
                )

                defaultrpg(member=ctx.author,job="Assassin")

        else:
            embed = discord.Embed(
                title="刺客 Assassin",
                description="物傷的極致，神秘又帥氣的職業，除了超高的物傷外還具有較高的敏捷度，但其他屬性相對較低．", color=discord.Colour.random()
            )

            embed.set_footer(text="輸入g!assassin y 來確認選取職業 | Ganyu RPG",icon_url=bot_icon_url)
            
        await ctx.send(embed=embed)
        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")

    @commands.command()
    async def tank(self, ctx, key=None):
        if key == "y":

            if rpg.have_job(ctx.author.id):
                embed = discord.Embed(
                    title="**您已經選過職業了!**",
                    color=discord.Colour.random()
                )

            else:
                embed = discord.Embed(
                    title="**成功選擇坦克!**",
                    color=discord.Colour.random())

                defaultrpg(member=ctx.author,job="Tank")
        else:
            embed = discord.Embed(
                title="坦克 Tank",
                description="顧名思義，坦克比任何職業的防禦能力都還要高，不管是在物防還是魔防部分都具有超高的防禦，其他屬性則沒什特點．", color=discord.Colour.random()
            )
            
            embed.set_footer(text="輸入g!tank y 來確認選取職業 | Ganyu RPG",icon_url=bot_icon_url)

        await ctx.send(embed=embed)
        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")

    @commands.command()
    async def ranjob(self, ctx):

        await ctx.send(embed=discord.Embed(
            title="",
            description="正在選擇職業..")
        )

        knight = discord.Embed(
            title="騎士 Knight",
            description="作為最基本的職業，騎士擁有強大的攻擊力及優越的防禦，但是他們受到魔法的傷害比其他職業還高．",
            color=discord.Colour.random()
        )
        knight.set_footer(text="輸入g!knight y 來確認選取職業 | Ganyu RPG",icon_url=bot_icon_url)

        shooter = discord.Embed(
            title="遊俠 Shooter",
            description="遊俠是所有職業裡敏捷度最高的職業，同時也具有較高的物傷，但是其他屬性則相對較低．",
            color=discord.Colour.random()
        )
        shooter.set_footer(text="輸入g!shooter y 來確認選取職業 | Ganyu RPG",icon_url=bot_icon_url)
        
        mage = discord.Embed(
            title="法師 Mage",
            description="法師是所有職業裡法傷最高的職業，如果說刺客是物傷天花板，那法師就是法傷天花板，除此之外其他屬性就普普而已．",
            color=discord.Colour.random()
        )
        mage.set_footer(text="輸入g!mage y 來確認選取職業 | Ganyu RPG",icon_url=bot_icon_url)

        assassin = discord.Embed(
            title="刺客 Assassin",
            description="物傷的極致，神秘又帥氣的職業，除了超高的物傷外還具有較高的敏捷度，但其他屬性相對較低．",
            color=discord.Colour.random()
        )
        assassin.set_footer(text="輸入g!assassin y 來確認選取職業 | Ganyu RPG",icon_url=bot_icon_url)
       
        tank = discord.Embed(
            title="坦克 Tank",
            description="顧名思義，坦克比任何職業的防禦能力都還要高，不管是在物防還是魔防部分都具有超高的防禦，其他屬性則沒什特點．",
            color=discord.Colour.random()
        )
        tank.set_footer(text="輸入g!tank y 來確認選取職業 | Ganyu RPG",icon_url=bot_icon_url)

        ranjob = [knight, shooter, mage, assassin, tank]

        end = random.choice(ranjob)

        await ctx.send(
            embed=discord.Embed(
                title=f"選到了 {end.title} !"
            )
        )

        await ctx.send(embed=end)
        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")

def setup(bot):
    bot.add_cog(rpg(bot))