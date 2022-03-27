import random , discord , datetime , ast , json
from discord.ext import commands
from ganyu import ganyu , pic , update

bot = commands.Bot(
    command_prefix='g!',
    intents = discord.Intents.all()
)

bot.remove_command("help")

bot.activity = discord.Game(
    name="g!help owo"
)

have_job = False

class func:

    def embed_copy(des):#快速嵌入訊息

        embed = discord.Embed(
            title = "指令執行失敗..",
            description = f"原因: {des}",
            color = discord.Colour.random()
        )

        return embed

class command:

    @bot.command()
    async def help(ctx):

        embed = discord.Embed(
            title="Ganyu 指令清單",
            color = 0xec8fff,
            timestamp = datetime.datetime.utcnow()
        )

        embed.add_field(
            name = 'g!fun',
            value = '查看娛樂的指令清單',
            inline = False
        )

        embed.add_field(
            name = 'g!info',
            value = '查看資訊的指令清單',
            inline = False
        )

        embed.add_field(
            name = 'g!other',
            value = '查看其他指令',
            inline = False
        )

        embed.set_footer(
            text = f"{ctx.author.name}",
            icon_url = ctx.author.avatar
        )

        funbutton = discord.ui.Button(
            style = discord.ButtonStyle.green,
            label =" fun",
            emoji = "🎉"
        )

        infobutton = discord.ui.Button(
            style = discord.ButtonStyle.primary,
            label = "info",
            emoji = "📘"
        )

        otherbutton = discord.ui.Button(
            style = discord.ButtonStyle.green,
            label = "other",
            emoji = "📰"
        )

        backbutton = discord.ui.Button(
            style = discord.ButtonStyle.green,
            label = "back",
            emoji = "🔙"
        )

        backview = discord.ui.View(timeout=None)
        main_view = discord.ui.View(timeout=None)

        backview.add_item(backbutton)       
        main_view.add_item(funbutton)
        main_view.add_item(infobutton)
        main_view.add_item(otherbutton)

        async def funcallback(interaction):

            embed = discord.Embed(
                title = "fun 指令清單",
                color = discord.Colour.random(),
                timestamp = datetime.datetime.utcnow()
            )

            embed.add_field(
                name = "g!say",
                value = "讓這個機器人模仿你說話"
            )

            embed.add_field(
                name = "g!avatar",
                value = "查看他人/自己的頭貼"
            )

            embed.add_field(
                name = "g!dice",
                value = "讓這個機器人幫你骰骰子"
            )

            embed.add_field(
                name = "g!math",
                value = "算數"
            )

            embed.add_field(
                name = "g!rpg",
                value = "RPG系統(製作中)"
            )

            embed.set_footer(
                text = f"{ctx.author.name}",
                icon_url = ctx.author.avatar
            )

            await interaction.response.edit_message(
                embed = embed,
                view = backview
            )

        async def infocallback(interaction): 
            embed = discord.Embed(
                title = "info 指令清單",
                color = discord.Colour.random(),
                timestamp = datetime.datetime.utcnow()
            )

            embed.add_field(
                name = "g!userinfo",
                value = "查看使用者在此伺服器的資訊"
            )

            embed.add_field(
                name = "g!serinfo",
                value = "查看伺服器的資訊"
            )

            embed.add_field(
                name = "g!botinfo",
                value = "查看機器人的資訊"
            )

            embed.add_field(
                name = "g!time",
                value = "查看各國時間"
            )

            embed.add_field(
                name = "g!update",
                value = "查看更新資訊"
            )

            embed.add_field(
                name="g!invite",
                value="獲取邀請連結"
            )

            embed.set_footer(
                text = f"{ctx.author.name}",
                icon_url = ctx.author.avatar
            )  

            await interaction.response.edit_message(
                embed = embed,
                view = backview
            )

        async def othercallback(interaction):

            embed = discord.Embed(
                title = "other 指令清單",
                color = discord.Colour.random(),
                timestamp = datetime.datetime.utcnow()
            )

            embed.add_field(
                name = "g!about",
                value = "關於甘雨"
            )

            embed.add_field(
                name = "g!ping",
                value = "查看機器人延遲"
            )

            embed.add_field(
                name = "g!say",
                value = "讓這個機器人模仿你說話"
            )

            embed.add_field(
                name = "g!getid",
                value =" 透過用戶取得用戶id"
            )

            embed.add_field(
                name = "g!about",
                value = "透過id取的用戶"
            )

            embed.set_footer(
                text = f"{ctx.author.name}",
                icon_url = ctx.author.avatar
            )  

            await interaction.response.edit_message(
                embed = embed,
                view = backview
            )

        async def backcallback(interaction):
            embed=discord.Embed(
                title = "Ganyu 指令清單",
                color = 0xec8fff,
                timestamp = datetime.datetime.utcnow()
            )

            embed.add_field(
                name = 'g!fun' , 
                value = '查看娛樂的指令清單', 
                inline = False
            )

            embed.add_field(
                name = 'g!info',
                value = '查看資訊的指令清單',
                inline = False
            )

            embed.add_field(
                name = 'g!other',
                value = '查看其他指令',
                inline = False
            )

            embed.set_footer(
                text = f"{ctx.author.name}",
                icon_url = ctx.author.avatar)

            await interaction.response.edit_message(
                embed = embed,
                view = main_view
            )

        funbutton.callback = funcallback
        infobutton.callback = infocallback
        otherbutton.callback = othercallback
        backbutton.callback = backcallback

        await ctx.send(
            embed = embed,
            view = main_view
        )

        print(
            f"""
            Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}
            User:{ctx.author} 
            ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}
            """)

    @bot.command()
    async def fun(ctx):

        embed = discord.Embed(
            title = "fun 指令清單",
            color = discord.Colour.random(),
            timestamp = datetime.datetime.utcnow()
        )

        embed.add_field(
            name = "g!say",
            value = "讓這個機器人模仿你說話"
        )

        embed.add_field(
            name = "g!avatar",
            value = "查看他人/自己的頭貼"
        )

        embed.add_field(
            name = "g!dice",
            value = "讓這個機器人幫你骰骰子"
        )

        embed.add_field(
            name = "g!math",
            value = "算數"
        )

        embed.add_field(
            name = "g!rpg",
            value = "RPG系統(製作中)"
        )

        embed.set_footer(
            text = f"{ctx.author.name}",
            icon_url = ctx.author.avatar
        )

        await ctx.send(
            embed = embed
        )

        print(
            f"""
            Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} 
            ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}
            """)

    @bot.command()
    async def info(ctx):

        embed = discord.Embed(
            title = "info 指令清單",
            color = discord.Colour.random(),
            timestamp = datetime.datetime.utcnow()
        )

        embed.add_field(
            name = "g!userinfo (製作中)",
            value = "查看使用者在此伺服器的資訊")

        embed.add_field(
            name = "g!serinfo (製作中)",
            value = "查看伺服器的資訊"
        )

        embed.add_field(
            name = "g!botinfo(製作中)",
            value = "查看機器人的資訊"
        )

        embed.add_field(
            name = "g!time",
            value = "查看各國時間"
        )

        embed.add_field(
            name = "g!update",
            value = "查看更新資訊"
        )

        embed.add_field(
            name = "g!invite",
            value = "獲取邀請連結"
        )

        embed.set_footer(
            text = f"{ctx.author.name}",
            icon_url = ctx.author.avatar
        )

        await ctx.send(embed=embed)

        print(
            f"""
            Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} 
            ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}
            """)
        
    @bot.command()
    async def other(ctx):

        embed = discord.Embed(
            title = "other 指令清單",
            color = discord.Colour.random(),
            timestamp = datetime.datetime.utcnow()
        )

        embed.add_field(
            name = "g!about",
            value = "關於甘雨"
        )

        embed.add_field(
            name = "g!ping",
            value = "查看機器人延遲"
        )

        embed.add_field(
            name = "g!getid",
            value = "透過用戶取得用戶id"
        )

        embed.add_field(
            name = "g!getuser",
            value = "透過id取得用戶"
        )

        embed.set_footer(
            text = f"{ctx.author.name}",
            icon_url = ctx.author.avatar
        )

        await ctx.send(embed=embed)

        print(
            f"""
            Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} 
            ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}
            """)

    @bot.command()
    async def say(ctx ,*, arg):

        await ctx.message.delete()
        await ctx.send(arg)

        print(
            f"""
            Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}
            """)

    @bot.command()
    async def invite(ctx):

        link = "https://ptb.discord.com/api/oauth2/authorize?client_id=921673886049910795&permissions=0&scope=bot"

        embed = discord.Embed(
            title = "邀請我至你的伺服器!",
            color = discord.Colour.random(),
            url = link
        )

        #embed = discord.Embed(title="🚫此功能暫未開啟",color=discord.Colour.random())
        await ctx.send(embed = embed)

        print(
            f"""
            Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} 
            ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}
            """)

    @bot.command()
    async def ban(ctx , member : discord.Member ,*, reason=None):

        if ctx.author == ctx.author.guild.owner:
            await member.ban(reason = reason)
            await ctx.send("banned "+ f"{member}" )   

        else:
            await ctx.send("你沒有權限!") 

            print(
                f"""
                Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
                User:{ctx.author} 
                ID:{ctx.author.id} 
                Guild:{ctx.author.guild} 
                Command:{ctx.command}
                """)

    @bot.command()
    async def about(ctx):

        await ctx.send(random.choice(ganyu))

        print(
            f"""
            Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} 
            ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}
            """)

    @bot.command()
    async def update(ctx):

        embed = discord.Embed(
            title = "更新資訊(此功能所提供的資訊並非完全準確)",
            description = f"{datetime.datetime.utcnow().strftime('%Y/%m/%d')}\n{update}",
            color = discord.Colour.random(),timestamp=datetime.datetime.utcnow()
        )

        embed.set_footer(
            text = f"{ctx.author.name}",
            icon_url=  ctx.author.avatar
        )

        await ctx.send(embed=embed)

        print(
            f"""
            Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}
            """)

    @bot.command()
    async def ping(ctx):

        embed=discord.Embed(
            title=f"💫💫💫 Ping: {round(bot.latency*1000)} ms",
            color=discord.Colour.random(),
            timestamp=datetime.datetime.utcnow()
        )

        embed.set_footer(
            text=f"{ctx.author.name}",
            icon_url=ctx.author.avatar
        )

        await ctx.send(embed=embed)

        print(
            f"""
            Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} 
            ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}
            """)

    @bot.command()
    async def pic(ctx):
        random_pic = random.choice(pic)
        picf = discord.File(random_pic)

        await ctx.send(file = picf)

        print(
            f"""
            Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} 
            ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}
            """)

    @bot.command()
    async def avatar(ctx,*,member:discord.Member):

        embed = discord.Embed(
            title = f"這是 {member.name} 的頭貼",
            color = discord.Colour.random(),
            timestamp = datetime.datetime.utcnow()
        )

        embed.set_image(url=member.avatar)

        embed.set_footer(
            text = f"{ctx.author.name}",
            icon_url = ctx.author.avatar
        )

        await ctx.send(embed = embed)#_url_as(format=None, static_format='webp', size=1024))

        print(
            f"""
            Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}
            """)

    @bot.command()
    async def getuser(ctx,id:int):
        embed = discord.Embed(
            title = "成功!",
            description = f"id為 {id} 的用戶是 {bot.get_user(id).name} !",
            color = discord.Colour.random(),
            timestamp = datetime.datetime.utcnow()
        )

        embed.set_footer(
            text = f"{ctx.author.name}",
            icon_url = ctx.author.avatar
        )

        await ctx.send(embed = embed)

    @bot.command()
    async def getid(ctx,name:discord.Member):

        embed = discord.Embed(
            title = "成功!",
            description = f"用戶名為 {name.name} 的id是 {name.id} !",
            color = discord.Colour.random(),
            timestamp = datetime.datetime.utcnow()
        )

        embed.set_footer(
            text = f"{ctx.author.name}",
            icon_url = ctx.author.avatar
        )

        await ctx.send(embed = embed)

    @bot.command()
    async def dice(ctx,nember:int):

        if int(nember) > 6 or int(nember) < 1:
            embed = discord.Embed(
                title = "...... >:(",
                description = f"叫你選1~6 你選{nember}幹嘛啦!",
                color=discord.Colour.random()
            )

            await ctx.send(embed = embed)

        else:
            dice = [1,2,3,4,5,6]
            end = random.choice(dice)

            if end == nember:
                embed = discord.Embed(
                    title = "成功!",
                    description = f"恭喜你成功骰到了{nember}!",
                    color = discord.Colour.random()
                )

            else:
                embed = discord.Embed(
                    title = "很遺憾..",
                    description = f"您骰到了{end}..",
                    color = discord.Colour.random()
                )

            await ctx.send(embed = embed)
        print(
            f"""
            Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} 
            ID:{ctx.author.id} 
            Guild:{ctx.author.guild} Command:{ctx.command}
            """)
        
    @bot.command()
    async def gueit(ctx,dight:int):#guessdight
        r = []

        for n in range(1,1001):
            r.append(n)

        ans =  random.choice(r)
        time = 0
        olddight = ""
        
        #embed = discord.Embed(title="太大了!",description="謎底比你想的還要小喔",color=discord.Colour.random())
                           
        #embed = discord.Embed(title="接近答案了!",description="但還是有點大XD",color=discord.Colour.random())
                  
        #embed = discord.Embed(title="就差一點了!",description="再小一點啦",color=discord.Colour.random())
                    
        #embed = discord.Embed(title="太小了",description="謎底比擬想的還要小喔",color=discord.Colour.random())
                    
        #embed = discord.Embed(title="接近答案了",description="但還是有點小XD",color=discord.Colour.random())
                    
        #embed = discord.Embed(title="就差一點了!",description="再大一點啦",color=discord.Colour.random())
                    
        embed = discord.Embed(
            title = "恭喜!",
            description = f"您猜中了數字! 答案是{ans} ",
            color = discord.Colour.random(),
            timestamp = datetime.datetime.utcnow()
        )

        embed.set_footer(
            text = f"{ctx.author.name}",
            icon_url = ctx.author.avatar
        )

        await ctx.send(embed = embed)

    @bot.command()
    async def test(ctx):
        embed = discord.Embed(
            title="This is test command owo"
        )
        await ctx.send(embed)
        
