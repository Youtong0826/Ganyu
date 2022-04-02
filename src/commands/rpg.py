import random , discord , datetime , json
from discord.ext import commands
from core.classes import Cog_ExtenSion

class rpg(Cog_ExtenSion):
    have_job = False

    def getDB():
        with open("res/db/DB.json","r") as f:
            return json.loads(f.read())

    def addDB(db):
        with open("res/db/DB.json","w") as f:
            return f.write(
                json.dumps(
                    db,
                    ensure_ascii=False,
                    indent=4,
                    separators=(',',': ')
                )
            )

    def getRPGDB():
        with open("res/db/rpg.json","r") as f:
            return json.loads(f.read())

    def addRPGDB(jobdb):
        with open("res/db/rpg.json","w") as f:
            return f.write(
                json.dumps(
                    jobdb,
                    ensure_ascii=False,
                    indent=4,
                    separators=(',', ': ')
                )
            )
    
    def addrpg(id, job, exp:int, level:int, coin:int, name):
        id = str(id)
        rpgdb = rpg.getRPGDB()

        if f'{id}' not in rpgdb:

            rpgdb[id] = {"name":"","job":"","exp":0,"level":0,"coin":0}

        rpgdb[id] = {"name":f"{name}","job":job,"exp":exp,"level":level,"coin":rpgdb[id].get('coin') + coin}
        
        rpg.addRPGDB(rpgdb)#{f'{id}':f'{job}'})

    def getjob(id):

        id = str(id)
        rpgdb = rpg.getRPGDB()

        if f"{id}" not in f"{rpgdb}":
            rpgdb[id] = "無"
        return rpgdb[id]
    
    def have_job(id):

        test = 0
        id = str(id)
        rpgdb = rpg.getRPGDB()

        if f"{id}" in f"{rpgdb}":
            job = {"job":"Knight","job":"Shooter","job":"Mage","job":"Assassin","job":"Tank"}

            for n in job:
                if n in rpgdb[id]:
                    test += 1

            if test == 1:
                return True 

            if test == 0:
                return False

        else:
            return False

    def top(type):#type=level or coin 
        rpgdb = rpg.getRPGDB()
        ramtop = {} 
        top = []
        time = 0

        for key in rpgdb:
            time += 1
            l = rpgdb[key].get(type)
            n = rpgdb[key].get("name")
            ramtop["name"]= n
            ramtop["int"]= l
            top.append(ramtop)
            print(sorted(top, key = lambda i: i['int'],reverse=True) )

    @commands.command()
    async def rpg(
        self,
        ctx,
        key):

        user = ctx.author
        id = str(user.id)
        taked = rpg.getDB()
        rpgdb = rpg.getRPGDB()

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
                text=f"{ctx.author.name}",
                icon_url=ctx.author.avatar
            )

        elif key == "start":

            if rpg.have_job(id):
                embed = discord.Embed(
                    title="**選擇你要前往的副本!**",
                    color=discord.Colour.random()
                )
                embed = discord.Embed(
                    title="**暫未開放**",
                    color=discord.Colour.random()
                )

            else:
                embed = discord.Embed(
                    title="**請先選擇職業!**",
                    color=discord.Colour.random()
                )

        elif key == "info":

            if user.nick == None:
                nick = user.name

            else:
                nick = user.nick

            if rpg.have_job(id):

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

            else:
                job = "無"
                level = 0     
                coin = 0

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
                name="**冒險幣**",
                value=f"{coin} $"
            )
            embed.set_footer(
                text=f"{ctx.author.name}",
                icon_url=ctx.author.avatar
            )

        elif key == "cointop":
            #top = rpg.top()
            #embed = discord.Embed(title=f"** Coin Top 等級排行**",description=f"1.  {top[1].get('name')}  **{top[1].get('coin')}** $\n2.  {top[2].get('name')}  **{top[2].get('coin')}** $\
