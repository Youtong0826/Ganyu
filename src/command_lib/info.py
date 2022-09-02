import discord
import datetime
from lib.bot_config import bot_icon_url
from discord.ext import commands
from lib.function import SendBGM

def ServerDict(guild:discord.Guild):
    #主要語言: {guild.preferred_locale}
    #規則頻道: {rules_channel}",

    robot = 0
    person = 0
    booster = ""

    for n in guild.members:
        if n.bot:
            robot += 1
        else:
            person += 1

    if guild.premium_progress_bar_enabled:
        bar = "已開啟"

    else:
        bar = "未開啟"

    for n in guild.premium_subscribers:
        booster += f"{n.mention}\n"

    if booster == "":
        booster = "無"

    if guild.rules_channel != None:
        rules_channel = f"{guild.rules_channel.mention}"

    else:
        rules_channel = "無"

    emojis = []
    animated_emojis = []

    for n in guild.emojis:

        if n.animated:
            animated_emojis.append(n)

        else:
            emojis.append(n)

    embed_main = discord.Embed(
        title=f'{guild}',
        color=0x9c8fff,
        timestamp=datetime.datetime.utcnow()
    )
    if guild.icon != None:
        embed_main.set_thumbnail(
            url=guild.icon
        )
            
    embed_main.set_footer(
        text=f"serverinfo | 伺服器資訊",
        icon_url=bot_icon_url
    )

    moreinfobutton = discord.ui.Button(
        style=discord.ButtonStyle.primary,
        emoji="📘",
        label="更多資訊!"
    )

    checkboosterbutton = discord.ui.Button(
        style=discord.ButtonStyle.success,
        emoji="📖",
        label="加成的大大"
    )

    backbutton = discord.ui.Button(
        style=discord.ButtonStyle.success,
        emoji="🔙",
        label="back"
    )
    
    rolesbutton = discord.ui.Button(
        style=discord.ButtonStyle.primary,
        emoji="📋",
        label="身分組"
    )

    view_main = discord.ui.View(timeout=None)
    view = discord.ui.View(timeout=None)
    view.add_item(backbutton)
    view_main.add_item(moreinfobutton)
    view_main.add_item(checkboosterbutton)
    view_main.add_item(rolesbutton)
    

    async def moreinfocallback(interaction:discord.Interaction):
        embed = discord.Embed(
            title=guild.name,
            color=discord.Colour.random()
        )

        embed.set_thumbnail(url=guild.icon)

        embed.set_footer(text="What's more?",icon_url=bot_icon_url)

        moreinfo = {
            "⚜️ __加成次數__": f"{guild.premium_subscription_count}",
            "🔱 __加成等級__" : f"{guild.premium_tier}",
            "📈 __活人__" : f"{person}",
            "📊 __機器人__" : f"{robot}",
            "🐷 __表情符號(靜態)__" : f"{len(emojis)}",
            "🐸 __表情符號(動態)__" : f"{len(animated_emojis)}"
        }

        for n in moreinfo:
            embed.add_field(name=n,value=moreinfo[n],inline=False)

        await interaction.response.edit_message(embed=embed,view=view)

    async def cbbcallback(interaction):
        await interaction.response.edit_message(
            embed=discord.Embed(
                title=f"加成此伺服器的人({len(guild.premium_subscribers)})",
                description=f"{booster}"),
                view=view
        )

    async def backcallback(interaction):
        await interaction.response.edit_message(
            embed=embed_main,
            view=view_main
        )
            
    async def rolescallback(interaction):
        roles_count = 0
        roles = ""
        for n in guild.roles:
            if n.name != '@everyone':
                roles += f"{n.mention} | "
                roles_count += 1
                if len(roles) >= 1014:
                    roles += f" +{len(guild.roles) -1  - roles_count} Roles..."
                    break


        await interaction.response.edit_message(
            embed=discord.Embed(
                title=f"身分組[{len(guild.roles)-1}]",
                description=f"{roles}"
            ),
            view=view
        )

    checkboosterbutton.callback = cbbcallback
    backbutton.callback = backcallback
    rolesbutton.callback = rolescallback
    moreinfobutton.callback = moreinfocallback

    normal ={
        "🚹 __服主__" : guild.owner.mention,
        "💳 __ID__" : guild.id,
        "🗓️ __創建時間__" : guild.created_at.strftime('%Y/%m/%d'),
        "📈 __人數__" : guild.member_count,
        "📊 __頻道數__" : len(guild.text_channels) + len(guild.voice_channels),
        "👾 __表情符號__" : len(guild.emojis),
        "📌 __身分組__" : len(guild.roles),               
            }

    setting = {
        "Embed" : embed_main,
        "View" : view_main
    }

    for n in normal:
        embed_main.add_field(name=n,value=normal[n],inline=False)
    
    return setting