class info:

    @bot.command()
    async def serinfo(ctx):
        can_see = True 
        mbot = 0
        person = 0
        booster = ""
        guild = ctx.author.guild

        for n in guild.members:

            if n.bot:
                mbot += 1

            else:
                person += 1

        if guild.premium_progress_bar_enabled:
            bar = "已開啟"

        else:
            bar = "未開啟"

        for n in guild.premium_subscribers:
            booster += f"{n}\n" 

        if booster == "":
            booster = "無"

        if can_see == True:
            embed_main = discord.Embed(
                title = f'{guild}',
                color = 0x9c8fff,
                timestamp = datetime.datetime.utcnow()
            )

            embed_main.add_field(
                name = "__:blue_book: 資訊__",
                value = f"\
                    **創建者:** \n`{guild.owner}`\
                    \n**創建者ID:** `\n{guild.owner_id}`\
                    \n**創建時間:** \n`{guild.created_at.strftime('%Y/%m/%d')}`\
                    \n**伺服器ID:** \n`{guild.id}`"
            )

            embed_main.add_field(
                name = "__:bar_chart: 統計__",
                value = f"\
                    **總成員數:** `{guild.member_count}`\
                    \n**活人:** `{person}`\
                    \n**機器人:** `{mbot}`\
                    \n**頻道數:** `{len(guild.channels)}`\
                    \n**身分組數:** `{len(guild.roles)}`\
                    \n**表情符號數:** `{len(guild.emojis)}`"     
            )

            embed_main.add_field(
                name = "__:newspaper: 其他__",
                value = f"\
                    **加成次數:** `{guild.premium_subscription_count}`\
                    \n**群組等級:** `{guild.premium_tier}`\
                    \n**加成進度條:** `{bar}`\
                    \n**主要語言:** `{guild.preferred_locale}`\
                    \n**規則頻道:** `#{guild.rules_channel}`",inline=True)

            embed_main.set_thumbnail(
                url = guild.icon
            )
    
            embed_main.set_footer(
                text = f"{ctx.author.name}",
                icon_url = ctx.author.avatar
            )

            if guild.rules_channel == None:
                linkbutton = discord.ui.Button(
                    style = discord.ButtonStyle.danger,
                    emoji = "🔖",
                    label = "無法前往規則頻道!"
                )
    
            else:
                linkbutton = discord.ui.Button(
                    style = discord.ButtonStyle.success,
                    emoji = "🔖",label="點擊前往規則頻道!",
                    url = f"https://discord.com/channels/{guild.id}/{guild.rules_channel.id}"
                )

            checkboosterbutton = discord.ui.Button(
                style = discord.ButtonStyle.success,
                emoji = "📖",
                label = "點擊查看加成此伺服器的人!"
            )

            select_main = discord.ui.Select(
                options = [
                    discord.SelectOption(
                        label = "SerInfo",
                        value = "ser",
                        description = "查看有關伺服器的資訊",
                        emoji = "📘"
                    ),
                    discord.SelectOption(
                        label="Botinfo",
                         value = "bot",
                         description = "查看Ganyu甘雨的資訊",
                         emoji = "🤖"
                    ),
                    discord.SelectOption(
                        label="UserInfo",
                            value = "user",
                        description = "查看用戶資訊",
                        emoji = "📰"
                    )                
                ]            
            )
                       

            backbutton = discord.ui.Button(
                style = discord.ButtonStyle.success,
                emoji = "🔙",
                label = "回去伺服器資訊"
            )

            view_main = discord.ui.View(timeout=None)
            view = discord.ui.View(timeout=None) 

            view.add_item(backbutton)
            view_main.add_item(linkbutton)
            view_main.add_item(checkboosterbutton)
            view_main.add_item(select_main)

            async def cbbcallback(interaction):

                await interaction.response.edit_message(
                    embed = discord.Embed(
                        title = f"加成此伺服器的人 ({len(guild.premium_subscribers)})",
                        description = f"{booster}"),
                        view = view
                )
            
            async def backcallback(interaction):

                await interaction.response.edit_message(
                    embed = embed,
                    view = view_main
                )

            async def mainselectcallback(interaction):

                if select_main.values[0] == "bot":

                    embed=discord.Embed(
                        title = f"{bot.user}",
                        color = 0x9c8ff,
                        timestamp = datetime.datetime.utcnow()
                    )

                    embed.add_field(
                        name = "📆 創建時間",
                        value = "`2022/1/21(GMT+8:00)`",
                        inline = False
                    )

                    embed.add_field(
                        name = "📜 ID",
                        value = f"`921673886049910795`",
                        inline = False
                    )

                    embed.add_field(
                        name = "🌐 伺服器",
                        value = f'`{len(bot.guilds)}`'
                    )

                    embed.add_field(
                        name = "📊 用戶",
                        value = f'`{len(bot.users)}`'
                    )

                    embed.add_field(
                        name = "💫 Ping",
                        value = f"`{round(bot.latency*1000)} ms`"
                    )

                    embed.set_footer(
                        text = "created by Youtong._.0826",
                        icon_url = "https://cdn.discordapp.com/avatars/856041155341975582/a5a57f0acdd5c5fb868c9ad50cf7c319.png?size=256"
                    )

                    linkbutton = discord.ui.Button(
                        style = discord.ButtonStyle.primary,
                        label = "Invite Link",emoji="🔗",
                        url = "https://ptb.discord.com/api/oauth2/authorize?client_id=921673886049910795&permissions=0&scope=bot"
                    ) 

                    view = discord.ui.View(timeout=None)
                    view.add_item(linkbutton)
                    view.add_item(select_main)

                    await interaction.response.edit_message(
                        embed = embed,
                        view = view
                    )

                if select_main.values[0] == "ser":
                        await interaction.response.edit_message(
                            embed = embed_main,
                            view = view_main
                        )

                elif select_main.values[0] == "user":

                    roles = ""
                    roles3 = ""
                    roles_count = 0
                    member = ctx.author

                    if member.nick == None:
                        nick = "無"

                    else:
                        nick = member.nick

                    if member.bot:
                        dbot = "Yes"

                    else:
                        dbot = "No"

                    for n in member.roles:

                        if n.name != '@everyone':
                            roles += f"{n.mention} | "
                            roles_count += 1

                        if len(roles) < 1014:
                            roles_count2 = roles_count
                            roles3 = f"{roles}"

                    if len(roles) > 1014:
                        roles = f"{roles3}+{roles_count-roles_count2} Roles..."

                    embed=discord.Embed(
                        title = f"{member.name} 的個人資訊 ",
                        color = 0x9c8fff,
                        timestamp = datetime.datetime.utcnow()
                    )

                    embed.set_thumbnail(url=member.avatar)

                    embed.add_field(
                        name = "🐬 暱稱",
                        value = f"{nick}"
                    )

                    embed.add_field(
                        name = "🤖 Bot",
                        value=f"{dbot}"
                    )

                    embed.add_field(
                        name = "💳 ID",
                        value = f"`{member.id}`",
                        inline = False
                    )

                    embed.add_field(
                        name = "📆 創建時間",
                        value = f"{member.created_at.strftime('%Y/%m/%d')}"
                    )

                    embed.add_field(
                        name = "📆 加入時間",
                        value = f"{member.joined_at.strftime('%Y/%m/%d')}"
                    ) 

                    embed.add_field(
                        name = f"📰 身分組:({roles_count})",
                        value = f"\n {roles}",inline=False
                    )

                    embed.set_footer(
                        text = f"{ctx.author.name}",
                        icon_url = ctx.author.avatar
                    )

                    view = discord.ui.View(timeout=None)
                    view.add_item(select_main)

                    await interaction.response.edit_message(
                        embed = embed,
                        view = view
                    )

            select_main.callback = mainselectcallback
            checkboosterbutton.callback = cbbcallback
            backbutton.callback = backcallback

            await ctx.send(
                embed = embed_main,
                view = view_main
            )

        else:
            embed = discord.Embed(
                title = "此功能暫未開啟",
                color = discord.Colour.random()
            )

        print(
            f"""\
            Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} \
            ID:{ctx.author.id}\
            Guild:{ctx.author.guild} \
            Command:{ctx.command}"""
        )


    @bot.command()
    async def botinfo(ctx):

        can_see = True

        if can_see == True:

            embed = discord.Embed(
                title = f"{bot.user}",
                color = 0x9c8ff,
                timestamp = datetime.datetime.utcnow()
            )

            embed.add_field(
                name = "📆 創建時間",
                value = "`2022/1/21(GMT+8:00)`",
                inline = False
            )

            embed.add_field(
                name = "📜 ID",
                value = f"`921673886049910795`",
                inline = False
            )

            embed.add_field(
                name = "🌐 伺服器",
                value = f'`{len(bot.guilds)}`'
            )

            embed.add_field(
                name = "📊 用戶",
                value = f'`{len(bot.users)}`'
            )

            embed.add_field(
                name = "💫 Ping",
                value = f"`{round(bot.latency*1000)} ms`"
            )

            embed.set_footer(
                text = "created by Youtong._.0826",
                icon_url = "https://cdn.discordapp.com/avatars/856041155341975582/a5a57f0acdd5c5fb868c9ad50cf7c319.png?size=256"
            )

            mainbutton1 = discord.ui.Button(
                style = discord.ButtonStyle.primary,
                label = "Invite Link",
                emoji = "🔗",
                url = "https://ptb.discord.com/api/oauth2/authorize?client_id=921673886049910795&permissions=0&scope=bot"
            ) 

            mian_view = discord.ui.View(timeout=None)
            mian_view.add_item(mainbutton1)

        await ctx.send(embed=embed,view=mian_view)

        print(
            f"""
            Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} 
            ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}"""
        )

    @bot.command()
    async def userinfo(ctx,member:discord.Member):

        roles = ""
        roles3 = ""
        roles_count = 0

        if member.nick == None:
            nick = "無"

        else:
            nick=member.nick

        if member.bot:
            dbot = "Yes"

        else:
            dbot = "No"

        for n in member.roles:

            if n.name != '@everyone':

                roles += f"{n.mention} | "
                roles_count += 1

                if len(roles) < 1014:

                    roles_count2 = roles_count
                    roles3 = f"{roles}"

        if len(roles) > 1014:
            roles = f"{roles3}+{roles_count-roles_count2} Roles..."

        embed_main = discord.Embed(
            title = f"{member.name} 的個人資訊 ",
            color = 0x9c8fff,
            timestamp = datetime.datetime.utcnow()
        )

        embed_main.set_thumbnail(
            url = member.avatar
        )

        embed_main.add_field(
            name = "🐬 暱稱",
            value = f"{nick}"
        )

        embed_main.add_field(
            name = "🤖 Bot",
            value = f"{dbot}"
        )

        embed_main.add_field(
            name = "💳 ID",
            value = f"`{member.id}`",
            inline = False
        ) 

        embed_main.add_field(
            name = "📆 創建時間",
            value = f"{member.created_at.strftime('%Y/%m/%d')}"
        )

        embed_main.add_field(
            name = "📆 加入時間",
            value = f"{member.joined_at.strftime('%Y/%m/%d')}"
        ) 

        embed_main.add_field(
            name = f"📰 身分組:({roles_count})",
            value = f"\n {roles}",inline=False
        )

        embed_main.set_footer(
            text = f"{ctx.author.name}",
            icon_url = ctx.author.avatar
        )

        main_view = discord.ui.View(timeout=None)

        await ctx.send(
            embed = embed_main,
            view = main_view
        ) 

        print(
            f"""
            Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} 
            ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}"""
        )
        
