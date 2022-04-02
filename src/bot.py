import discord , datetime , os
from discord.ext import commands

bot = commands.Bot(
    command_prefix='g!',
    intents = discord.Intents.all()
)

for Filename in os.listdir("src/commands"):
    if Filename.endswith(".py"):
        bot.load_extension(f"commands.{Filename[:-3]}")

bot.activity = discord.Game(
    name="g!help owo"
)
    
@bot.command()
async def test(ctx):
    embed = discord.Embed(
        title="This is a test command owo"
    )
    await ctx.send(embed = embed)
    

@bot.command()
async def time(ctx,key):

        if f"{key}" == "taiwan" or "TW" or "tw" or "Tw":
            embed = discord.Embed(
                title="台北時間",
                description=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}"
            )
        await ctx.send(embed=embed)

@bot.command()
async def load(ctx,extension):
    if ctx.author.id == 611118369474740244 or 856041155341975582:
        bot.load_extension(f"commands.{extension}")
        embed = discord.Embed(
            title=f"Loaded - {extension} - Cog",
            color=0x5cff8d
        )
    else:
        embed = discord.Embed(
            title="此為開發者專屬功能",
            color=0x5cff8d
        ) 
    await ctx.send(embed = embed)
    print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}]:{ctx.author.name} loaded {extension} Cog in {ctx.author.guild}")

@bot.command()
async def unload(ctx,extension):
    if ctx.author.id == 611118369474740244 or 856041155341975582:
        bot.unload_extension(f"commands.{extension}")
        embed = discord.Embed(
            title=f"Unloaded - {extension} - Cog",
            color=0x5cff8d
        )
    else:
        embed = discord.Embed(
            title="此為開發者專屬功能",
            color=0x5cff8d
        ) 
    await ctx.send(embed = embed)
    print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}]:{ctx.author.name} unloaded {extension} Cog in {ctx.author.guild}")