def BotDict(bot:commands.Bot):
    embed = discord.Embed(
            title=f"{bot.user}",
            color=0x9c8ff,
            timestamp=datetime.datetime.utcnow()
        )

    botinfo = {
        "📆 創建時間":{"value":"`2022/1/21(GMT+8:00)`","inline":False},
        "📜 ID":{"value":"`921673886049910795`","inline":False},
        "🌐 伺服器" : {"value":f"`{len(bot.guilds)}`","inline":True},
        "📊 用戶" : {"value":f"`{len(bot.users)}`","inline":True},
        "💫 Ping" : {"value":f"`{round(bot.latency * 1000)} ms`","inline":True}
    }

    for n in botinfo:
        embed.add_field(name=n,value=botinfo[n].get("value"),inline=botinfo[n].get("inline"))
        
    embed.set_footer(
        text="made by Ganyu-Bot-Devs",
        icon_url="https://cdn.discordapp.com/avatars/856041155341975582/a5a57f0acdd5c5fb868c9ad50cf7c319.png?size=256"
    )

    invitebutton = discord.ui.Button(
        style=discord.ButtonStyle.primary,
        label="Invite me!",
        emoji="🔗",
        url="https://ptb.discord.com/api/oauth2/authorize?client_id=921673886049910795&permissions=380108955712&scope=bot%20applications.commands"
    )

    supportbutton = discord.ui.Button(
        label="Support Server",
        emoji="❓",
        url="https://discord.gg/AVCWGuuUex"
    )

    Moreinfobutton = discord.ui.Button(
        style=discord.ButtonStyle.primary,
        label="更多資訊!",
        emoji="🔗",
    )

    main_view = discord.ui.View(timeout=None)
    main_view.add_item(invitebutton)
    main_view.add_item(supportbutton)

    setting = {
        "Embed" : embed,
        "View" : main_view
    }

    return setting

def UserDict(member:discord.Member):
    roles = ""
    roles_count = 0
    dbot = "No"
    nick = "無"

    if member.nick != None:
        nick = member.nick

    if member.bot:
        dbot = "Yes"

    for n in member.roles:
            if n.name != '@everyone':
                roles += f"{n.mention} | "
                roles_count += 1
                if len(roles) >= 1014:
                    roles += f" +{len(member.roles) - roles_count} Roles..."
                    roles = roles[:-1]
                    break

    if roles == "":
        roles = "無"

    embed_main = discord.Embed(
        title=f"{member.name} 的個人資訊 ",
        color=0x9c8fff,
        timestamp=datetime.datetime.utcnow()
    )

    if member.avatar != None:
        avatar = member.avatar

    else:
        avatar = member.default_avatar

    embed_main.set_thumbnail(
        url=avatar
    )

    info = {
        "🐬 暱稱" : {
            "value" : nick,
            "inline" : True
        },

        "🤖 Bot" : {
            "value" : dbot,
            "inline" : True
        },

        "💳 ID" : {
            "value" : f"`{member.id}`",
            "inline" : False
        },

        "📆 創建時間" : {
            "value" : member.created_at.strftime('%Y/%m/%d'),
            "inline" : True
        },

        "📆 加入時間" : {
            "value" : member.joined_at.strftime('%Y/%m/%d'),
            "inline" : True
        },

        f"📰 身分組[{len(member.roles)-1}]:" : {
            "value" : roles,
            "inline" : False
        }
    }

    for n in info:
        embed_main.add_field(name=n,value=info[n].get("value"),inline=info[n].get("inline"))
    
    embed_main.set_footer(
        text=f"userinfo | 用戶資訊",
        icon_url=bot_icon_url
    )

    main_view = discord.ui.View(timeout=None)
    back_view = discord.ui.View(timeout=None)

    moreinfobutton = discord.ui.Button(
        style = discord.ButtonStyle.primary,
        label="更多資訊!",
        emoji= "📘"
    )

    backbutton = discord.ui.Button(
        style = discord.ButtonStyle.primary,
        label="back",
        emoji= "🔙"
    )

    main_view.add_item(moreinfobutton)
    back_view.add_item(backbutton)

    async def moreinfobuttoncallback(interaction:discord.Interaction):
        psince = "尚未加成"
        pending = "已驗證"

        if member.premium_since != None:
            psince = member.premium_since

        if member.pending:
            pending = "未驗證"

        moreinfo = {
            "🖥️ 驗證" : f"`{pending}`",
            "🔱 加成的時間" : f"`{psince}`",
            "⚜️ 徽章數" : f"`{len(member.public_flags.all())}`"
        }

        embed = discord.Embed(
            title=f"{member.name} 的個人資訊"
        )

        embed.set_thumbnail(url=member.avatar)

        for n in moreinfo:
            embed.add_field(name=n,value=moreinfo[n],inline=False)

        await interaction.response.edit_message(embed=embed,view=back_view)

    async def backbuttoncallback(interaction:discord.Interaction):
        await interaction.response.edit_message(embed=embed_main,view=main_view)

    moreinfobutton.callback = moreinfobuttoncallback
    backbutton.callback = backbuttoncallback
    
    Setting = {"Embed" : embed_main,"View" : main_view}

    return Setting