class math:

    @bot.command()
    async def math(ctx):

        embed=discord.Embed(
            title="算數",
            description="ex:g!add 10 20 ex:g!sqrt 20",
            color=discord.Colour.random()
        )
        embed.add_field(
            name='g!add',
            value='加法'
        )
        embed.add_field(
            name='g!remove',
            value='減法'
        )
        embed.add_field(
            name='g!mupy',
            value='乘法'
        )
        embed.add_field(
            name='g!dvsn',
            value='除法'
        )
        embed.add_field(
            name='g!sqrt',
            value='平方根'
        )
        embed.add_field(
            name='g!square',
            value='平方'
        )
        embed.add_field(
            name='g!fac',
            value='列出該數的因數(正負因數不列入考量)',
            inline=False
        )
        embed.set_footer(
            text=f"{ctx.author.name}",
            icon_url=ctx.author.avatar
        )

        await ctx.send(embed=embed)

        print(
            f"""
            Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}""")

    @bot.command()
    async def add(
        ctx,
        a : ast.literal_eval,
        b : ast.literal_eval
    ):
        embed = discord.Embed(
            title=" 執行成功!",
            description=f"{a} + {b}的結果為: {a+b}",
            color=discord.Colour.random()
        )
        await ctx.send(embed=embed)

        print(
            f"""
            Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}""")

    @bot.command()
    async def remove(
        ctx,a : ast.literal_eval,
        b : ast.literal_eval
    ):
        embed = discord.Embed(
            title=" 執行成功!",
            description=f"{a} - {b}的結果為: {a-b}",
            color=discord.Colour.random()
        )

        await ctx.send(embed=embed)
        print(
            f"""
            Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} 
            ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}"""
        )

    @bot.command()
    async def mupy(ctx,
        a : ast.literal_eval,
        b : ast.literal_eval
    ):
        embed = discord.Embed(
            title=" 執行成功!",
            description=f"{a} × {b}的結果為: {a*b}",
            color=discord.Colour.random()
        )

        await ctx.send(embed=embed)

        print(
            f"""
            Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} 
            ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}"""
        )

    @bot.command()
    async def dvsn(
        ctx,
        a : ast.literal_eval,
        b : ast.literal_eval
    ):
        embed = discord.Embed(
            title=" 執行成功!",
            description=f"{a} ÷ {b}的結果為: {a/b}",
            color=discord.Colour.random()
        )

        await ctx.send(embed=embed)
        print(
            f"""
            Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}"""
        )

    @bot.command()
    async def sqrt(
        ctx,
        a : ast.literal_eval
    ):
        if "-" in f'{a}':

            embed = discord.Embed(
                title=" 錯誤",
                description=f"負數沒有平方根!",
                color=discord.Colour.random()
            )

        else:

            embed = discord.Embed(
                title="Math執行成功!",
                description=f"{a} 開根號的結果為: {a**0.5}",
                color=discord.Colour.random()
            )

        await ctx.send(embed=embed)

        print(
            f"""Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} 
            ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}"""
        )

    @bot.command()
    async def square(
        ctx,
        a : ast.literal_eval
    ):
        embed = discord.Embed(
            title=" 執行成功!",
            description=f"{a}的平方結果為: {a*a}",
            color=discord.Colour.random()
        )

        await ctx.send(embed=embed)

        print(
            f"""Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} 
            ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}"""
        )

    @bot.command()
    async def fac(
        ctx,
        a : ast.literal_eval
    ):
        if len(f"{a}") > 6:

            embed = discord.Embed(
                title=" 錯誤",
                description=f"{a}太長了 該數不能超過6位數!",
                color=discord.Colour.random())

        else:

            if '-' in f'{a}':

                    embed = discord.Embed(
                        title="無法執行..",
                        description=f"原因:正負因數不列入考量..",
                        color=discord.Colour.random())
            else:

                fac=[]
                time = 0

                for i in range(1, a+1): 
                    time += 1

                    if a % i == 0:
                        fac.append(i) 
                        continue

                    else:
                        pass

                if len(fac) == 0:
                    embed = discord.Embed(
                        title=" 錯誤",
                        description=f"{a}沒有因數!",
                        color=discord.Colour.random())

                else:
                    embed = discord.Embed(
                        title=" 執行成功!",
                        description=f"{a}擁有的因數: {fac}",
                        color=discord.Colour.random())

        await ctx.send(embed=embed)

        print(
            f"""Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} 
            ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}"""
        )
        