@bot.command()
async def reload(ctx,extension):
    if ctx.author.id == 611118369474740244 or 856041155341975582:
        bot.reload_extension(f"commands.{extension}")
        embed = discord.Embed(
            title=f"Reloaded - {extension} - Cog",
            color=0x5cff8d
        )
    else:
        embed = discord.Embed(
            title="此為開發者專屬功能",
            color=0x5cff8d
        ) 
    await ctx.send(embed = embed)
    print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}]:{ctx.author.name} reloaded {extension} Cog in {ctx.author.guild}")

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event 
async def on_command_error(ctx,error):
    bool1 = False
    bool2 = False
    def on_cmd_error(keywords,error):#尋找回報中是否含有關鍵字
        test = 0
        for n in keywords:
            if n in f'{error}':
                test += 1
        if test == len(keywords):
            return True
        else:
            return False
    def embed_copy(des):#快速嵌入訊息
        embed = discord.Embed(
            title = "指令執行失敗..",
            description = f"原因: {des}",
            color = discord.Colour.random()
        )
        return embed
    if on_cmd_error(keywords=["Missing Permission"],error=error):
        bool1 = True
        if f"{ctx.command}" == "say":
            embed = embed_copy(des="我沒有刪除訊息的權限")
        else:
            embed= embed_copy(des="我沒有權限..")
    if on_cmd_error(keywords=["Member","not found"],error=error):
        bool1 = True
        embed= embed_copy(des="查無此人")
    if on_cmd_error(keywords=['Command','is not found'],error=error):
        bool1 = True
        bool2 = False
        embed= embed_copy(des="沒有這個指令啦!")
    if on_cmd_error(keywords=['Converting to "literal_eval" failed for parameter "a".'],error=error):
        bool1 = True
        embed= embed_copy(des="第一個數字是不是怪怪的hmm")
    if on_cmd_error(keywords=['Converting to "literal_eval" failed for parameter "b".'],error=error):
        bool1 = True
        embed= embed_copy(des="第二個數字是不是怪怪的hmm")
    if on_cmd_error(keywords=["b is a required argument that is missing."],error=error):
        bool1 = True
        embed= embed_copy(des="阿你的第二個數字勒..")
    if on_cmd_error(keywords=['a is a required argument that is missing.'],error=error):
        bool1 = True
        embed= embed_copy(des="你不輸入數字我怎麼算...")
    if on_cmd_error(keywords=['arg is a required argument that is missing.'],error=error):
        bool1 = True
        if f"{ctx.command}" == "say":
            embed= embed_copy(des="沒有可以模仿的話..")
        elif f"{ctx.command}" == "ac":
            embed= embed_copy(des="此為測試功能")
    if on_cmd_error(keywords=['nember is a required argument that is missing.'],error=error):
        bool1 = True
        embed=discord.Embed(
            title="選擇你要猜的號碼!",
            description="輸入 g!dice 1~6",
            color=discord.Colour.random()
        )
    if on_cmd_error(keywords=['key is a required argument that is missing.'],error=error):
        bool1 = True
        if f"{ctx.command}" == "rpg":
            embed = discord.Embed(
                title="RPG系統",
                color=discord.Colour.random()
            )
            embed.add_field(
                name="g!rpg  job",
                value="選擇你的職業"
            )
            embed.add_field(
                name="g!rpg  start",
                value="開始你的旅程!"
            )
            embed.add_field(
                name="g!rpg  info",
                value="查看你的RPG資訊"
            )
            embed.add_field(
                name="g!rpg  ann",
                value="獲取最新公告"
            )
            embed.add_field(
                name="g!rpg  levtop",
                value="查看等級排行"
            )
            embed.add_field(
                name="g!rpg  cointop",
                value="查看冒險幣排"
            )
        elif f'{ctx.command}' == "knight":
            embed = discord.Embed(
                title="騎士 Knight",
                description="作為最基本的職業，騎士擁有強大的攻擊力及優越的防禦，但是他們受到魔法的傷害比其他職業還高．",
                color=discord.Colour.random()
            )
            embed.add_field(
                name="**能力值:**",
                value="**物理傷害:** 12/20\n**魔法傷害:** 02/20\n**物理防禦:** 14/20\n**魔法防禦:** 06/20\n**敏捷度:** 08/20\n**智力:** 06/20\n\n輸入g!knight y來確認選取職業"
            )
        elif f'{ctx.command}' == "shooter":
            embed = discord.Embed(
                title="遊俠 Shooter",
                description="遊俠是所有職業裡敏捷度最高的職業，同時也具有較高的物傷，但是其他屬性則相對較低．",
                color=discord.Colour.random()
            )
            embed.add_field(
                name="**能力值:**",
                value="**物理傷害:** 16/20\n**魔法傷害:** 08/20\n**物理防禦:** 02/20\n**魔法防禦:** 02/20\n**敏捷度:** 14/20\n**智力:** 06/20\n\n輸入g!shooter y來確認選取職業"
            )
        elif f'{ctx.command}' == "mage":
            embed = discord.Embed(
                title="法師 Mage",
                description="法師是所有職業裡法傷最高的職業，如果說刺客是物傷天花板，那法師就是法傷天花板，除此之外其他屬性就普普而已．",
                color=discord.Colour.random()
            )
            embed.add_field(
                name="**能力值:**",
                value="**物理傷害:** 02/20\n**魔法傷害:** 18/20\n**物理防禦:** 02/20\n**魔法防禦:** 10/20\n**敏捷度:** 04/20\n**智力:** 12/20\n\n輸入g!mage y來確認選取職業"
            )
        elif f'{ctx.command}' == "assassin":
            embed = discord.Embed(
                title="刺客 Assassin",
                description="物傷的極致，神秘又帥氣的職業，除了超高的物傷外還具有較高的敏捷度，但其他屬性相對較低．"
                ,color=discord.Colour.random()
            )
            embed.add_field(
                name="**能力值:**",
                value="**物理傷害:** 18/20\n**魔法傷害:** 02/20\n**物理防禦:** 06/20\n**魔法防禦:** 02/20\n**敏捷度:** 12/20\n**智力:** 08/20\n\n輸入g!assassin y來確認選取職業"
            )
        elif f'{ctx.command}' == "tank":
            embed = discord.Embed(
                title="坦克 Tank",
                description="顧名思義，坦克比任何職業的防禦能力都還要高，不管是在物防還是魔防部分都具有超高的防禦，其他屬性則沒什特點．"
                ,color=discord.Colour.random()
            )
            embed.add_field(
                name="**能力值:**",
                value="**物理傷害:** 06/20\n**魔法傷害:** 02/20\n**物理防禦:** 16/20\n**魔法防禦:** 16/20\n**敏捷度:** 02/20\n**智力:** 08/20\n\n輸入g!tank y來確認選取職業"
            )
        elif f'{ctx.command}' == 'time':
            embed = discord.Embed(title="世界時間 world time")
            embed.add_field(
                name="台北 Taipei ",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="北京 Beijing ",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="夏威夷 Hawaii ",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=-10))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="安克拉治 Anchorage ",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=-9))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="溫哥華 vancouver ",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=-8))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="鳳凰城 Phoenix",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=-7))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="墨西哥城 Moxico City",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=-6))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="紐約 New York",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=-5))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="卡拉卡斯 Caracas",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=-4))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="聖保羅 Sao Paulo",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=-3))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="倫敦 London",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=0))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="柏林 Berlin",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=1))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="開羅 Cairo",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=2))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="莫斯科 Moscow",value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=3))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="杜拜 Dubai",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=4))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="新德里 New Delhi",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=5.5))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="仰光 Yangon",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=6.5))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="曼谷 Bangkok",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=7))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="東京 Tokyo",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=9))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="雪梨 Sydney",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=10))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="威靈頓 Wellington",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=12))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
    if on_cmd_error(keywords=['Converting to "int" failed for parameter "nember"'],error=error):
        bool1 = True
        embed= embed_copy(des=f"奇怪..您好像不是輸入一個完整的數字欸")
    if on_cmd_error(keywords=['id is a required argument that is missing.'],error=error):
        bool1 = True
        embed= embed_copy(des=f"缺少用來查找用戶的id")
    if on_cmd_error(keywords=['name is a required argument that is missing.'],error=error):
        bool1 = True
        embed= embed_copy(des=f"缺少用來查找id的用戶名")
    if on_cmd_error(keywords=["description is a required argument that is missing."],error=error):
        bool1 = True
        embed = embed_copy(des="缺少內容")
    if on_cmd_error(keywords=['member is a required argument that is missing.'],error=error):
        bool1 = True
        if "avatar" in f"{ctx.command}":
            bool2 = True
            embed = discord.Embed(
                title=f"這是 {user.name} 的頭貼",
                color=discord.Colour.random(),
                timestamp=datetime.datetime.utcnow()
            )
            embed.set_image(url=user.avatar)
            embed.set_footer(
                text=f"{ctx.author.name}",
                icon_url=ctx.author.avatar
            )
        elif "ban" in f"{ctx.command}":
            embed = embed_copy(des="是要我ban誰啦")
        elif ctx.command == "kick":
            embed = embed_copy(des="是要我kick誰啦")
        elif f"{ctx.command}" == "userinfo":
            user = ctx.author
            role = ""
            roles2 = ""
            roles_count = 0
            if user.nick == None:
                nick="無"
            else:
                nick=user.nick
            if user.bot:
                dbot = "Yes"
            else:
                dbot = "No"
            for n in user.roles:
                if n.name != '@everyone':
                    role += f"{n.mention} | "
                    roles_count += 1
                    if len(role) < 1014:
                        roles_count2 = roles_count 
                        roles2 = f"{role}"
            if len(role) > 1014:
                role = f"{roles2}+{roles_count - roles_count2} Roles"
            embed_main=discord.Embed(
                title=f"{user.name} 的個人資料",
                color=0x9c8fff,timestamp=datetime.datetime.utcnow()
            )
            embed_main.set_thumbnail(url=user.avatar)
            embed_main.add_field(
                name="🐬 暱稱",
                value=f"{nick}"
            )
            embed_main.add_field(
                name="🤖 Bot",
                value=f"{dbot}"
            )
            embed_main.add_field(
                name="💳 ID",
                value=f"`{user.id}`",
                inline=False
            )                
            embed_main.add_field(
                name=f"🗓️ 創建時間",
                value=f"{user.created_at.strftime('%Y/%m/%d')}"
            )
            embed_main.add_field(
                name="🗓️ 加入時間",
                value=f"{user.joined_at.strftime('%Y/%m/%d')}"
            ) 
            embed_main.add_field(
                name=f"📰 身分組:({roles_count})",
                value=f" {role}",inline=False
            )
            embed_main.set_footer(
                text=f"{user.name}",
                icon_url=f"{user.avatar}"
            )
            view_main = discord.ui.View(timeout=None)
            bool2 = True
            await ctx.send(embed=embed_main,view = view_main)
    if bool1 == False:
        #embed=event.embed_copy(des="待釐清... :(")
        print(error)
    if bool2 == False:
        await ctx.send(embed = embed)
    print(f"""
Time:'{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}'
User:'{ctx.author.name}' 
Guild:{ctx.author.guild}' 
Command:{ctx.command}'
Error:'{error}' 
bool1:'{bool1}' 
bool2:'{bool2}'
""")

if __name__ == "__main__":
    with open("token","r") as f:
        bot.run(f.read())