#\n3.  {top[3].get('name')}  **{top[3].get('coin')}** $\n4.  {top[4].get('name')}  **{top[4].get('coin')}** $\n5.  {top[5].get('name')}  **{top[5].get('coin')}** $\n6.  {top[6].get('name')}  **{top[6].get('coin')}** $\n",color=discord.Colour.random())
            #await ctx.send(rpg.top(type="coin"))

            embed = discord.Embed(
                title=f"** 暫未開放 **",
                color=discord.Colour.random()
            )

        elif key == "levtop":
            top = rpg.top(type="level")
            #embed = discord.Embed(title=f"** Level Top 冒險幣排行**\n1.  {top[1].get('name')}  Lv.{top[1].get('level')}",color=discord.Colour.random())
            embed = discord.Embed(
                title=f"* 暫未開放 **",
                color=discord.Colour.random()
            )

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

        elif key == "kit":
            #if not id in taked:
            #    embed = discord.Embed(title=f"**成功領取補償包!**",color=discord.Colour.random())
            #    rpg.addrpg(id=f"{id}",job=f"{rpgdb[id].get('job')}",exp=rpgdb[id].get('exp'),level=rpgdb[id].get('level'),name=f"{rpgdb[id].get('name')}",coin=300)
            #    taked[user.id] = user.name
            #    rpg.addDB(taked)
            #else:
                #embed = discord.Embed(title=f"**您已經領過了!**",color=discord.Colour.random())
                embed = discord.Embed(
                    title = "目前尚無可領取的禮包喔~", 
                )

        else:            
            embed = discord.Embed(
                title="**錯誤X**",
                description=f'RPG沒有"{key}"這個分類喔~',
                color=discord.Colour.random())

        await ctx.send(embed=embed)

    @commands.command()
    async def knight(self,ctx,key):
        if rpg.have_job(ctx.author.id):
            embed = discord.Embed(title="**您已經選過職業了!**",color=discord.Colour.random())
        else:
            if key == "y":
                embed = discord.Embed(title="**成功選擇騎士!**",color=discord.Colour.random())
                rpg.addrpg(id=f"{ctx.author.id}",job="Knight",exp=0,level=0,coin=0,name=f"{ctx.author.name}")
        await ctx.send(embed=embed)

    @commands.command()
    async def shooter(self,ctx,key):

        if rpg.have_job(self.author.id):
            embed = discord.Embed(
                title="**您已經選過職業了!**",
                color=discord.Colour.random()
            )

        else:

            if key == "y":
                embed = discord.Embed(
                    title="**成功選擇射手!**",
                    color=discord.Colour.random()
                )

                rpg.addrpg(id=f"{ctx.author.id}",job="Shooter",exp=0,level=0,coin=0,name=f"{ctx.author.name}")

        await ctx.send(embed=embed)
    
    @commands.command()
    async def mage(self,ctx,key):

        if rpg.have_job(ctx.author.id):
            embed = discord.Embed(
                title="**您已經選過職業了!**",
                color=discord.Colour.random()
            )

        else:
            if key == "y":
                embed = discord.Embed(
                    title="**成功選擇法師!**",
                    color=discord.Colour.random()
                )

                rpg.addrpg(id=f"{ctx.author.id}",job="Mage",exp=0,level=0,coin=0,name=f"{ctx.author.name}")

        await ctx.send(embed=embed)

    @commands.command()
    async def assassin(self,ctx,key):

        if rpg.have_job(ctx.author.id):
            embed = discord.Embed(
                title="**您已經選過職業了!**",
                color=discord.Colour.random()
            )
        else:
            if key == "y":
                embed = discord.Embed(
                    title="**成功選擇刺客!**",
                    color=discord.Colour.random()
                )

                rpg.addrpg(id=f"{ctx.author.id}",job="Assassin",exp=0,level=0,coin=0,name=f"{ctx.author.name}")

        await ctx.send(embed=embed)

    @commands.command()
    async def tank(self,ctx,key):

        if rpg.have_job(ctx.author.id):
            embed = discord.Embed(
                title="**您已經選過職業了!**",
                color=discord.Colour.random()
            )

        else:
            if key == "y":

                embed = discord.Embed(
                    title="**成功選擇坦克!**",
                    color=discord.Colour.random())

                rpg.addrpg(id=f"{ctx.author.id}",job="Tank",exp=0,level=0,coin=0,name=f"{ctx.author.name}")

        await ctx.send(embed=embed)
    
    @commands.command()
    async def ranjob(self,ctx):

        await ctx.send(embed = discord.Embed(
            title="正在選擇職業..")
            )

        knight = discord.Embed(
            title="騎士 Knight",
            description="作為最基本的職業，騎士擁有強大的攻擊力及優越的防禦，但是他們受到魔法的傷害比其他職業還高．",
            color=discord.Colour.random()
        )
        knight.add_field(
            name="**能力值:**",
            value="**物理傷害:** 12/20\n**魔法傷害:** 02/20\n**物理防禦:** 14/20\n**魔法防禦:** 06/20\n**敏捷度:** 08/20\n**智力:** 06/20\n\n輸入g!knight y來確認選取職業"
        )
        shooter = discord.Embed(
            title="遊俠 Shooter",
            description="遊俠是所有職業裡敏捷度最高的職業，同時也具有較高的物傷，但是其他屬性則相對較低．",
            color=discord.Colour.random()
        )
        shooter.add_field(
            name="**能力值:**",
            value="**物理傷害:** 16/20\n**魔法傷害:** 08/20\n**物理防禦:** 02/20\n**魔法防禦:** 02/20\n**敏捷度:** 14/20\n**智力:** 06/20\n\n輸入g!shooter y來確認選取職業"
        )
        mage = discord.Embed(
            title="法師 Mage",
            description="法師是所有職業裡法傷最高的職業，如果說刺客是物傷天花板，那法師就是法傷天花板，除此之外其他屬性就普普而已．",
            color=discord.Colour.random()
        )
        mage.add_field(
            name="**能力值:**",
            value="**物理傷害:** 02/20\n**魔法傷害:** 18/20\n**物理防禦:** 02/20\n**魔法防禦:** 10/20\n**敏捷度:** 04/20\n**智力:** 12/20\n\n輸入g!mage y來確認選取職業")
        assassin = discord.Embed(
            title="刺客 Assassin",
            description="物傷的極致，神秘又帥氣的職業，除了超高的物傷外還具有較高的敏捷度，但其他屬性相對較低．",
            color=discord.Colour.random()
        )
        assassin.add_field(
            name="**能力值:**",
            value="**物理傷害:** 18/20\n**魔法傷害:** 02/20\n**物理防禦:** 06/20\n**魔法防禦:** 02/20\n**敏捷度:** 12/20\n**智力:** 08/20\n\n輸入g!assassin y來確認選取職業"
        )
        tank = discord.Embed(
            title="坦克 Tank",
            description="顧名思義，坦克比任何職業的防禦能力都還要高，不管是在物防還是魔防部分都具有超高的防禦，其他屬性則沒什特點．",
            color=discord.Colour.random()
        )
        tank.add_field(
            name="**能力值:**",
            value="**物理傷害:** 06/20\n**魔法傷害:** 02/20\n**物理防禦:** 16/20\n**魔法防禦:** 16/20\n**敏捷度:** 02/20\n**智力:** 08/20\n\n輸入g!tank y來確認選取職業"
        )

        ranjob = [knight,shooter,mage,assassin,tank]

        end = random.choice(ranjob)

        await ctx.send(
            embed = discord.Embed(
                title=f"選到了{end.title}!"
            )
        )

        await ctx.send(embed=end)

def setup(bot):
    bot.add_cog(rpg(bot))