#    @bot.command()
#    async def ac(ctx,arg):
#        arg = str(arg)
#        length = 0
#        for n in arg:
#            length += 1
#        if "×" or "x" or "*" in f"{arg}":
#            print(arg.index("x"))

class rpg:

    def getDB():
        with open("DB.json","r") as f:
            return json.loads(f.read())

    def addDB(db):
        with open("DB.json","w") as f:
            return f.write(
                json.dumps(
                    db,
                    ensure_ascii=False,
                    indent=4,
                    separators=(',',': ')
                )
            )

    def getRPGDB():
        with open("rpg.json","r") as f:
            return json.loads(f.read())

    def addRPGDB(jobdb):
        with open("rpg.json","w") as f:
            return f.write(
                json.dumps(
                    jobdb,
                    ensure_ascii=False,
                    indent=4,
                    separators=(',', ': ')
                )
            )
    
    def addrpg( 
        id,
        job,
        exp : int, 
        level : int,
        coin:int,
        name 
    ):
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

    @bot.command()
    async def rpg(ctx,key):

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

    @bot.command()
    async def knight(ctx,key):
        if rpg.have_job(ctx.author.id):
            embed = discord.Embed(title="**您已經選過職業了!**",color=discord.Colour.random())
        else:
            if key == "y":
                embed = discord.Embed(title="**成功選擇騎士!**",color=discord.Colour.random())
                rpg.addrpg(id=f"{ctx.author.id}",job="Knight",exp=0,level=0,coin=0,name=f"{ctx.author.name}")
        await ctx.send(embed=embed)

    @bot.command()
    async def shooter(ctx,key):

        if rpg.have_job(ctx.author.id):
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
    
    @bot.command()
    async def mage(ctx,key):

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

    @bot.command()
    async def assassin(ctx,key):

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

    @bot.command()
    async def tank(ctx,key):

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
    
    @bot.command()
    async def ranjob(ctx):

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