async def Allinfo(ctx,bot,type="slash"):
    embed = discord.Embed(
        title="一次查看所有資訊!",
        color=discord.Colour.random(),
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
        ],
        placeholder="選擇你要查看的資訊"
        )

    async def mainselectcallback(interaction : discord.Interaction):

        if select_main.values[0] == "bot":
            info = BotDict(bot)
            embed = info["Embed"]
            view = info["View"]

        elif select_main.values[0] == "user":
            info = UserDict(ctx.author)
            embed = info["Embed"]
            view = info["View"]

        elif select_main.values[0] == "ser":
            info = ServerDict(ctx.author.guild)
            embed = info["Embed"]
            view = info["View"]

        view.add_item(select_main)

        await interaction.response.edit_message(embed=embed,view=view)

    view_main.add_item(select_main)
    select_main.callback = mainselectcallback
    
    if type == "command":
        await ctx.send(embed=embed, view=view_main)

    elif type == "slash":
        await ctx.respond(embed=embed,viwe=view_main)

    SendBGM(ctx)

async def Invite(ctx,type="slash"):
    link = "[邀請連結 | invite link](https://ptb.discord.com/api/oauth2/authorize?client_id=921673886049910795&permissions=294695021638&scope=bot%20applications.commands)"
    server_link = "[支援伺服器 | Support Server](https://discord.gg/AVCWGuuUex)"

    embed = discord.Embed(
        title="邀請我至你的伺服器!",
        description=f"{link}\n{server_link}",
        color=discord.Colour.random(),
    )

    

    #embed = discord.Embed(title="🚫此功能暫未開啟",color=discord.Colour.random())

    if type == "command":
        await ctx.send(embed=embed)

    elif type == "command":
        await ctx.respond(embed=embed)

    SendBGM(ctx)

async def Invites(ctx:discord.ApplicationContext,type="slash"):
    embed = discord.Embed(
        title=f"{ctx.guild.name} 的邀請榜", 
        color=discord.Color.blue()
    )

    context = ""
    invites = await ctx.guild.invites()

    invites.sort(key=lambda k: k.uses, reverse=True)

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


    inviters = []
        
    for n in invites: invites.remove(n) if n.inviter in inviters else inviters.append(n.inviter) 

    for index, invite in enumerate(invites):
        if index < 10:context += f"{numbers[index]} {str(invite.inviter)[:-5]} 邀請 {invite.uses} 人\n\n" 

    embed.description = context
    
    if type == "command":
        await ctx.send(embed=embed)
    
    elif type == "slash":
        await ctx.respond(embed=embed)

    SendBGM(ctx)

async def Roleinfo(ctx,role,type="slash"):
    if role != None:
        role_data = {
            "🗒️ 名字" : role.mention,
            "💳 id" : role.id,
            "📊 人數" : len(role.members),
            "🗓️ 創建時間" : role.created_at.strftime('%Y/%m/%d'),
            "👾 貼圖" : role.unicode_emoji
            }

        embed = discord.Embed(
            title=f'有關 {role.name} 身分組的資訊',
            color=role.color,
            timestamp=datetime.datetime.utcnow()
        )

        view = discord.ui.View(timeout=None)
        backview = discord.ui.View(timeout=None)

        checkbutton = discord.ui.Button(
            style=discord.ButtonStyle.success,
            label="擁有者",
            emoji="📊"
        )
        backbutton = discord.ui.Button(
            style=discord.ButtonStyle.primary,
            label="回去",
            emoji="🔙"
        )

        async def checkbuttoncallback(interaction:discord.Interaction):
            role_members = ""
            role_members_count = 0

            for n in role.members:
                role_members_count += 1
                role_members += f"{n.name}\n"
                if len(role_members) >= 1014:
                    role_members += f"+{len(role.members) - role_members_count}人.."

                    break
            checkembed = discord.Embed(
                title=f"擁有此身分組的人",
                description=role_members,
                color=discord.Colour.random()
            )

            await interaction.response.edit_message(embed=checkembed,view=backview)

        async def backbuttoncallback(interaction:discord.Interaction):
            await interaction.response.edit_message(embed=embed,view=view)
        
        for n in role_data:
            if n == None:
                n = "無"

            embed.add_field(name=n,value=role_data[n],inline=False)

        checkbutton.callback = checkbuttoncallback
        backbutton.callback = backbuttoncallback

        view.add_item(checkbutton)
        backview.add_item(backbutton)
  
    else:

        view = discord.ui.View()

        embed = discord.Embed(
            title="使用 g!roleinfo 取得身分組資訊!",
            description="使用方法❓ g!roleinfo `標註身分組/身分組名稱/身分組id`",
            color=discord.Colour.random()
        )

    embed.set_footer(
        text="rolenfo | 身分組資訊",
        icon_url=bot_icon_url
    )
    
    if type == "command":
        await ctx.send(embed=embed,view=view)

    elif type == "slash":
        await ctx.respond(embed=embed,view=view)

    SendBGM(ctx)