class time:
    @bot.command()
    async def time(ctx,key):

        if f"{key}" == "taiwan" or "TW" or "tw" or "Tw":
            embed = discord.Embed(
                title="台北時間",
                description=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}"
            )

        await ctx.send(embed=embed)

class event:
    @bot.event
    async def on_ready():
        print(">>Bot is online<<")

    @bot.event
    async def on_command_error(ctx,error):

        bool2 = False
        bool1 = False

        def on_cmd_error(keywords,error):#尋找回報中是否含有關鍵字

            test = 0

            for n in keywords:

                if n in f'{error}':
                    test += 1

            if test == len(keywords):
                return True

            else:
                return False

        if on_cmd_error(keywords=["Missing Permission"],error=error):

            bool1 = True

            if f"{ctx.command}" == "say":
                embed = func.embed_copy(des="我沒有刪除訊息的權限")

            else:
                embed=func.embed_copy(des="我沒有權限..")

        if on_cmd_error(keywords=["Member","not found"],error=error):

            bool1 = True
            embed=func.embed_copy(des="查無此人")

        if on_cmd_error(keywords=['Command','is not found'],error=error):

            bool1 = True
            embed=func.embed_copy(des="沒有這個指令啦!")
            
        if on_cmd_error(keywords=['Converting to "literal_eval" failed for parameter "a".'],error=error):

            bool1 = True
            embed=func.embed_copy(des="第一個數字是不是怪怪的hmm")
        if on_cmd_error(keywords=['Converting to "literal_eval" failed for parameter "b".'],error=error):

            bool1 = True
            embed=func.embed_copy(des="第二個數字是不是怪怪的hmm")
            
        if on_cmd_error(keywords=["b is a required argument that is missing."],error=error):

            bool1 = True
            embed=func.embed_copy(des="阿你的第二個數字勒..")
            
        if on_cmd_error(keywords=['a is a required argument that is missing.'],error=error):

            bool1 = True
            embed=func.embed_copy(des="你不輸入數字我怎麼算...")

        if on_cmd_error(keywords=['arg is a required argument that is missing.'],error=error):

            bool1 = True

            if f"{ctx.command}" == "say":
                embed=func.embed_copy(des="沒有可以模仿的話..")

            elif f"{ctx.command}" == "ac":
                embed=func.embed_copy(des="此為測試功能")

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
            embed=func.embed_copy(des=f"奇怪..您好像不是輸入一個完整的數字欸")

        if on_cmd_error(keywords=['id is a required argument that is missing.'],error=error):
            bool1 = True
            embed=func.embed_copy(des=f"缺少用來查找用戶的id")

        if on_cmd_error(keywords=['name is a required argument that is missing.'],error=error):
            bool1 = True
            embed=func.embed_copy(des=f"缺少用來查找id的用戶名")

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
                embed = func.embed_copy(des="是要我ban誰啦")

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
                select_main = discord.ui.Select(
                    options=[
                        discord.SelectOption(
                            label="UserInfo",
                            value="user",
                            description="查看用戶資訊",
                            emoji="📰"
                        ),
                        discord.SelectOption(
                            label="BotInfo",
                            value="bot",
                            description="查看Ganyu甘雨的資訊",
                            emoji="🤖"
                        ),
                        discord.SelectOption(
                            label="SerInfo",
                            value="ser",
                            description="查看有關伺服器的資訊",
                            emoji="📘"
                        )
                    ]
                )

                async def mainselectcallback(interaction):

                    if select_main.values[0] == "bot":
                        embed=discord.Embed(
                            title=f"{bot.user}",
                            color=0x9c8ff,
                            timestamp=datetime.datetime.utcnow()
                        )
                        embed.add_field(
                            name="📆 創建時間",
                            value="`2022/1/21(GMT+8:00)`",
                            inline=False
                        )
                        embed.add_field(
                            name="📜 ID",
                            value=f"`921673886049910795`",
                            inline=False
                        )
                        embed.add_field(
                            name="🌐 伺服器",
                            value=f'`{len(bot.guilds)}`'
                        )
                        embed.add_field(
                            name="📊 用戶",
                            value=f'`{len(bot.users)}`'
                        )
                        embed.add_field(
                            name="💫 Ping",
                            value=f"`{round(bot.latency*1000)} ms`"
                        )
                        embed.set_footer(
                            text="created by Youtong._.0826",
                            icon_url="https://cdn.discordapp.com/avatars/856041155341975582/a5a57f0acdd5c5fb868c9ad50cf7c319.png?size=256"
                        )
                        mainbutton1 = discord.ui.Button(
                            style=discord.ButtonStyle.primary,
                            label="Invite Link",
                            emoji="🔗",
                            url="https://ptb.discord.com/api/oauth2/authorize?client_id=921673886049910795&permissions=0&scope=bot"
                        ) 
                        view = discord.ui.View(timeout=None)
                        view.add_item(mainbutton1)
                        view.add_item(select_main)

                        await interaction.response.edit_message(
                            embed = embed,
                            view = view
                        )

                    elif select_main.values[0] == "user":
                        await interaction.response.edit_message(embed=embed_main,view = view_main)

                    elif select_main.values[0] == "ser":
                        mbot = 0
                        person = 0
                        booster = ""
                        guild = ctx.author.guild

                        for n in guild.members:

                            if n.bot:
                                mbot += 1

                            else:
                                person += 1

                        if guild.premium_progress_bar_enabled:
                            bar = "已開啟"

                        else:
                            bar = "未開啟"

                        for n in guild.premium_subscribers:
                            booster += f"{n}\n" 

                        if booster == "":
                            booster = "無"

                        embed = discord.Embed(
                            title=f'{guild}',
                            color=0x9c8fff,
                            timestamp=datetime.datetime.utcnow()
                        )

                        embed.add_field(
                            name="__:blue_book: 資訊__",
                            value=f"\
                            **創建者:** \n`{guild.owner}`\
                            \n**創建者ID:** `\n{guild.owner_id}`\
                            \n**創建時間:** \n`{guild.created_at.strftime('%Y/%m/%d')}`\
                            \n**伺服器ID:** \n`{guild.id}`"
                        )
                        embed.add_field(
                            name="__:bar_chart: 統計__",
                            value=f"\
                            **總成員數:** `{guild.member_count}`\
                            \n**活人:** `{person}`\
                            \n**機器人:** `{mbot}`\
                            \n**頻道數:** `{len(guild.channels)}`\
                            \n**身分組數:** `{len(guild.roles)}`\
                            \n**表情符號數:** `{len(guild.emojis)}`"
                        )
                        embed.add_field(
                            name="__:newspaper: 其他__",
                            value=f"\
                            **加成次數:** `{guild.premium_subscription_count}`\
                            \n**群組等級:** `{guild.premium_tier}`\
                            \n**加成進度條:** `{bar}`\
                            \n**主要語言:** `{guild.preferred_locale}`\
                            \n**規則頻道:** `#{guild.rules_channel}`"
                        )

                        embed.set_thumbnail(url=guild.icon)

                        embed.set_footer(
                            text=f"{ctx.author.name}",
                            icon_url=ctx.author.avatar
                        )            

                        if guild.rules_channel == None:
                            rulebutton = discord.ui.Button(
                                style=discord.ButtonStyle.danger,
                                emoji="🔖",
                                label="無法前往規則頻道!"
                            )

                        else:
                            rulebutton = discord.ui.Button(
                                style=discord.ButtonStyle.success,
                                emoji="🔖",
                                label="點擊前往規則頻道!",
                                url=f"https://discord.com/channels/{guild.id}/{guild.rules_channel.id}"
                            )

                        chechboosterbutton = discord.ui.Button(
                            style=discord.ButtonStyle.success,
                            emoji="📖",
                            label="點擊查看加成此伺服器的人!"
                        )
                        backbutton = discord.ui.Button(
                            style=discord.ButtonStyle.success,
                            emoji="🔙",
                            label="回去伺服器資訊"
                        )

                        view = discord.ui.View(timeout=None)
                        view_else = discord.ui.View(timeout=None)            
                        view_else.add_item(backbutton)
                        view.add_item(rulebutton)
                        view.add_item(chechboosterbutton)
                        view.add_item(select_main)

                        async def checkboostercallback(interaction):   
                            await interaction.response.edit_message(
                                embed = discord.Embed(
                                title=f"加成此伺服器的人 ({len(guild.premium_subscribers)})",
                                description=f"{booster}"
                                ),
                            view = view_else
                            )

                        async def backcallback(interaction):   
                            await interaction.response.edit_message(
                                embed = embed,
                                view = view
                            )

                        chechboosterbutton.callback = checkboostercallback
                        backbutton.callback = backcallback

                        await interaction.response.edit_message(
                            embed=embed,
                            view = view
                        )

                view_main.add_item(select_main)
                select_main.callback = mainselectcallback
                bool2 = True

                await ctx.send(embed=embed_main,view = view_main)

        if bool1 == False:
            embed=func.embed_copy(des="待釐清... :(")

        if bool2 == False:
            await ctx.send(embed=embed)
            
        print(f"Time:'{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}'\nUser:'{ctx.author.name}' Guild:'{ctx.author.guild}' 'Command:'{ctx.command}'\nError:'{error}' bool1:'{bool1}' bool2:'{bool2}'")

with open("token","r") as f:
    bot.run(f.read())